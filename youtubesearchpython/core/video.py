import json
from typing import Union, List
from urllib.parse import urlencode

import httpx

from youtubesearchpython.core.constants import *


class VideoCore:
    def __init__(self, videoLink: str, componentMode: str, resultMode: int, timeout: int):
        self.timeout = timeout
        self.resultMode = resultMode
        self.componentMode = componentMode
        self.videoLink = videoLink

    def post_request_processing(self):
        self.__extractFromHTML()
        self.__parseSource()
        self.__getVideoComponent(self.componentMode)
        self.result = self.__videoComponent

    async def async_create(self):
        statusCode = await self.__makeAsyncRequest(self.__getVideoId(self.videoLink))
        if statusCode == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def sync_create(self):
        statusCode = self.__makeRequest(self.__getVideoId(self.videoLink))
        if statusCode == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def __extractFromHTML(self):
        f1 = "var ytInitialPlayerResponse = "
        startpoint = self.response.find(f1)
        self.response = self.response[startpoint + len(f1):]
        f2 = ';var meta = '
        endpoint = self.response.find(f2)
        #print(startpoint)
        #print(endpoint)
        if startpoint and endpoint:
            startpoint += len(f1)
            endpoint += len(f2)
            r = self.response[:endpoint]
            r = r.replace(';var meta = ', "")
            self.response = r

    def __getVideoId(self, videoLink: str) -> str:
        if 'youtu.be' in videoLink:
            if videoLink[-1] == '/':
                return videoLink.split('/')[-2]
            return videoLink.split('/')[-1]
        elif 'youtube.com' in videoLink:
            if '&' not in videoLink:
                return videoLink[videoLink.index('v=') + 2:]
            return videoLink[videoLink.index('v=') + 2: videoLink.index('&')]
        else:
            return videoLink

    def __makeRequest(self, videoId: str) -> int:
        request = httpx.get(
            'https://www.youtube.com/watch' + '?' + urlencode({
                'v': videoId
            }),
            headers={
                'User-Agent': userAgent,
            },
            timeout=self.timeout
        )
        try:
            self.response = request.text
            return request.status_code
        except:
            raise Exception('ERROR: Could not make request.')

    async def __makeAsyncRequest(self, videoId: str) -> int:
        async with httpx.AsyncClient() as client:
            request = await client.get(
                'https://www.youtube.com/watch' + '?' + urlencode({
                    'v': videoId
                }),
                headers={
                    'User-Agent': userAgent,
                },
                timeout=self.timeout
            )
        try:
            self.response = request.text
            return request.status_code
        except:
            raise Exception('ERROR: Could not make request.')

    def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response)
        except Exception as e:
            raise Exception('ERROR: Could not parse YouTube response.')

    def __result(self, mode: int) -> Union[dict, str]:
        if mode == ResultMode.dict:
            return self.__videoComponent
        elif mode == ResultMode.json:
            return json.dumps(self.__videoComponent, indent=4)

    def __getVideoComponent(self, mode: str) -> None:
        videoComponent = {}
        if mode in ['getInfo', None]:
            component = {
                'id': self.__getValue(self.responseSource, ['videoDetails', 'videoId']),
                'title': self.__getValue(self.responseSource, ['videoDetails', 'title']),
                'viewCount': {
                    'text': self.__getValue(self.responseSource, ['videoDetails', 'viewCount'])
                },
                'thumbnails': self.__getValue(self.responseSource, ['videoDetails', 'thumbnail', 'thumbnails']),
                'description': self.__getValue(self.responseSource, ['videoDetails', 'shortDescription']),
                'channel': {
                    'name': self.__getValue(self.responseSource, ['videoDetails', 'author']),
                    'id': self.__getValue(self.responseSource, ['videoDetails', 'channelId']),
                },
                'averageRating': self.__getValue(self.responseSource, ['videoDetails', 'averageRating']),
                'keywords': self.__getValue(self.responseSource, ['videoDetails', 'keywords']),
                'publishDate': self.__getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'publishDate']),
                'uploadDate': self.__getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'uploadDate']),
            }
            component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
            component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
            videoComponent.update(component)
        if mode in ['getFormats', None]:
            component = {
                'streamingData': self.__getValue(self.responseSource, ['streamingData']),
            }
            videoComponent.update(component)
        self.__videoComponent = videoComponent

    def __getValue(self, source: dict, path: List[str]) -> Union[str, int, dict, None]:
        value = source
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = None
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = None
                    break
        return value