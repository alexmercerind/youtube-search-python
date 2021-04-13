isPyTubeInstalled = False

import httpx
from urllib.request import urlopen
from urllib.parse import parse_qs, urlencode
import json
try:
    from pytube.extract import apply_descrambler, apply_signature
    from pytube import YouTube, extract
    import pytube
    isPyTubeInstalled = True
except:
    class YouTube:
        def __init__(self):
            pass


class StreamURLFetcherInternal(YouTube):
    '''
    Overrided parent's constructor.
    '''
    def __init__(self):
        if isPyTubeInstalled:
            self._js_url = None
            self._js = None
            self._getJS()
        else:
            raise Exception('ERROR: PyTube is not installed. To use this functionality of youtube-search-python, PyTube must be installed.')

    '''
    Saving videoFormats inside a dictionary with key "player_response" for apply_descrambler & apply_signature methods.
    '''
    def _getDecipheredURLs(self, videoFormats: dict) -> None:
        self._player_response = {'player_response': videoFormats}
        if not videoFormats['streamingData']:
            try:
                ''' For getting streamingData in age restricted video. '''
                response = urlopen(
                    'https://youtube.com/get_video_info' + '?' + urlencode({
                        'video_id': videoFormats['id'],
                        'eurl': f'https://youtube.googleapis.com/v/{videoFormats["id"]}',
                        'sts': '',
                    }),
                    data = ''.encode('utf_8'),
                    timeout = None,
                )
                ''' Derived from extract.video_info_url_age_restricted '''
                ''' Google returns content as a query string instead of a JSON. '''
                self._player_response['player_response'] = json.loads(parse_qs(response.read().decode('utf_8'))["player_response"][0])
            except:
                raise Exception('ERROR: Could not make request.')
        self.video_id = videoFormats["id"]
        self._decipher()

    '''
    This method is derived from YouTube.prefetch.
    This method fetches player JavaScript & its URL from /watch endpoint on YouTube.
    Removed unnecessary methods & web requests as we already have metadata.
    Uses httpx.AsyncClient in place of requests.
    Removed v parameter from the query. (No idea about why PyTube bothered with that)
    '''
    def _getJS(self) -> None:
        try:
            response = urlopen('https://youtube.com/watch', timeout = None)
            watch_html = response.read().decode('utf_8')
            age_restricted = extract.is_age_restricted(watch_html)
            self._js_url = extract.js_url(watch_html)
            if pytube.__js_url__ != self._js_url:
                response = urlopen(self._js_url, timeout = None)
                self._js = response.read().decode('utf_8')
                pytube.__js__ = self._js
                pytube.__js_url__ = self._js_url
            else:
                self._js = pytube.__js__
        except:
            raise Exception('ERROR: Could not make request.')

    '''
    Not fetching for new player JavaScript if pytube.__js__ is not None or exception is not caused.
    '''
    def _decipher(self, retry: bool = False):
        if not pytube.__js__ or retry:
            self._getJS()
        try:
            '''
            These two are the main methods being used from PyTube.
            Used to decipher the stream URLs using player JavaScript & the player_response passed from the getStream method of this derieved class.
            These methods operate on the value of "player_response" key in dictionary of self._player_response & save _deciphered information in the "url_encoded_fmt_stream_map" key.
            '''
            apply_descrambler(self._player_response, "url_encoded_fmt_stream_map")
            apply_signature(
                self._player_response, "url_encoded_fmt_stream_map", pytube.__js__
            )
        except:
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            self._decipher(retry = False)
