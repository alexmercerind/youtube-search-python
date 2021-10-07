import json
from typing import Union, List
from urllib.parse import urlencode

from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.core.componenthandler import getValue, getVideoId


class VideoCore(RequestCore):
    def __init__(self, videoLink: str, componentMode: str, resultMode: int, timeout: int):
        super().__init__()
        self.timeout = timeout
        self.resultMode = resultMode
        self.componentMode = componentMode
        self.videoLink = videoLink
        self.url = 'https://www.youtube.com/watch' + '?' + urlencode({
            'v': getVideoId(self.videoLink)
        })

    def post_request_processing(self):
        self.__extractFromHTML()
        self.__parseSource()
        self.__getVideoComponent(self.componentMode)
        self.result = self.__videoComponent

    async def async_create(self):
        response = await self.asyncGetRequest()
        self.response = response.text
        if response.status_code == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def sync_create(self):
        response = self.syncGetRequest()
        self.response = response.text
        if response.status_code == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def __extractFromHTML(self):
        f1 = "var ytInitialPlayerResponse = "
        startpoint = self.response.find(f1)
        self.response = self.response[startpoint + len(f1):]
        f2 = ';var meta = '
        endpoint = self.response.find(f2)
        if startpoint and endpoint:
            startpoint += len(f1)
            endpoint += len(f2)
            r = self.response[:endpoint]
            r = r.replace(';var meta = ', "")
            self.response = r

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
                'id': getValue(self.responseSource, ['videoDetails', 'videoId']),
                'title': getValue(self.responseSource, ['videoDetails', 'title']),
                'viewCount': {
                    'text': getValue(self.responseSource, ['videoDetails', 'viewCount'])
                },
                'thumbnails': getValue(self.responseSource, ['videoDetails', 'thumbnail', 'thumbnails']),
                'description': getValue(self.responseSource, ['videoDetails', 'shortDescription']),
                'channel': {
                    'name': getValue(self.responseSource, ['videoDetails', 'author']),
                    'id': getValue(self.responseSource, ['videoDetails', 'channelId']),
                },
                'averageRating': getValue(self.responseSource, ['videoDetails', 'averageRating']),
                'keywords': getValue(self.responseSource, ['videoDetails', 'keywords']),
                'publishDate': getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'publishDate']),
                'uploadDate': getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'uploadDate']),
            }
            component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
            component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
            videoComponent.update(component)
        if mode in ['getFormats', None]:
            component = {
                'streamingData': getValue(self.responseSource, ['streamingData']),
            }
            videoComponent.update(component)
        self.__videoComponent = videoComponent
