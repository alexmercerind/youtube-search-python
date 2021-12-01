import collections
import copy
import itertools
import json
from typing import Iterable, Mapping, Tuple, TypeVar, Union, List
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore


K = TypeVar("K")
T = TypeVar("T")


class PlaylistCore(RequestCore):
    playlistComponent = None
    result = None
    continuationKey = None

    def __init__(self, playlistLink: str, componentMode: str, resultMode: int, timeout: int):
        super().__init__()
        self.componentMode = componentMode
        self.resultMode = resultMode
        self.timeout = timeout
        self.url = playlistLink

    def post_processing(self):
        self.__parseSource()
        self.__getComponents()
        if self.resultMode == ResultMode.json:
            self.result = json.dumps(self.playlistComponent, indent=4)
        else:
            self.result = self.playlistComponent

    def sync_create(self):
        statusCode = self.__makeRequest()
        if statusCode == 200:
            self.post_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    async def async_create(self):
        # Why do I use sync request in a async function, you might ask
        # Well, there were some problems with httpx.
        # Until I solve those problems, it is going to stay this way.
        statusCode = await self.__makeAsyncRequest()
        if statusCode == 200:
            self.post_processing()
        else:
            raise Exception('ERROR: Invalid status code.')

    def next_post_processing(self):
        self.__parseSource()
        self.__getNextComponents()
        if self.resultMode == ResultMode.json:
            self.result = json.dumps(self.playlistComponent, indent=4)
        else:
            self.result = self.playlistComponent

    def _next(self):
        self.prepare_next_request()
        if self.continuationKey:
            statusCode = self.syncPostRequest()
            self.response = statusCode.text
            if statusCode.status_code == 200:
                self.next_post_processing()
            else:
                raise Exception('ERROR: Invalid status code.')

    async def _async_next(self):
        if self.continuationKey:
            self.prepare_next_request()
            statusCode = await self.asyncPostRequest()
            self.response = statusCode.text
            if statusCode.status_code == 200:
                self.next_post_processing()
            else:
                raise Exception('ERROR: Invalid status code.')
        else:
            await self.async_create()
    
    def prepare_first_request(self):
        self.url.strip('/')
        id = self.url.replace("https://www.youtube.com/playlist?list=", "")
        self.url = 'https://www.youtube.com/youtubei/v1/browse' + '?' + urlencode({
            'key': searchKey,
        })
        browseId = "VL" + id if not id.startswith("VL") else id
        self.data = {
            "browseId": browseId,
        }
        self.data.update(copy.deepcopy(requestPayload))

    def __makeRequest(self) -> int:
        self.prepare_first_request()
        request = self.syncPostRequest()
        self.response = request.text
        return request.status_code
    
    async def __makeAsyncRequest(self) -> int:
        self.prepare_first_request()
        request = await self.asyncPostRequest()
        self.response = request.text
        return request.status_code

    def prepare_next_request(self):
        requestBody = copy.deepcopy(requestPayload)
        requestBody['continuation'] = self.continuationKey
        self.data = requestBody
        self.url = 'https://www.youtube.com/youtubei/v1/browse' + '?' + urlencode({
            'key': searchKey,
        })

    def __makeNextRequest(self) -> int:
        response = self.syncPostRequest()
        try:
            self.response = response.text
            return response.status_code
        except:
            raise Exception('ERROR: Could not make request.')

    def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response)
        except:
            raise Exception('ERROR: Could not parse YouTube response.')

    def __getComponents(self) -> None:
        inforenderer = self.responseSource["sidebar"]["playlistSidebarRenderer"]["items"][0]["playlistSidebarPrimaryInfoRenderer"]
        channelrenderer = self.responseSource["sidebar"]["playlistSidebarRenderer"]["items"][1]["playlistSidebarSecondaryInfoRenderer"]["videoOwner"]["videoOwnerRenderer"]
        videorenderer = self.__getFirstValue(self.responseSource, ["contents", "twoColumnBrowseResultsRenderer", "tabs", None, "tabRenderer", "content", "sectionListRenderer", "contents", None, "itemSectionRenderer", "contents", None, "playlistVideoListRenderer", "contents"])
        videos = []
        for video in videorenderer:
            try:
                video = video["playlistVideoRenderer"]
                j = {
                    "id": self.__getValue(video, ["videoId"]),
                    "thumbnails": self.__getValue(video, ["thumbnail", "thumbnails"]),
                    "title": self.__getValue(video, ["title", "runs", 0, "text"]),
                    "channel": {
                        "name": self.__getValue(video, ["shortBylineText", "runs", 0, "text"]),
                        "id": self.__getValue(video, ["shortBylineText", "runs", 0, "navigationEndpoint", "browseEndpoint", "browseId"]),
                        "link": self.__getValue(video, ["shortBylineText", "runs", 0, "navigationEndpoint", "browseEndpoint", "canonicalBaseUrl"]),
                    },
                    "duration": self.__getValue(video, ["lengthText", "simpleText"]),
                    "accessibility": {
                        "title": self.__getValue(video, ["title", "accessibility", "accessibilityData", "label"]),
                        "duration": self.__getValue(video, ["lengthText", "accessibility", "accessibilityData", "label"]),
                    },
                    "link": "https://www.youtube.com" + self.__getValue(video, ["navigationEndpoint", "commandMetadata", "webCommandMetadata", "url"]),
                }
                videos.append(j)
            except:
                pass

        playlistElement = {
            'info': {
                "id": self.__getValue(inforenderer, ["title", "runs", 0, "navigationEndpoint", "watchEndpoint", "playlistId"]),
                "thumbnails": self.__getValue(inforenderer, ["thumbnailRenderer", "playlistVideoThumbnailRenderer", "thumbnail", "thumbnails"]),
                "title": self.__getValue(inforenderer, ["title", "runs", 0, "text"]),
                "videoCount": self.__getValue(inforenderer, ["stats", 0, "runs", 0, "text"]),
                "viewCount": self.__getValue(inforenderer, ["stats", 1, "simpleText"]),
                "link": self.__getValue(self.responseSource, ["microformat", "microformatDataRenderer", "urlCanonical"]),
                "channel": {
                    "id": self.__getValue(channelrenderer, ["title", "runs", 0, "navigationEndpoint", "browseEndpoint", "browseId"]),
                    "name": self.__getValue(channelrenderer, ["title", "runs", 0, "text"]),
                    "link": "https://www.youtube.com" + self.__getValue(channelrenderer, ["title", "runs", 0, "navigationEndpoint", "browseEndpoint", "canonicalBaseUrl"]),
                    "thumbnails": self.__getValue(channelrenderer, ["thumbnail", "thumbnails"]),
                }
            },
            'videos': videos,
        }
        if self.componentMode == "getInfo":
            self.playlistComponent = playlistElement["info"]
        elif self.componentMode == "getVideos":
            self.playlistComponent = {"videos": videos}
        else:
            self.playlistComponent = playlistElement
        self.continuationKey = self.__getValue(videorenderer, [-1, "continuationItemRenderer", "continuationEndpoint", "continuationCommand", "token"])

    def __getNextComponents(self) -> None:
        self.continuationKey = None
        playlistComponent = {
            'videos': [],
        }
        continuationElements = self.__getValue(self.responseSource,
                                               ['onResponseReceivedActions', 0, 'appendContinuationItemsAction',
                                                'continuationItems'])
        for videoElement in continuationElements:
            if playlistVideoKey in videoElement.keys():
                videoComponent = {
                    'id': self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                    'title': self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                    'thumbnails': self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                    'link': "https://www.youtube.com" + self.__getValue(videoElement, [playlistVideoKey, "navigationEndpoint", "commandMetadata", "webCommandMetadata", "url"]),
                    'channel': {
                        'name': self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                        'id': self.__getValue(videoElement,
                                              [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint',
                                               'browseEndpoint', 'browseId']),
                        "link": "https://www.youtube.com" + self.__getValue(videoElement, [playlistVideoKey, "shortBylineText", "runs", 0, "navigationEndpoint", "browseEndpoint", "canonicalBaseUrl"])
                    },
                    'duration': self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                    'accessibility': {
                        'title': self.__getValue(videoElement,
                                                 [playlistVideoKey, 'title', 'accessibility', 'accessibilityData',
                                                  'label']),
                        'duration': self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility',
                                                                   'accessibilityData', 'label']),
                    },
                }
                playlistComponent['videos'].append(
                    videoComponent
                )
            self.continuationKey = self.__getValue(videoElement, continuationKeyPath)
        self.playlistComponent["videos"].extend(playlistComponent['videos'])

    def __getPlaylistComponent(self, element: dict, mode: str) -> dict:
        playlistComponent = {}
        if mode in ['getInfo', None]:
            for infoElement in element['info']:
                if playlistPrimaryInfoKey in infoElement.keys():
                    component = {
                        'id': self.__getValue(infoElement,
                                              [playlistPrimaryInfoKey, 'title', 'runs', 0, 'navigationEndpoint',
                                               'watchEndpoint', 'playlistId']),
                        'title': self.__getValue(infoElement, [playlistPrimaryInfoKey, 'title', 'runs', 0, 'text']),
                        'videoCount': self.__getValue(infoElement,
                                                      [playlistPrimaryInfoKey, 'stats', 0, 'runs', 0, 'text']),
                        'viewCount': self.__getValue(infoElement, [playlistPrimaryInfoKey, 'stats', 1, 'simpleText']),
                        'thumbnails': self.__getValue(infoElement, [playlistPrimaryInfoKey, 'thumbnailRenderer',
                                                                    'playlistVideoThumbnailRenderer', 'thumbnail']),
                    }
                    if not component['thumbnails']:
                        component['thumbnails'] = self.__getValue(infoElement,
                                                                  [playlistPrimaryInfoKey, 'thumbnailRenderer',
                                                                   'playlistCustomThumbnailRenderer', 'thumbnail',
                                                                   'thumbnails']),
                    component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
                    playlistComponent.update(component)
                if playlistSecondaryInfoKey in infoElement.keys():
                    component = {
                        'channel': {
                            'name': self.__getValue(infoElement,
                                                    [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer',
                                                     'title', 'runs', 0, 'text']),
                            'id': self.__getValue(infoElement,
                                                  [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer',
                                                   'title', 'runs', 0, 'navigationEndpoint', 'browseEndpoint',
                                                   'browseId']),
                            'thumbnails': self.__getValue(infoElement,
                                                          [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer',
                                                           'thumbnail', 'thumbnails']),
                        },
                    }
                    component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
                    playlistComponent.update(component)
        if mode in ['getVideos', None]:
            self.continuationKey = None
            playlistComponent['videos'] = []
            for videoElement in element['videos']:
                if playlistVideoKey in videoElement.keys():
                    videoComponent = {
                        'id': self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                        'title': self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                        'thumbnails': self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                        'channel': {
                            'name': self.__getValue(videoElement,
                                                    [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                            'id': self.__getValue(videoElement,
                                                  [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint',
                                                   'browseEndpoint', 'browseId']),
                        },
                        'duration': self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                        'accessibility': {
                            'title': self.__getValue(videoElement,
                                                     [playlistVideoKey, 'title', 'accessibility', 'accessibilityData',
                                                      'label']),
                            'duration': self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility',
                                                                       'accessibilityData', 'label']),
                        },
                    }
                    videoComponent['link'] = 'https://www.youtube.com/watch?v=' + videoComponent['id']
                    videoComponent['channel']['link'] = 'https://www.youtube.com/channel/' + videoComponent['channel'][
                        'id']
                    playlistComponent['videos'].append(
                        videoComponent
                    )
                if continuationItemKey in videoElement.keys():
                    self.continuationKey = self.__getValue(videoElement, continuationKeyPath)
        return playlistComponent

    def __result(self, mode: int) -> Union[dict, str]:
        if mode == ResultMode.dict:
            return self.playlistComponent
        elif mode == ResultMode.json:
            return json.dumps(self.playlistComponent, indent=4)

    def __getValue(self, source: dict, path: Iterable[str]) -> Union[str, int, dict, None]:
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

    def __getAllWithKey(self, source: Iterable[Mapping[K, T]], key: K) -> Iterable[T]:
        for item in source:
            if key in item:
                yield item[key]

    def __getValueEx(self, source: dict, path: List[str]) -> Iterable[Union[str, int, dict, None]]:
        if len(path) <= 0:
            yield source
            return
        key = path[0]
        upcoming = path[1:]
        if key is None:
            following_key = upcoming[0]
            upcoming = upcoming[1:]
            if following_key is None:
                raise Exception("Cannot search for a key twice consecutive or at the end with no key given")
            values = self.__getAllWithKey(source, following_key)
            for val in values:
                yield from self.__getValueEx(val, path=upcoming)
        else:
            val = self.__getValue(source, path=[key])
            yield from self.__getValueEx(val, path=upcoming)

    def __getFirstValue(self, source: dict, path: Iterable[str]) -> Union[str, int, dict, None]:
        values = self.__getValueEx(source, list(path))
        for val in values:
            if val is not None:
                return val
        return None
