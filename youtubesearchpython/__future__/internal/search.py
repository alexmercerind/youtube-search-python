from typing import Union
from youtubesearchpython.__future__.handlers.requesthandler import RequestHandler
from youtubesearchpython.__future__.handlers.componenthandler import ComponentHandler
from youtubesearchpython.__future__.internal.constants import *


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

    async def next(self) -> dict:
        '''Searches & returns the search result on the next page.

        Returns:
            dict: Returns dictionary containing the search result.
        '''
        self.response = None
        self.responseSource = None
        self.resultComponents = []
        await self._makeRequest()
        await self._parseSource()
        await self._getComponents(*self.searchMode)
        return {
            'result': self.resultComponents,
        }

    async def _getComponents(self, findVideos: bool, findChannels: bool, findPlaylists: bool) -> None:
        self.resultComponents = []
        for element in self.responseSource:
            if videoElementKey in element.keys() and findVideos:
                videoComponent = await self._getVideoComponent(element)
                self.resultComponents.append(videoComponent)
            if channelElementKey in element.keys() and findChannels:
                channelComponent = await self._getChannelComponent(element)
                self.resultComponents.append(channelComponent)
            if playlistElementKey in element.keys() and findPlaylists:
                playlistComponent = await self._getPlaylistComponent(element)
                self.resultComponents.append(playlistComponent)
            if shelfElementKey in element.keys() and findVideos:
                shelfComponent = await self._getShelfComponent(element)
                for shelfElement in shelfComponent['elements']:
                    videoComponent = await self._getVideoComponent(
                        shelfElement,
                        shelfTitle = shelfComponent['title']
                    )
                    self.resultComponents.append(videoComponent)
            if richItemKey in element.keys() and findVideos:
                richItemElement = await self._getValue(element, [richItemKey, 'content'])
                ''' Initial fallback handling for VideosSearch '''
                if videoElementKey in richItemElement.keys():
                    videoComponent = await self._getVideoComponent(richItemElement)
                    self.resultComponents.append(videoComponent)
            if len(self.resultComponents) >= self.limit:
                break
