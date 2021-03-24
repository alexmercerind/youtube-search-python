import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from typing import Union, List
from youtubesearchpython.internal.constants import *


class VideoInternal:
    def __init__(self, videoLink: str, componentMode: str, resultMode: int):
        self.resultMode = resultMode
        statusCode = self.__makeRequest(self.__getVideoId(videoLink))
        if statusCode == 200:
            self.__parseSource()
            self.__getComponents(componentMode)
        else:
            raise Exception('ERROR: Invalid status code.')

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
                'v': videoId,
                'pbj': 1,
            }),
            headers = {
                'User-Agent': userAgent,
            },
            data = urlencode({}).encode('utf_8'),
        )
        try:
            response = urlopen(request)
            self.response = response.read().decode('utf_8')
            return response.getcode()
        except:
            raise Exception('ERROR: Could not make request.')
    
    def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response)
        except:
            raise Exception('ERROR: Could not parse YouTube response.')

    def __getComponents(self, mode: str = None) -> None:
        for element in self.responseSource:
            if playerResponseKey in element.keys():
                if 'videoDetails' in element[playerResponseKey].keys():
                    '''
                    Valid video ID.
                    '''
                    self.__videoComponent = self.__getVideoComponent(element[playerResponseKey], mode)
                    self.result = self.__result(self.resultMode)
                    break
                else:
                    '''
                    Invalid video ID.
                    '''
                    self.result = None

    def __result(self, mode: int) -> Union[dict, str]:
        if mode == ResultMode.dict:
            return self.__videoComponent
        elif mode == ResultMode.json:
            return json.dumps(self.__videoComponent, indent = 4)

    def __getVideoComponent(self, element: dict, mode: str) -> dict:
        videoComponent = {}
        if mode in ['getInfo', None]:
            component = {
                'id':                             self.__getValue(element, ['videoDetails', 'videoId']),
                'title':                          self.__getValue(element, ['videoDetails', 'title']),
                'viewCount': {
                    'text':                       self.__getValue(element, ['videoDetails', 'viewCount'])
                },
                'thumbnails':                     self.__getValue(element, ['videoDetails', 'thumbnail', 'thumbnails']),
                'description':                    self.__getValue(element, ['videoDetails', 'shortDescription']),
                'channel': {
                    'name':                       self.__getValue(element, ['videoDetails', 'author']),
                    'id':                         self.__getValue(element, ['videoDetails', 'channelId']),
                },
                'averageRating':                  self.__getValue(element, ['videoDetails', 'averageRating']),
                'keywords':                       self.__getValue(element, ['videoDetails', 'keywords']),
                'publishDate':                    self.__getValue(element, ['microformat', 'playerMicroformatRenderer', 'publishDate']),
                'uploadDate':                     self.__getValue(element, ['microformat', 'playerMicroformatRenderer', 'uploadDate']),
            }
            component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
            component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
            videoComponent.update(component)
        if mode in ['getFormats', None]:
            component = {
                'streamingData':                  self.__getValue(element, ['streamingData']),
            }
            videoComponent.update(component)
        return videoComponent

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

    def __init__(self, playlistLink: str, componentMode: str, resultMode: int):
        self.componentMode = componentMode
        self.resultMode = resultMode
        statusCode = self.__makeRequest(playlistLink)
        if statusCode == 200:
            self.__parseSource()
            self.__getComponents()
        else:
            raise Exception('ERROR: Invalid status code.')

    def next(self):
        if self.continuationKey:
            statusCode = self.__makeNextRequest()
            if statusCode == 200:
                self.__parseSource()
                self.__getNextComponents()
            else:
                raise Exception('ERROR: Invalid status code.')

    def __makeRequest(self, playlistLink: str) -> int:
        playlistLink.strip('/')
        request = Request(
            playlistLink + '&pbj=1',
            data = urlencode({}).encode('utf_8'),
            headers = {
                'User-Agent': userAgent,
            },
        )
        try:
            response = urlopen(request)
            self.response = response.read().decode('utf_8')
            return response.getcode()
        except:
            raise Exception('ERROR: Could not make request.')
    
    def __makeNextRequest(self, requestBody = requestPayload) -> int:
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
            },
        )
        try:
            response = urlopen(request)
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
        for response in self.responseSource:
            if 'response' in response.keys():
                playlistElement = {
                    'info':                               self.__getValue(response, playlistInfoPath),
                    'videos':                             self.__getValue(response, playlistVideosPath),
                }
                if not playlistElement['info']:
                    raise Exception('ERROR: Could not parse YouTube response.')
                self.playlistComponent = self.__getPlaylistComponent(playlistElement, self.componentMode)
                self.result = self.__result(self.resultMode)

    def __getNextComponents(self) -> None:
        self.continuationKey = None
        playlistComponent = {
            'videos': [],
        }
        continuationElements = self.__getValue(self.responseSource, ['onResponseReceivedActions', 0, 'appendContinuationItemsAction', 'continuationItems'])
        for videoElement in continuationElements:
            if playlistVideoKey in videoElement.keys():
                videoComponent = {
                    'id':                             self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                    'title':                          self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                    'thumbnails':                     self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                    'channel': {
                        'name':                       self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                        'id':                         self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                    },
                    'duration':                       self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                    'accessibility': {
                        'title':                      self.__getValue(videoElement, [playlistVideoKey, 'title', 'accessibility', 'accessibilityData', 'label']),
                        'duration':                   self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility', 'accessibilityData', 'label']),
                    },
                }
                playlistComponent['videos'].append(
                    videoComponent
                )
            if continuationItemKey in videoElement.keys():
                self.continuationKey = self.__getValue(videoElement, continuationKeyPath)
        self.playlistComponent['videos'].extend(playlistComponent['videos'])
                
    def __getPlaylistComponent(self, element: dict, mode: str) -> dict:
        playlistComponent = {}
        if mode in ['getInfo', None]:
            for infoElement in element['info']:
                if playlistPrimaryInfoKey in infoElement.keys():
                    component = {
                        'id':                             self.__getValue(infoElement, [playlistPrimaryInfoKey, 'title', 'runs', 0, 'navigationEndpoint', 'watchEndpoint', 'playlistId']),
                        'title':                          self.__getValue(infoElement, [playlistPrimaryInfoKey, 'title', 'runs', 0, 'text']),
                        'videoCount':                     self.__getValue(infoElement, [playlistPrimaryInfoKey, 'stats', 0, 'runs', 0, 'text']),
                        'viewCount':                      self.__getValue(infoElement, [playlistPrimaryInfoKey, 'stats', 1, 'simpleText']),
                        'thumbnails':                     self.__getValue(infoElement, [playlistPrimaryInfoKey, 'thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail']),
                    }
                    if not component['thumbnails']:
                        component['thumbnails'] =         self.__getValue(infoElement, [playlistPrimaryInfoKey, 'thumbnailRenderer', 'playlistCustomThumbnailRenderer', 'thumbnail', 'thumbnails']),
                    component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
                    playlistComponent.update(component)
                if playlistSecondaryInfoKey in infoElement.keys():
                    component = {
                        'channel': {
                            'name':                       self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text']),
                            'id':                         self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'title', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                            'thumbnails':                 self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails']),
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
                        'id':                             self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                        'title':                          self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                        'thumbnails':                     self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                        'channel': {
                            'name':                       self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                            'id':                         self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                        },
                        'duration':                       self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                        'accessibility': {
                            'title':                      self.__getValue(videoElement, [playlistVideoKey, 'title', 'accessibility', 'accessibilityData', 'label']),
                            'duration':                   self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility', 'accessibilityData', 'label']),
                        },
                    }
                    videoComponent['link'] = 'https://www.youtube.com/watch?v=' + videoComponent['id']
                    videoComponent['channel']['link'] = 'https://www.youtube.com/channel/' + videoComponent['channel']['id']
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
            return json.dumps(self.playlistComponent, indent = 4)

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
    def __init__(self, language: str = 'en', region: str = 'US'):
        self.language = language
        self.region = region

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
            return json.dumps({'result': searchSuggestions}, indent = 4)
        
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
            headers = {
                'User-Agent': userAgent,
            },
        )
        try:
            self.response = urlopen(request).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')
