from typing import List, Union
import json
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.handlers.requesthandler import RequestHandler
from youtubesearchpython.core.constants import *


def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


class LegacyComponentHandler(RequestHandler, ComponentHandler):
    index = 0

    @overrides(ComponentHandler)
    def _getVideoComponent(self, element: dict, shelfTitle: str = None) -> dict:
        video = element[videoElementKey]
        videoId = self.__getValue(video, ['videoId'])
        viewCount = 0
        thumbnails = []
        for character in self.__getValue(video, ['viewCountText', 'simpleText']):
            if character.isnumeric():
                viewCount = viewCount * 10 + int(character)
        modes = ['default', 'hqdefault', 'mqdefault', 'sddefault', 'maxresdefault']
        for mode in modes:
            thumbnails.append('https://img.youtube.com/vi/' + videoId + '/' + mode + '.jpg')
        component = {
            'index':                          self.index,
            'id':                             videoId,
            'link':                           'https://www.youtube.com/watch?v=' + videoId,
            'title':                          self.__getValue(video, ['title', 'runs', 0, 'text']),
            'channel':                        self.__getValue(video, ['ownerText', 'runs', 0, 'text']),
            'duration':                       self.__getValue(video, ['lengthText', 'simpleText']),
            'views':                          viewCount,
            'thumbnails':                     thumbnails,
            'channeId':                       self.__getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']), 
            'publishTime':                    self.__getValue(video, ['publishedTimeText', 'simpleText']),
        }
        self.index += 1
        return component
    
    @overrides(ComponentHandler)
    def _getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[playlistElementKey]
        playlistId = self.__getValue(playlist, ['playlistId'])
        thumbnailVideoId = self.__getValue(playlist, ['navigationEndpoint', 'watchEndpoint', 'videoId'])
        thumbnails = []
        modes = ['default', 'hqdefault', 'mqdefault', 'sddefault', 'maxresdefault']
        for mode in modes:
            thumbnails.append('https://img.youtube.com/vi/' + thumbnailVideoId + '/' + mode + '.jpg')
        component = {
            'index':                          self.index,
            'id':                             playlistId,
            'link':                           'https://www.youtube.com/playlist?list=' + playlistId,
            'title':                          self.__getValue(playlist, ['title', 'simpleText']),
            'thumbnails':                     thumbnails,
            'count':                          self.__getValue(playlist, ['videoCount']),
            'channel':                        self.__getValue(playlist, ['shortBylineText', 'runs', 0, 'text']),
        }
        self.index += 1
        return component

    @overrides(ComponentHandler)
    def _getShelfComponent(self, element: dict) -> dict:
        shelf = element[shelfElementKey]
        return {
            'title':                          self.__getValue(shelf, ['title', 'simpleText']),
            'elements':                       self.__getValue(shelf, ['content', 'verticalListRenderer', 'items']),
        }

    def __getValue(self, component: dict, path: List[str]) -> Union[str, int, dict]:
        value = component
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = 'LIVE'
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = 'LIVE'
                    break
        return value

class LegacySearchInternal(LegacyComponentHandler):
    exception = False
    resultComponents = []
    responseSource = []

    def __init__(self, keyword, offset, mode, max_results, language, region):
        self.page = offset
        self.query = keyword
        self.mode = mode
        self.limit = max_results
        self.language = language
        self.region = region
        self.continuationKey = None
        self.timeout = None
    
    def result(self) -> Union[str, dict, list, None]:
        '''Returns the search result.

        Returns:
            Union[str, dict, list, None]: Returns JSON, list or dictionary & None in case of any exception.
        '''
        if self.exception or len(self.resultComponents) == 0:
            return None
        else:
            if self.mode == 'dict':
                return {'search_result': self.resultComponents}
            elif self.mode == 'json':
                return json.dumps({'search_result': self.resultComponents}, indent = 4)
            elif self.mode == 'list':
                result = []
                for component in self.resultComponents:
                    listComponent = []
                    for key in component.keys():
                        listComponent.append(component[key])
                    result.append(listComponent)
                return result


class SearchVideos(LegacySearchInternal):
    '''
    DEPRECATED
    ----------
    Use `VideosSearch` instead.
    
    Searches for playlists in YouTube.

    Args:
        keyword (str): Sets the search query.
        offset (int, optional): Sets the search result page number. Defaults to 1.
        mode (str, optional): Sets the result type, can be 'json', 'dict' or 'list'. Defaults to 'json'. 
        max_results (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en-US'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = SearchPlaylists('Harry Styles', max_results = 1)
        >>> print(search.result())
        {
            "search_result": [
                {
                    "index": 0,
                    "id": "PLj-vAPBrjcxoBfEk3q2Jp-naXRFpekySW",
                    "link": "https://www.youtube.com/playlist?list=PLj-vAPBrjcxoBfEk3q2Jp-naXRFpekySW",
                    "title": "Harry Styles - Harry Styles Full Album videos with lyrics",
                    "thumbnails": [
                        "https://img.youtube.com/vi/Y9yOG_dJwFg/default.jpg",
                        "https://img.youtube.com/vi/Y9yOG_dJwFg/hqdefault.jpg",
                        "https://img.youtube.com/vi/Y9yOG_dJwFg/mqdefault.jpg",
                        "https://img.youtube.com/vi/Y9yOG_dJwFg/sddefault.jpg",
                        "https://img.youtube.com/vi/Y9yOG_dJwFg/maxresdefault.jpg"
                    ],
                    "count": "10",
                    "channel": "Jana Hol\u00fabkov\u00e1"
                }
            ]
        }
    '''
    def __init__(self, keyword, offset = 1, mode = 'json', max_results = 20, language = 'en', region = 'US'):
        super().__init__(keyword, offset, mode, max_results, language, region)
        self.searchPreferences = 'EgIQAQ%3D%3D'
        self._makeRequest()
        self._parseSource()
        self.__makeComponents()

    def __makeComponents(self) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if videoElementKey in element.keys():
                self.resultComponents.append(self._getVideoComponent(element))
            if shelfElementKey in element.keys():
                for shelfElement in self._getShelfComponent(element)['elements']:
                    self.resultComponents.append(self._getVideoComponent(shelfElement))
            if len(self.resultComponents) >= self.limit:
                break

class SearchPlaylists(LegacySearchInternal):
    '''
    DEPRECATED
    ----------
    Use `PlaylistsSearch` instead.

    Searches for playlists in YouTube.

    Args:
        keyword (str): Sets the search query.
        offset (int, optional): Sets the search result page number. Defaults to 1.
        mode (str, optional): Sets the result type, can be 'json', 'dict' or 'list'. Defaults to 'json'. 
        max_results (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en-US'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = SearchVideos('Watermelon Sugar', max_results = 1)
        >>> print(search.result())
        {
            "search_result": [
                {
                    "index": 0,
                    "id": "E07s5ZYygMg",
                    "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
                    "title": "Harry Styles - Watermelon Sugar (Official Video)",
                    "channel": "Harry Styles",
                    "duration": "3:09",
                    "views": 162235006,
                    "thumbnails": [
                        "https://img.youtube.com/vi/E07s5ZYygMg/default.jpg",
                        "https://img.youtube.com/vi/E07s5ZYygMg/hqdefault.jpg",
                        "https://img.youtube.com/vi/E07s5ZYygMg/mqdefault.jpg",
                        "https://img.youtube.com/vi/E07s5ZYygMg/sddefault.jpg",
                        "https://img.youtube.com/vi/E07s5ZYygMg/maxresdefault.jpg"
                    ],
                    "channeId": "UCZFWPqqPkFlNwIxcpsLOwew",
                    "publishTime": "6 months ago"
                }
            ]
        }
    '''
    def __init__(self, keyword, offset = 1, mode = 'json', max_results = 20, language = 'en', region = 'US'):
        super().__init__(keyword, offset, mode, max_results, language, region)
        self.searchPreferences = 'EgIQAw%3D%3D'
        self._makeRequest()
        self._parseSource()
        self.__makeComponents()

    def __makeComponents(self) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if playlistElementKey in element.keys():
                self.resultComponents.append(self._getPlaylistComponent(element))
            if len(self.resultComponents) >= self.limit:
                break
