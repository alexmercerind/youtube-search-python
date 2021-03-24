import httpx
from youtubesearchpython.__future__.handlers.componenthandler import ComponentHandler
from youtubesearchpython.__future__.internal.constants import *


class RequestHandler(ComponentHandler):
    async def _makeRequest(self, requestBody = requestPayload) -> None:
        requestBody['query'] = self.query
        requestBody['client'] = {
            'hl': self.language,
            'gl': self.region,
        }
        if self.searchPreferences:
            requestBody['params'] = self.searchPreferences
        if self.continuationKey:
            requestBody['continuation'] = self.continuationKey
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://www.youtube.com/youtubei/v1/search',
                    params = {
                        'key': searchKey,
                    },
                    headers = {
                        'User-Agent': userAgent,
                    },
                    json = requestBody,
                )
                self.response = response.json()
        except:
            raise Exception('ERROR: Could not make request.')
    
    async def _parseSource(self) -> None:
        try:
            if not self.continuationKey:
                responseContent = await self._getValue(self.response, contentPath)
            else:
                responseContent = await self._getValue(self.response, continuationContentPath)
            if responseContent:
                for element in responseContent:
                    if itemSectionKey in element.keys():
                        self.responseSource = await self._getValue(element, [itemSectionKey, 'contents'])
                    if continuationItemKey in element.keys():
                        self.continuationKey = await self._getValue(element, continuationKeyPath)
            else:
                self.responseSource = await self._getValue(self.response, fallbackContentPath)
                self.continuationKey = await self._getValue(self.responseSource[-1], continuationKeyPath)
        except:
            raise Exception('ERROR: Could not parse YouTube response.')
