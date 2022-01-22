import copy
import urllib.request
import urllib.parse

import re

from youtubesearchpython.core.constants import ResultMode
from youtubesearchpython.core.video import VideoCore
from youtubesearchpython.core.componenthandler import getValue
from youtubesearchpython.core.requests import RequestCore

isYtDLPinstalled = False

try:
    from yt_dlp.extractor.youtube import YoutubeBaseInfoExtractor, YoutubeIE
    from yt_dlp import YoutubeDL
    from yt_dlp.utils import url_or_none, try_get, update_url_query, ExtractorError

    isYtDLPinstalled = True
except:
    pass


class StreamURLFetcherCore(RequestCore):
    '''
    Overrided parent's constructor.
    '''
    def __init__(self):
        if isYtDLPinstalled:
            super().__init__()
            self._js_url = None
            self._js = None
            #self.ytdlp = YoutubeBaseInfoExtractor()
            self.ytie = YoutubeIE()
            self.ytie.set_downloader(YoutubeDL())
            self._streams = []
        else:
            raise Exception('ERROR: yt-dlp is not installed. To use this functionality of youtube-search-python, yt-dlp must be installed.')

    '''
    Saving videoFormats inside a dictionary with key "player_response" for apply_descrambler & apply_signature methods.
    '''
    def _getDecipheredURLs(self, videoFormats: dict, formatId: int = None) -> None:
        # We reset our stream list
        # See https://github.com/alexmercerind/youtube-search-python/pull/155#discussion_r790165920
        # If we don't reset it, then it's going to cache older URLs and as we are using length comparison in upper class
        # it would return None, because length is not 1
        self._streams = []

        self.video_id = videoFormats["id"]
        if not videoFormats["streamingData"]:
            # Video is age-restricted. Try to retrieve it using ANDROID_EMBED client and override old response.
            # This works most time.
            vc = VideoCore(self.video_id, None, ResultMode.dict, None, False, overridedClient="ANDROID_EMBED")
            vc.sync_create()
            videoFormats = vc.result
            if not videoFormats["streamingData"]:
                # Video is:
                # 1. Either age-restricted on so called level 3
                # 2. Needs payment (is only for users that use so called "Join feature")
                raise Exception("streamingData is not present in Video.get. This is most likely a age-restricted video")
        # We deepcopy a list, otherwise it would duplicate
        # See https://github.com/alexmercerind/youtube-search-python/pull/155#discussion_r790165920
        self._player_response = copy.deepcopy(videoFormats["streamingData"]["formats"])
        self._player_response.extend(videoFormats["streamingData"]["adaptiveFormats"])
        self.format_id = formatId
        self._decipher()

    def extract_js_url(self, res: str):
        if res:
            # My modified RegEx derived from yt-dlp, that retrieves JavaScript version
            # Source: https://github.com/yt-dlp/yt-dlp/blob/e600a5c90817f4caac221679f6639211bba1f3a2/yt_dlp/extractor/youtube.py#L2258
            player_version = re.search(
                r'([0-9a-fA-F]{8})\\?', res)
            player_version = player_version.group().replace("\\", "")
            self._js_url = f'https://www.youtube.com/s/player/{player_version}/player_ias.vflset/en_US/base.js'
        else:
            raise Exception("Failed to retrieve JavaScript for this video")

    def _getJS(self) -> None:
        # Here we get a JavaScript that links to specific Player JavaScript
        self.url = 'https://www.youtube.com/iframe_api'
        res = self.syncGetRequest()
        self.extract_js_url(res.text)

    async def getJavaScript(self):
        # Same as in _getJS(), except it's asynchronous
        self.url = 'https://www.youtube.com/iframe_api'
        res = await self.asyncGetRequest()
        self.extract_js_url(res.text)

    def _decipher(self, retry: bool = False):
        if not self._js_url or retry:
            self._js_url = None
            self._js = None
            self._getJS()
        try:
            # We need to decipher one URL at time.
            for yt_format in self._player_response:
                # If format_id is specified, then it means that we requested only for one URL (ITAG), thus we can skip
                # all other ITAGs, which would take up our precious system resources and our valuable time
                if self.format_id == yt_format["itag"] or self.format_id is None:
                    # If "url" is specified in JSON, it is definitely an unciphered URL.
                    # Thus we can skip deciphering completely.
                    if getValue(yt_format, ["url"]):
                        # This is a non-ciphered URL
                        yt_format["throttled"] = False
                        self._streams.append(yt_format)
                        continue
                    else:
                        cipher = yt_format["signatureCipher"]
                    # Some deciphering magic from yt-dlp
                    # Source: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/youtube.py#L2972-L2981
                    sc = urllib.parse.parse_qs(cipher)
                    fmt_url = url_or_none(try_get(sc, lambda x: x['url'][0]))
                    encrypted_sig = try_get(sc, lambda x: x['s'][0])
                    if not (sc and fmt_url and encrypted_sig):
                        # It's not ciphered
                        yt_format["throttled"] = False
                        self._streams.append(yt_format)
                        continue
                    if not cipher:
                        continue
                    signature = self.ytie._decrypt_signature(sc['s'][0], self.video_id, self._js_url)
                    sp = try_get(sc, lambda x: x['sp'][0]) or 'signature'
                    fmt_url += '&' + sp + '=' + signature

                    # Some magic to unthrottle streams
                    # Source: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/youtube.py#L2983-L2993
                    query = urllib.parse.parse_qs(fmt_url)
                    throttled = False
                    if query.get('n'):
                        try:
                            fmt_url = update_url_query(fmt_url, {
                                'n': self.ytie._decrypt_nsig(query['n'][0], self.video_id, self._js_url)})
                        except ExtractorError as e:
                            throttled = True
                    yt_format["url"] = fmt_url
                    yt_format["throttled"] = throttled
                    self._streams.append(yt_format)
        except Exception as e:
            if retry:
                raise e
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            self._decipher(retry=True)
