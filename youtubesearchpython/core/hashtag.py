import copy
import json
from typing import Union
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import httpx

from youtubesearchpython.core.constants import *
from youtubesearchpython.handlers.componenthandler import ComponentHandler


class HashtagCore(ComponentHandler):
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

    def create_sync(self):
        self._getParams()
        self._makeRequest()

    async def create_async(self):
        await self._getAsyncParams()
        await self._makeAsyncRequest()

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

    def _next(self) -> bool:
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

    async def _nextAsync(self):
        self.response = None
        self.resultComponents = []
        if self.params is None:
            await self._getParamsAsync()
        self._makeRequest()
        self._getComponents()
        return {
            'result': self.resultComponents,
        }

    def _postParamsProcessing(self, response):
        content = self._getValue(json.loads(response), contentPath)
        for item in self._getValue(content, [0, 'itemSectionRenderer', 'contents']):
            if hashtagElementKey in item.keys():
                self.params = self._getValue(item[hashtagElementKey], ['onTapCommand', 'browseEndpoint', 'params'])
                return

    async def _getParamsAsync(self) -> None:
        requestBody = requestPayload
        requestBody['query'] = "#" + self.hashtag
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://www.youtube.com/youtubei/v1/search',
                    params={
                        'key': searchKey,
                    },
                    headers={
                        'User-Agent': userAgent,
                    },
                    json=requestBody,
                    timeout=self.timeout
                )
                response = response.json()
        except:
            raise Exception('ERROR: Could not make request.')
        content = self._getValue(response, contentPath)
        for item in self._getValue(content, [0, 'itemSectionRenderer', 'contents']):
            if hashtagElementKey in item.keys():
                self.params = self._getValue(item[hashtagElementKey],
                                                   ['onTapCommand', 'browseEndpoint', 'params'])
                return

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
        self._postParamsProcessing(response)

    async def _getAsyncParams(self) -> None:
        self._getParams()

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
            data=requestBodyBytes,
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Content-Length': len(requestBodyBytes),
                'User-Agent': userAgent,
            }
        )
        try:
            self.response = urlopen(request, timeout=self.timeout).read().decode('utf_8')
        except:
            raise Exception('ERROR: Could not make request.')

    async def _makeAsyncRequest(self) -> None:
        self._makeRequest()

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