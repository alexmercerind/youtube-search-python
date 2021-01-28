from typing import Union, List
import json
import httpx
from youtubesearchpython.__future__.internal.constants import *


class VideoInternal:
    videoId = None
    videoComponent = None

    def __init__(self, videoLink: str, componentMode: str):
        self.videoLink = videoLink
        self.componentMode = componentMode
    
    async def get(self):
        self.videoId = await self.__getVideoId(self.videoLink)
        await self.__makeRequest()
        await self.__getComponents(self.componentMode)
        if not self.videoComponent:
            raise Exception('ERROR: Could not parse YouTube response.')

    async def __getVideoId(self, videoLink: str) -> str:
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

    async def __makeRequest(self) -> None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://www.youtube.com/watch',
                    params = {
                        'v': self.videoId,
                        'pbj': 1,
                    },
                )
                self.responseSource = response.json()
        except:
            raise Exception('ERROR: Could not make request.')

    async def __getComponents(self, mode: str) -> None:
        for element in self.responseSource:
            if playerResponseKey in element.keys():
                if 'videoDetails' in element[playerResponseKey].keys():
                    '''
                    Valid video ID.
                    '''
                    self.videoComponent = await self.__getVideoComponent(element[playerResponseKey], mode)
                    break
                else:
                    '''
                    Invalid video ID.
                    '''
                    self.videoComponent = None

    async def __getVideoComponent(self, element: dict, mode: str) -> dict:
        videoComponent = {}
        if mode in ['getInfo', None]:
            component = {
                'id':                             await self.__getValue(element, ['videoDetails', 'videoId']),
                'title':                          await self.__getValue(element, ['videoDetails', 'title']),
                'viewCount': {
                    'text':                       await self.__getValue(element, ['videoDetails', 'viewCount'])
                },
                'thumbnails':                     await self.__getValue(element, ['videoDetails', 'thumbnail', 'thumbnails']),
                'description':                    await self.__getValue(element, ['videoDetails', 'shortDescription']),
                'channel': {
                    'name':                       await self.__getValue(element, ['videoDetails', 'author']),
                    'id':                         await self.__getValue(element, ['videoDetails', 'channelId']),
                },
                'averageRating':                  await self.__getValue(element, ['videoDetails', 'averageRating']),
                'keywords':                       await self.__getValue(element, ['videoDetails', 'keywords']),
                'publishDate':                    await self.__getValue(element, ['microformat', 'playerMicroformatRenderer', 'publishDate']),
                'uploadDate':                     await self.__getValue(element, ['microformat', 'playerMicroformatRenderer', 'uploadDate']),
            }
            component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
            component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
            videoComponent.update(component)
        if mode in ['getFormats', None]:
            component = {
                'streamingData':                  await self.__getValue(element, ['streamingData']),
            }
            videoComponent.update(component)
        return videoComponent

    async def __getValue(self, source: dict, path: List[str]) -> Union[str, int, dict, None]:
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


class SuggestionsInternal:
    searchSuggestions = []
    
    def __init__(self):
        pass
    
    async def get(self, query: str, language: str = 'en', region: str = 'US') -> dict:
        self.query = query
        self.language = language
        self.region = region
        await self.__makeRequest()
        await self.__parseSource()
        for element in self.responseSource:
            if type(element) is list:
                for searchSuggestionElement in element:
                    self.searchSuggestions.append(searchSuggestionElement[0])
                break
        return {
            'result': self.searchSuggestions,
        }
        
    async def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response[self.response.index('(') + 1: self.response.index(')')])
        except:
            raise Exception('ERROR: Could not parse YouTube response.')

    async def __makeRequest(self) -> None:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    'https://clients1.google.com/complete/search',
                    params = {
                        'hl': self.language,
                        'gl': self.region,
                        'q': self.query,
                        'client': 'youtube',
                        'gs_ri': 'youtube',
                        'ds': 'yt',
                    },
                )
                self.response = response.text
        except:
            raise Exception('ERROR: Could not make request.')
