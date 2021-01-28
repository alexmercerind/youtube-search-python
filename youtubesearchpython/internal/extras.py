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
            })
        )
        try:
            self.response = urlopen(request).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')
