import copy
from typing import Union
import json
from urllib.parse import urlencode

from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.core.constants import *


class ChannelRequestCore(RequestCore, ComponentHandler):
    def __init__(self, query: str, language: str, region: str, searchPreferences: str, browseId: str, timeout: int):
        super().__init__()
        self.query = query
        self.language = language
        self.region = region
        self.browseId = browseId
        self.searchPreferences = searchPreferences
        self.continuationKey = None
        self.timeout = timeout
        self.response = None
        self.responseSource = None
        self.resultComponents = []

    def sync_create(self):
        self._syncRequest()
        self._parseChannelSearchSource()
        self.response = self._getChannelSearchComponent(self.response)

    async def next(self):
        await self._asyncRequest()
        self._parseChannelSearchSource()
        self.response = self._getChannelSearchComponent(self.response)
        return self.response

    def _parseChannelSearchSource(self) -> None:
        raise NotImplementedError('ABC')

    def _getRequestBody(self):
        ''' Fixes #47 '''
        requestBody = copy.deepcopy(requestPayload)
        requestBody['query'] = self.query
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        requestBody['params'] = self.searchPreferences
        requestBody['browseId'] = self.browseId
        self.url = 'https://www.youtube.com/youtubei/v1/browse' + '?' + urlencode({
            'key': searchKey,
        })
        self.data = requestBody

    def _syncRequest(self) -> None:
        ''' Fixes #47 '''
        self._getRequestBody()

        request = self.syncPostRequest()
        try:
            self.response = request.json()
        except:
            raise Exception('ERROR: Could not make request.')

    async def _asyncRequest(self) -> None:
        ''' Fixes #47 '''
        self._getRequestBody()

        request = await self.asyncPostRequest()
        try:
            self.response = request.json()
        except:
            raise Exception('ERROR: Could not make request.')

    def result(self, mode: int = ResultMode.dict) -> Union[str, dict]:
        '''Returns the search result.

        Args:
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Returns:
            Union[str, dict]: Returns JSON or dictionary.
        '''
        if mode == ResultMode.json:
            return json.dumps({'result': self.response}, indent=4)
        elif mode == ResultMode.dict:
            return {'result': self.response}


class ChannelSearchCore(ChannelRequestCore):
    def __init__(self, query: str, language: str, region: str, searchPreferences: str, browseId: str, timeout: int):
        super().__init__(query, language, region, searchPreferences, browseId, timeout)

    def _parseChannelSearchSource(self) -> None:
        try:
            last_tab = self.response["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][-1]
            if 'expandableTabRenderer' in last_tab:
                self.response = last_tab["expandableTabRenderer"]["content"]["sectionListRenderer"]["contents"]
            else:
                tab_renderer = last_tab["tabRenderer"]
                if 'content' in tab_renderer:
                    self.response = tab_renderer["content"]["sectionListRenderer"]["contents"]
                else:
                    self.response = []
        except:
            raise Exception('ERROR: Could not parse YouTube response.')


class ChannelPlaylistSearchCore(ChannelRequestCore):
    def __init__(self, query: str, language: str, region: str, searchPreferences: str, browseId: str, timeout: int):
        super().__init__(query, language, region, searchPreferences, browseId, timeout)

    def _parseChannelSearchSource(self) -> None:
        try:
            playlist_tab = None
            for tab in self.response["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]:
                tab_renderer = tab["tabRenderer"]
                if tab_renderer['title'] == 'Playlists':
                    playlist_tab = tab_renderer
                    break
            if playlist_tab is None:
                raise Exception('Playlist tab is not present in youtube response')
            if 'content' in tab_renderer:
                self.response = tab_renderer["content"]["sectionListRenderer"]["contents"]
            else:
                self.response = []
            response = []
            for item_section_renderer in self.response:
                searchPreferences = item_section_renderer['itemSectionRenderer']['contents'][0]['shelfRenderer']['title']['runs'][0]['navigationEndpoint']['browseEndpoint']['params']
                playlist_search = SingleChannelPlaylistSearch(self.query, self.language, self.region, searchPreferences, self.browseId, self.timeout)
                playlist_search.sync_create()
                response.append(playlist_search.result()['result'])
            self.response = response
        except:
            raise Exception('ERROR: Could not parse YouTube response.')
    
    def _getChannelSearchComponent(self, elements: list) -> list:
        return elements

class SingleChannelPlaylistSearch(ChannelRequestCore):
    def __init__(self, query: str, language: str, region: str, searchPreferences: str, browseId: str, timeout: int):
        super().__init__(query, language, region, searchPreferences, browseId, timeout)

    def _parseChannelSearchSource(self) -> None:
        try:
            playlist_tab = None
            for tab in self.response["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]:
                tab_renderer = tab["tabRenderer"]
                if tab_renderer['title'] == 'Playlists':
                    playlist_tab = tab_renderer
                    break
            if playlist_tab is None:
                raise Exception('Playlist tab is not present in youtube response')
            if 'content' in tab_renderer:
                self.response = tab_renderer["content"]["sectionListRenderer"]["contents"]
            else:
                self.response = []
            for item_section_renderer in self.response:
                self.response = item_section_renderer['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
        except:
            raise Exception('ERROR: Could not parse YouTube response.')
