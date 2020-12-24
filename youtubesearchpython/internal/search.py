from typing import Union
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json
from youtubesearchpython.handlers.requesthandler import RequestHandler
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.internal.constants import *


class SearchInternal(RequestHandler, ComponentHandler):
    response = None
    responseSource = None
    resultComponents = []

    def __init__(self, query: str, limit: int, language: str, region: str, searchPreferences: str):
        self.query = query
        self.limit = limit
        self.language = language
        self.region = region
        self.searchPreferences = searchPreferences
        self.continuationKey = None
        self._RequestHandler__makeRequest()
        self._RequestHandler__parseSource()
    
    def result(self, mode: int = ResultMode.dict) -> Union[str, dict]:
        '''Returns the search result.

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
        '''Gets the subsequent search result. Call result

        Args:
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Returns:
            Union[str, dict]: Returns True if getting more results was successful.
        '''
        if self.continuationKey:
            self.response = None
            self.responseSource = None
            self.resultComponents = []
            self._RequestHandler__makeRequest()
            self._RequestHandler__parseSource()
            self._SearchInternal__getComponents(*self.searchMode)
            return True
        else:
            return False

    def __getComponents(self, findVideos: bool, findChannels: bool, findPlaylists: bool) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if videoElementKey in element.keys() and findVideos:
                self.resultComponents.append(self.getVideoComponent(element))
            if channelElementKey in element.keys() and findChannels:
                self.resultComponents.append(self.getChannelComponent(element))
            if playlistElementKey in element.keys() and findPlaylists:
                self.resultComponents.append(self.getPlaylistComponent(element))
            if shelfElementKey in element.keys() and findVideos:
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))
            if len(self.resultComponents) >= self.limit:
                break

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
            "result": [
                "harry styles",
                "harry styles treat people with kindness",
                "harry styles golden music video",
                "harry styles interview",
                "harry styles adore you",
                "harry styles watermelon sugar",
                "harry styles snl",
                "harry styles falling",
                "harry styles tpwk",
                "harry styles sign of the times",
                "harry styles jingle ball 2020",
                "harry styles christmas",
                "harry styles live",
                "harry styles juice"
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

    def __makeRequest(self, query: str) -> str:
        request = Request(
            'https://clients1.google.com/complete/search' + '?' + urlencode({
                'hl': self.language,
                'gl': self.region,
                'q': query,
                'client': 'youtube',
                'gs_ri': 'youtube',
                'ds': 'yt',
            })
        )
        try:
            self.response = urlopen(request).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')
