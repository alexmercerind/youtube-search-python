from youtubesearchpython.base.constants import *
from youtubesearchpython.handlers.requesthandler import RequestHandler
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from typing import Union
import json


class BaseSearch(RequestHandler, ComponentHandler):
    exception = False
    resultComponents = []
    responseSource = []

    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US', searchPreferences: str = None):
        self.page = page
        self.query = query
        self.limit = limit
        self.language = language
        self.region = region
        self.searchPreferences = searchPreferences
        self._RequestHandler__request()
        self._RequestHandler__makeSource()
    
    def result(self, mode: int = ResultMode.json) -> Union[str, dict, None]:
        '''Returns the search result.

        Args:
            mode (int, optional): Sets the type of result. Defaults to ResultMode.json.

        Returns:
            Union[str, dict, None]: Returns JSON or dictionary & None in case of any exception.
        '''
        if self.exception or len(self.resultComponents) == 0:
            return None
        else:
            if mode == ResultMode.json:
                return json.dumps({'result': self.resultComponents}, indent = 4)
            elif mode == ResultMode.dict:
                return {'result': self.resultComponents}

    def __makeComponents(self, findVideos: bool, findChannels: bool, findPlaylists: bool) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys() and findVideos:
                self.resultComponents.append(self.getVideoComponent(element))
            if CHANNEL_ELEMENT in element.keys() and findChannels:
                self.resultComponents.append(self.getChannelComponent(element))
            if PLAYLIST_ELEMENT in element.keys() and findPlaylists:
                self.resultComponents.append(self.getPlaylistComponent(element))
            if SHELF_ELEMENT in element.keys() and findVideos:
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))
            if len(self.resultComponents) >= self.limit:
                break
