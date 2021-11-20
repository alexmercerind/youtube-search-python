import json
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
        # For some reason, we cannot fetch JavaScript the old way, as PyTube's RegEx doesn't like it.
        self.video_id = videoFormats["id"]
        self._player_response = videoFormats
        if not videoFormats['streamingData']:
            try:
                self.use_oauth = False
                self.allow_oauth_cache = False
                self.bypass_age_gate()
                self._player_response = self._vid_info
            except:
                raise Exception('ERROR: Could not make request.')

        # We use this to retrieve JavaScript
        url = f"https://www.youtube.com/watch?v={self.video_id}"
        self.youtube = pytube.YouTube(url)

        self._decipher()

    '''
    This method is derived from YouTube.prefetch.
    This method fetches player JavaScript & its URL from /watch endpoint on YouTube.
    Removed unnecessary methods & web requests as we already have metadata.
    Uses httpx.AsyncClient in place of requests.
    Removed v parameter from the query. (No idea about why PyTube bothered with that)
    '''
    def _getJS(self) -> None:
        self._js = self.youtube.js

    async def getJavaScript(self):
        # we don't wanna break compatibility, so we just pass.
        # We retrieve Player JavaScript using _getDecipheredURLs()
        pass

    '''
    Not fetching for new player JavaScript if pytube.__js__ is not None or exception is not caused.
    '''
    def _decipher(self, retry: bool = False):
        if not pytube.__js__ or retry:
            self.youtube._js = None
            self.youtube._js_url = None
            pytube.__js__ = None
            pytube.__js_url__ = None
            self._getJS()
        try:
            '''
            These two are the main methods being used from PyTube.
            Used to decipher the stream URLs using player JavaScript & the player_response passed from the getStream method of this derieved class.
            These methods operate on the value of "player_response" key in dictionary of self._player_response & save _deciphered information in the "url_encoded_fmt_stream_map" key.
            '''

            stream = apply_descrambler(self._player_response["streamingData"])
            apply_signature(
                stream, self._player_response, pytube.__js__
            )
            self._streams = stream
        except Exception as e:
            if retry:
                raise e
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            self._decipher(retry = True)