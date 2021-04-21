isPyTubeInstalled = False

import asyncio
import httpx
try:
    from youtubesearchpython.__future__.internal.json import loads
    from pytube.extract import apply_descrambler, apply_signature
    from pytube import YouTube, extract
    from urllib.parse import parse_qs
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
        self._js_url = None
        self._js = None
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
        try:
            global js_url
            async with httpx.AsyncClient() as client:
                response = await client.get('https://www.youtube.com/watch', timeout = None)
            watchHTML = response.text
            loop = asyncio.get_running_loop()
            self._js_url = await loop.run_in_executor(None, extract.js_url, watchHTML)
            if js_url != self._js_url:
                async with httpx.AsyncClient() as client:
                    response = await client.get(self._js_url, timeout = None)
                self._js = response.text
        except:
            raise Exception('ERROR: Could not make request.')

    '''
    Saving videoFormats inside a dictionary with key 'player_response' for apply_descrambler & apply_signature methods.
    '''
    async def _getDecipheredURLs(self, videoFormats: dict) -> None:
        self._player_response = {'player_response': videoFormats}
        if not videoFormats['streamingData']:
            try:
                ''' For getting streamingData in age restricted video. '''
                async with httpx.AsyncClient() as client:
                    ''' Derived from extract.video_info_url_age_restricted '''
                    response = await client.post(
                        'https://youtube.com/get_video_info',
                        params = {
                            'video_id': videoFormats['id'],
                            'eurl': f'https://youtube.googleapis.com/v/{videoFormats["id"]}',
                            'sts': None,
                        },
                        timeout = None,
                    )
                    ''' Google returns content as a query string instead of a JSON. '''
                    self._player_response['player_response'] = await loads(parse_qs(response.text)["player_response"][0])
            except:
                raise Exception('ERROR: Could not make request.')
        self.video_id = videoFormats["id"]
        await self._decipher()

    async def _decipher(self, retry: bool = False):
        '''
        Not fetching for new player JavaScript if self._js is not None or exception is not caused.
        '''
        if not self._js or retry:
            await self.getJavaScript()
        try:
            '''
            These two are the main methods being used from PyTube.
            Used to _decipher the stream URLs using player JavaScript & the player_response passed from the getStream method of this derieved class.
            These methods operate on the value of "player_response" key in dictionary of self._player_response & save _deciphered information in the "url_encoded_fmt_stream_map" key.
            '''
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(None, apply_descrambler, self._player_response, 'url_encoded_fmt_stream_map')
            await loop.run_in_executor(None, apply_signature, self._player_response, 'url_encoded_fmt_stream_map', self._js)
            
        except:
            '''
            Fetch updated player JavaScript to get new cipher algorithm.
            '''
            await self._decipher(retry = False)
