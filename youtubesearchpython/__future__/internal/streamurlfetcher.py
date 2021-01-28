isPyTubeInstalled = False


import asyncio
import httpx
try:
    from pytube.__main__ import apply_descrambler, apply_signature
    from pytube import YouTube, extract
    isPyTubeInstalled = True
except:
    class YouTube:
        def __init__(self):
            pass


js_url = None


class StreamURLFetcherInternal(YouTube):
    '''
    Overrided parent's constructor.
    '''
    def __init__(self):
        self.js_url = None
        self.js = None
        if not isPyTubeInstalled:
            raise Exception('ERROR: PyTube is not installed. To use this functionality of youtube-search-python, PyTube must be installed.')

    '''
    This method is derived from YouTube.prefetch.
    This method fetches player JavaScript & its URL from /watch endpoint on YouTube.
    Removed unnecessary methods & web requests as we already have metadata.
    Uses httpx.AsyncClient in place of requests.
    Removed v parameter from the query. (No idea about why PyTube bothered with that)
    '''
    async def getJavaScript(self) -> None:
        '''Gets player JavaScript from YouTube, avoid calling more than once.
        '''
        global js_url
        async with httpx.AsyncClient() as client:
            response = await client.get('https://youtube.com/watch', timeout = None)
        watch_html = response.text
        age_restricted = extract.is_age_restricted(watch_html)
        if age_restricted:
            async with httpx.AsyncClient() as client:
                response = await client.get('https://www.youtube.com/embed', timeout = None)
            embed_html = response.text
            self.js_url = extract.js_url(embed_html)
        else:
            self.js_url = extract.js_url(watch_html)
        if js_url != self.js_url:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.js_url, timeout = None)
            self.js = response.text

    '''
    Saving videoFormats inside a dictionary with key "player_response" for apply_descrambler & apply_signature methods.
    '''
    async def _getDecipheredURLs(self, videoFormats: dict) -> None:
        self.player_response = {'player_response': videoFormats}
        self.video_id = videoFormats["id"]
        await self._decipher()

    async def _decipher(self, retry: bool = False):
        '''
        Not fetching for new player JavaScript if self.js is not None or exception is not caused.
        '''
        if not self.js or retry:
            await self.getJavaScript()
        try:
            '''
            These two are the main methods being used from PyTube.
            Used to _decipher the stream URLs using player JavaScript & the player_response passed from the getStream method of this derieved class.
            These methods operate on the value of "player_response" key in dictionary of self.player_response & save _deciphered information in the "url_encoded_fmt_stream_map" key.
            '''
            loop = asyncio.get_running_loop()
            loop.run_in_executor(None, apply_descrambler, self.player_response, 'url_encoded_fmt_stream_map')
            loop.run_in_executor(None, apply_signature, self.player_response, 'url_encoded_fmt_stream_map', self.js)
            
        except:
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            await self._decipher(retry = False)
