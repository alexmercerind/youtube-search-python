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
        # For some reason, we cannot fetch JavaScript the old way, as PyTube's RegEx doesn't like it.
        self.video_id = videoFormats["id"]
        if not videoFormats["streamingData"]:
            vc = VideoCore(self.video_id, None, ResultMode.dict, None, False, overridedClient="ANDROID_EMBED")
            vc.sync_create()
            videoFormats = vc.result
            if not videoFormats["streamingData"]:
                raise Exception("streamingData is not present in Video.get. This is most likely a age-restricted video")
        self._player_response = videoFormats["streamingData"]["formats"]
        self._player_response.extend(videoFormats["streamingData"]["adaptiveFormats"])
        self.format_id = formatId
        self._decipher()

    def extract_js_url(self, res: str):
        if res:
            player_version = re.search(
                r'([0-9a-fA-F]{8})\\?', res)
            player_version = player_version.group().replace("\\", "")
            self._js_url = f'https://www.youtube.com/s/player/{player_version}/player_ias.vflset/en_US/base.js'
        else:
            raise Exception("Failed to retrieve JavaScript for this video")

    def _getJS(self) -> None:
        self.url = f'https://www.youtube.com/iframe_api'
        res = self.syncGetRequest()
        self.extract_js_url(res.text)

    async def getJavaScript(self):
        self.url = f'https://www.youtube.com/iframe_api'
        res = await self.asyncGetRequest()
        self.extract_js_url(res.text)

    def _decipher(self, retry: bool = False):
        if not self._js_url or retry:
            self._js_url = None
            self._js = None
            self._getJS()
        try:
            #print(self._player_response)
            for yt_format in self._player_response:
                if self.format_id == yt_format["itag"] or self.format_id is None:
                    if getValue(yt_format, ["url"]):
                        # This is a non-ciphered URL
                        yt_format["throttled"] = False
                        self._streams.append(yt_format)
                        continue
                    else:
                        cipher = yt_format["signatureCipher"]
                    #cipher = "s=F%3DX%3DgIkn_MWCUvQZ__3tR_7gPNDBeOz8n9M0WGxNtIZ6zwxAiA-VALQ9F5bz%3DW8I_Z8WfXPLHjEGEn_JRVVu7BcNJJfjKAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D137%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D75694686%26dur%3D188.813%26lmt%3D1601811652909447%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgTGJdeFFnVZy97rzAeBnJCSdcY7KWBCa21RQ9ZvkH0KsCIQD1-Vzcj53p39l_DWtK1b69VjQmtBi_SIZOZD0hzXHJNA%253D%253D"
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
                    #print("It is ciphered")
                    signature = self.ytie._decrypt_signature(sc['s'][0], self.video_id, self._js_url)
                    sp = try_get(sc, lambda x: x['sp'][0]) or 'signature'
                    fmt_url += '&' + sp + '=' + signature
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
