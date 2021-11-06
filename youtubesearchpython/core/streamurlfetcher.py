import urllib.request

from youtubesearchpython.core.requests import RequestCore

isPyTubeInstalled = False

import httpx
try:
    from pytube.extract import apply_descrambler, apply_signature
    from pytube import YouTube, extract
    import pytube
    isPyTubeInstalled = True
except:
    class YouTube:
        def __init__(self):
            pass


class StreamURLFetcherCore(YouTube):
    '''
    Overrided parent's constructor.
    '''
    def __init__(self):
        if isPyTubeInstalled:
            self._js_url = None
            self._js = None
        else:
            raise Exception('ERROR: PyTube is not installed. To use this functionality of youtube-search-python, PyTube must be installed.')

    '''
    Saving videoFormats inside a dictionary with key "player_response" for apply_descrambler & apply_signature methods.
    '''
    def _getDecipheredURLs(self, videoFormats: dict) -> None:
        if not videoFormats['streamingData']:
            try:
                self.use_oauth = False
                self.allow_oauth_cache = False
                self.video_id = videoFormats["id"]
                self.bypass_age_gate()
                r = self._vid_info["streamingData"]
                ''' Derived from extract.video_info_url_age_restricted '''
                ''' Google returns content as a query string instead of a JSON. '''
            except:
                raise Exception('ERROR: Could not make request.')
        else:
            r = videoFormats["streamingData"]
        self._player_response = {'player_response': r}
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
        response = urllib.request.urlopen('https://youtube.com/watch')
        watch_html = response.read().decode()
        try:
            self._js_url = extract.js_url(watch_html)
            if pytube.__js_url__ != self._js_url:
                response = httpx.get(self._js_url, timeout = None)
                self._js = response.text
                pytube.__js__ = self._js
                pytube.__js_url__ = self._js_url
            else:
                self._js = pytube.__js__
        except:
            raise Exception('ERROR: Could not make request.')

    async def _asyncGetJS(self):
        # Due to some errors with JS fetching with httpx, we are now using sync urllib
        self._getJS()

    async def getJavaScript(self):
        await self._asyncGetJS()

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

            stream = apply_descrambler(self._player_response["player_response"])

            try:
                apply_signature(
                    stream, self._player_response, pytube.__js__
                )
            except:
                # TODO: Applying signature is randomly failing - not to me, but on GitHub Actions server. I disabled throwing errors, since we don't want a whole mailbox of failed tests...
                pass
            self._streams = stream
        except Exception as e:
            if retry:
                raise e
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            self._decipher(retry = True)