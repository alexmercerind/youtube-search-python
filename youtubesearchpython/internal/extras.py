import json
import copy
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from typing import Union, List
from youtubesearchpython.internal.constants import *
from youtubesearchpython.handlers.componenthandler import ComponentHandler


class VideoInternal:
    def __init__(self, videoLink: str, componentMode: str, resultMode: int, timeout: int):
        self.timeout = timeout
        self.resultMode = resultMode
        statusCode = self.__makeRequest(self.__getVideoId(videoLink))
        if statusCode == 200:
            self.__extractFromHTML()
            self.__parseSource()
            self.__getVideoComponent(componentMode)
            self.result = self.__videoComponent
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
        request = Request(
            'https://www.youtube.com/watch' + '?' + urlencode({
                'v': videoId
            }),
            headers={
                'User-Agent': userAgent,
            },
            method="GET"
        )
        try:
            response = urlopen(request, timeout=self.timeout)
            self.response = response.read().decode('utf_8')
            return response.getcode()
        except:
            raise Exception('ERROR: Could not make request.')

    def __parseSource(self) -> None:
        #print(self.response.encode("utf-8"))
        try:
            self.responseSource = json.loads(self.response)
        except Exception as e:
            print(e)
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


class PlaylistInternal:
    playlistComponent = None
    result = None
    continuationKey = None

    def __init__(self, playlistLink: str, componentMode: str, resultMode: int, timeout: int):
        self.componentMode = componentMode
        self.resultMode = resultMode
        self.timeout = timeout
        statusCode = self.__makeRequest(playlistLink)
        if statusCode == 200:
            self.__extractFromHTML()
            self.__parseSource()
            self.__getComponents()
            if resultMode == ResultMode.json:
                self.result = json.dumps(self.playlistComponent, indent=4)
            else:
                self.result = self.playlistComponent
        else:
            raise Exception('ERROR: Invalid status code.')

    def next(self):
        if self.continuationKey:
            statusCode = self.__makeNextRequest()
            if statusCode == 200:
                self.__parseSource()
                self.__getNextComponents()
                if self.resultMode == ResultMode.json:
                    self.result = json.dumps(self.playlistComponent, indent=4)
                else:
                    self.result = self.playlistComponent
            else:
                raise Exception('ERROR: Invalid status code.')


    def __extractFromHTML(self):
        f1 = "var ytInitialData = "
        startpoint = self.response.find(f1)
        f2 = '"}}};</script>'
        endpoint = self.response.find(f2)
        if startpoint and endpoint:
            startpoint += len(f1)
            endpoint += len(f2)
            r = self.response[startpoint:endpoint]
            r = r.replace(";</script>", "")
            self.response = r
            print(startpoint)
            print(endpoint)

    def __makeRequest(self, playlistLink: str) -> int:
        playlistLink.strip('/')
        request = Request(
            playlistLink,
            data=urlencode({}).encode('utf_8'),
            headers={
                'User-Agent': userAgent,
            },
            method="GET"
        )
        try:
            response = urlopen(request, timeout=self.timeout)
            self.response = response.read().decode('utf_8')
            return response.getcode()
        except:
            raise Exception('ERROR: Could not make request.')

    def __makeNextRequest(self, requestBody=requestPayload) -> int:
        requestBody['continuation'] = self.continuationKey
        requestBodyBytes = json.dumps(requestBody).encode('utf_8')
        request = Request(
            'https://www.youtube.com/youtubei/v1/browse' + '?' + urlencode({
                'key': searchKey,
            }),
            data=requestBodyBytes,
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': len(requestBodyBytes),
                'User-Agent': userAgent,
            },
        )
        try:
            response = urlopen(request, timeout=self.timeout)
            self.response = response.read().decode('utf_8')
            return response.getcode()
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
        videorenderer = self.responseSource["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["playlistVideoListRenderer"]["contents"]
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


class Suggestions:
    '''Gets search suggestions for the given query.

    Args:
        language (str, optional): Sets the suggestion language. Defaults to 'en'.
        region (str, optional): Sets the suggestion region. Defaults to 'US'.
    
    Examples:
        Calling `result` method gives the search result.

        >>> suggestions = Suggestions(language = 'en', region = 'US').get('Harry Styles', mode = ResultMode.json)
        >>> print(suggestions)
        {
            'result': [
                'harry styles',
                'harry styles treat people with kindness',
                'harry styles golden music video',
                'harry styles interview',
                'harry styles adore you',
                'harry styles watermelon sugar',
                'harry styles snl',
                'harry styles falling',
                'harry styles tpwk',
                'harry styles sign of the times',
                'harry styles jingle ball 2020',
                'harry styles christmas',
                'harry styles live',
                'harry styles juice'
            ]
        }
    '''

    def __init__(self, language: str = 'en', region: str = 'US', timeout: int = None):
        self.language = language
        self.region = region
        self.timeout = timeout

    def get(self, query: str, mode: int = ResultMode.dict) -> Union[dict, str]:
        '''Fetches & returns the search suggestions for the given query.

        Args:
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Returns:
            Union[str, dict]: Returns JSON or dictionary.
        '''
        searchSuggestions = []
        self.__makeRequest(query)
        self.__parseSource()
        for element in self.responseSource:
            if type(element) is list:
                for searchSuggestionElement in element:
                    searchSuggestions.append(searchSuggestionElement[0])
                break
        if mode == ResultMode.dict:
            return {'result': searchSuggestions}
        elif mode == ResultMode.json:
            return json.dumps({'result': searchSuggestions}, indent=4)

    def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response[self.response.index('(') + 1: self.response.index(')')])
        except:
            raise Exception('ERROR: Could not parse YouTube response.')

    def __makeRequest(self, query: str) -> None:
        request = Request(
            'https://clients1.google.com/complete/search' + '?' + urlencode({
                'hl': self.language,
                'gl': self.region,
                'q': query,
                'client': 'youtube',
                'gs_ri': 'youtube',
                'ds': 'yt',
            }),
            headers={
                'User-Agent': userAgent,
            },
        )
        try:
            self.response = urlopen(request, timeout=self.timeout).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')


class HashtagInternal(ComponentHandler):
    response = None
    resultComponents = []

    def __init__(self, hashtag: str, limit: int, language: str, region: str, timeout: int):
        self.hashtag = hashtag
        self.limit = limit
        self.language = language
        self.region = region
        self.timeout = timeout
        self.continuationKey = None
        self.params = None
        self._getParams()
        self._makeRequest()

    def result(self, mode: int = ResultMode.dict) -> Union[str, dict]:
        '''Returns the hashtag videos.

        Args:
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Returns:
            Union[str, dict]: Returns JSON or dictionary.
        '''
        if mode == ResultMode.json:
            return json.dumps({'result': self.resultComponents}, indent = 4)
        elif mode == ResultMode.dict:
            return {'result': self.resultComponents}

    def next(self) -> bool:
        '''Gets the videos from the next page. Call result

        Returns:
            Union[str, dict]: Returns True if getting more results was successful.
        '''
        self.response = None
        self.resultComponents = []
        if self.continuationKey:
            self._makeRequest()
            self._getComponents()
        if self.resultComponents:
            return True
        return False

    def _getParams(self) -> None:
        requestBody = copy.deepcopy(requestPayload)
        requestBody['query'] = "#" + self.hashtag
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        requestBodyBytes = json.dumps(requestBody).encode('utf_8')
        request = Request(
            'https://www.youtube.com/youtubei/v1/search' + '?' + urlencode({
                'key': searchKey,
            }),
            data = requestBodyBytes,
            headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': len(requestBodyBytes),
                'User-Agent': userAgent,
            }
        )
        try:
            response = urlopen(request, timeout=self.timeout).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')
        content = self._getValue(json.loads(response), contentPath)
        for item in self._getValue(content, [0, 'itemSectionRenderer', 'contents']):
            if hashtagElementKey in item.keys():
                self.params = self._getValue(item[hashtagElementKey], ['onTapCommand', 'browseEndpoint', 'params'])
                return

    def _makeRequest(self) -> None:
        if self.params == None:
            return
        requestBody = copy.deepcopy(requestPayload)
        requestBody['browseId'] = hashtagBrowseKey
        requestBody['params'] = self.params
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        if self.continuationKey:
            requestBody['continuation'] = self.continuationKey
        requestBodyBytes = json.dumps(requestBody).encode('utf_8')
        request = Request(
            'https://www.youtube.com/youtubei/v1/browse' + '?' + urlencode({
                'key': searchKey,
            }),
            data = requestBodyBytes,
            headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': len(requestBodyBytes),
                'User-Agent': userAgent,
            }
        )
        try:
            self.response = urlopen(request, timeout=self.timeout).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')

    def _getComponents(self) -> None:
        if self.response == None:
            return
        self.resultComponents = []
        try:
            if not self.continuationKey:
                responseSource = self._getValue(json.loads(self.response), hashtagVideosPath)
            else:
                responseSource = self._getValue(json.loads(self.response), hashtagContinuationVideosPath)
            if responseSource:
                for element in responseSource:
                    if richItemKey in element.keys():
                        richItemElement = self._getValue(element, [richItemKey, 'content'])
                        if videoElementKey in richItemElement.keys():
                            videoComponent = self._getVideoComponent(richItemElement)
                            self.resultComponents.append(videoComponent)
                    if len(self.resultComponents) >= self.limit:
                        break
                self.continuationKey = self._getValue(responseSource[-1], continuationKeyPath)
        except:
            raise Exception('ERROR: Could not parse YouTube response.')
