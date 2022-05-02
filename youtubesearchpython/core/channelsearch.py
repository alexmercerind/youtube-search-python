import copy
from typing import Union
import json
from urllib.parse import urlencode

from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.core.constants import *


class ChannelSearchCore(RequestCore, ComponentHandler):
    response = None
    responseSource = None
    resultComponents = []

    def __init__(self, query: str, language: str, region: str, searchPreferences: str, browseId: str, timeout: int):
        super().__init__()
        self.query = query
        self.language = language
        self.region = region
        self.browseId = browseId
        self.searchPreferences = searchPreferences
        self.continuationKey = None
        self.timeout = timeout

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

