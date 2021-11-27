import copy
import json
from typing import Union, List
from urllib.parse import urlencode

from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.core.componenthandler import getValue, getVideoId


class VideoCore(RequestCore):
    def __init__(self, videoLink: str, componentMode: str, resultMode: int, timeout: int, enableHTML: bool):
        super().__init__()
        self.timeout = timeout
        self.resultMode = resultMode
        self.componentMode = componentMode
        self.videoLink = videoLink
        self.enableHTML = enableHTML

    def post_request_processing(self):
        self.__parseSource()
        self.__getVideoComponent(self.componentMode)
        self.result = self.__videoComponent

    def prepare_innertube_request(self):
        self.url = 'https://www.youtube.com/youtubei/v1/player' + "?" + urlencode({
            'key': searchKey,
            'contentCheckOk': True,
            'racyCheckOk': True,
            "videoId": getVideoId(self.videoLink)
        })
        self.data = {
            'context': {
                'client': {
                    'clientName': 'ANDROID',
                    'clientVersion': '16.20'
                }
            },
            'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
        }

    def __extractFromHTML(self):
        f1 = "var ytInitialPlayerResponse = "
        startpoint = self.htmlresponse.find(f1)
        self.htmlresponse = self.htmlresponse[startpoint + len(f1):]
        f2 = ';var meta = '
        endpoint = self.htmlresponse.find(f2)
        if startpoint and endpoint:
            startpoint += len(f1)
            endpoint += len(f2)
            r = self.htmlresponse[:endpoint]
            r = r.replace(';var meta = ', "")
            self.htmlresponse = r
        try:
            self.HTMLresponseSource = json.loads(self.htmlresponse)
        except Exception as e:
            raise Exception('ERROR: Could not parse YouTube response.')

    async def async_create(self):
        self.prepare_innertube_request()
        response = await self.asyncPostRequest()
        self.response = response.text
        if response.status_code == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def sync_create(self):
        self.prepare_innertube_request()
        response = self.syncPostRequest()
        self.response = response.text
        if response.status_code == 200:
            self.post_request_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def prepare_html_request(self):
        self.url = 'https://www.youtube.com/watch' + '?' + urlencode({'v': getVideoId(self.videoLink)})

    def sync_html_create(self):
        self.prepare_html_request()
        response = self.syncGetRequest()
        self.htmlresponse = response.text
        if response.status_code == 200:
            self.__extractFromHTML()
        else:
            raise Exception('ERROR: Invalid status code.')

    async def async_html_create(self):
        self.prepare_html_request()
        response = await self.asyncGetRequest()
        self.htmlresponse = response.text
        if response.status_code == 200:
            self.__extractFromHTML()
        else:
            raise Exception('ERROR: Invalid status code.')

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
                'duration': {
                    'secondsText': getValue(self.responseSource, ['videoDetails', 'lengthSeconds']),
                },
                'viewCount': {
                    'text': getValue(self.responseSource, ['videoDetails', 'viewCount'])
                },
                'thumbnails': getValue(self.responseSource, ['videoDetails', 'thumbnail', 'thumbnails']),
                'description': getValue(self.responseSource, ['videoDetails', 'shortDescription']),
                'channel': {
                    'name': getValue(self.responseSource, ['videoDetails', 'author']),
                    'id': getValue(self.responseSource, ['videoDetails', 'channelId']),
                },
                'allowRatings': getValue(self.responseSource, ['videoDetails', 'allowRatings']),
                'averageRating': getValue(self.responseSource, ['videoDetails', 'averageRating']),
                'keywords': getValue(self.responseSource, ['videoDetails', 'keywords']),
                'isLiveContent': getValue(self.responseSource, ['videoDetails', 'isLiveContent']),
                'publishDate': getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'publishDate']),
                'uploadDate': getValue(self.responseSource, ['microformat', 'playerMicroformatRenderer', 'uploadDate']),
            }
            component['isLiveNow'] = component['isLiveContent'] and component['duration']['secondsText'] == "0"
            component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
            component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
            videoComponent.update(component)
        if mode in ['getFormats', None]:
            videoComponent.update(
                {
                    "streamingData": getValue(self.responseSource, ["streamingData"])
                }
            )
        if self.enableHTML:
            videoComponent["publishDate"] = getValue(self.HTMLresponseSource, ['microformat', 'playerMicroformatRenderer', 'publishDate'])
            videoComponent["uploadDate"] = getValue(self.HTMLresponseSource, ['microformat', 'playerMicroformatRenderer', 'uploadDate'])
        self.__videoComponent = videoComponent
