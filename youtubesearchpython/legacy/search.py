from youtubesearchpython.base.constants import *
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.handlers.requesthandler import RequestHandler
from typing import List, Union
import json


def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


class LegacyComponentHandler(RequestHandler, ComponentHandler):
    index = 0

    @overrides(ComponentHandler)
    def getVideoComponent(self, element: dict, shelfTitle: str = None) -> dict:
        video = element[VIDEO_ELEMENT]
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
            'index':                           self.index,
            'id':                              videoId,
            'link':                            'https://www.youtube.com/watch?v=' + videoId,
            'title':                           self.__getValue(video, ['title', 'runs', 0, 'text']),
            'channel':                         self.__getValue(video, ['ownerText', 'runs', 0, 'text']),
            'duration':                        self.__getValue(video, ['lengthText', 'simpleText']),
            'views':                           viewCount,
            'thumbnails':                      thumbnails,
            'channeId':                        self.__getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']), 
            'publishTime':                     self.__getValue(video, ['publishedTimeText', 'simpleText']),
        }
        self.index += 1
        return component
    
    @overrides(ComponentHandler)
    def getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[PLAYLIST_ELEMENT]
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
    def getShelfComponent(self, element: dict) -> dict:
        shelf = element[SHELF_ELEMENT]
        return {
            'title':                           self.__getValue(shelf, ['title', 'simpleText']),
            'elements':                        self.__getValue(shelf, ['content', 'verticalListRenderer', 'items']),
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

class LegacyBaseSearch(LegacyComponentHandler):
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
    
    '''
    Returns
    -------
    None, str, dict, list
        Returns video results from YouTube. Returns None, if network error occurs.
    '''
    def result(self) -> Union[str, dict, list, None]:
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


class SearchVideos(LegacyBaseSearch):
    '''
    Search for videos in YouTube.
    Parameters
    ----------
    keyword : str
        Used as a query to search for videos in YouTube.
    offset : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    mode : str
        Search result mode. Can be 'json', 'dict' or 'list'.
    max_results : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
        Can be used to get results in particular language. Defaults to 'en-US'
    region: str, optional
        Can be used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the videos fetched from YouTube.
    '''
    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20, language = "en-US", region = "US"):
        super().__init__(keyword, offset = offset, mode = mode, max_results = max_results, language = language, region = region)
        self.searchPreferences = "EgIQAQ%3D%3D"
        self._RequestHandler__request()
        self._RequestHandler__makeSource()
        self.__makeComponents()

    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys():
                self.resultComponents.append(self.getVideoComponent(element))
            if SHELF_ELEMENT in element.keys():
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement))
            if len(self.resultComponents) >= self.limit:
                break

class SearchPlaylists(LegacyBaseSearch):
    '''
    Search for playlists in YouTube.
    Parameters
    ----------
    keyword : str
        Used as a query to search for playlists in YouTube.
    offset : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    mode : str
        Search result mode. Can be 'json', 'dict' or 'list'.
    max_results : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
        Can be used to get results in particular language. Defaults to 'en-US'
    region: str, optional
        Can be used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the videos fetched from YouTube.
    '''
    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20, language = "en-US", region = "US"):
        super().__init__(keyword, offset = offset, mode = mode, max_results = max_results, language = language, region = region)
        self.searchPreferences = "EgIQAw%3D%3D"
        self._RequestHandler__request()
        self._RequestHandler__makeSource()
        self.__makeComponents()

    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if PLAYLIST_ELEMENT in element.keys():
                self.resultComponents.append(self.getPlaylistComponent(element))
            if len(self.resultComponents) >= self.limit:
                break
