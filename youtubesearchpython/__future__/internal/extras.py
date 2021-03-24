from typing import Union, List
from youtubesearchpython.__future__.internal.json import loads
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
                    headers = {
                        'User-Agent': userAgent,
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
                'id':                             await self.__getValue(element, ['videoDetails', 'videoId']),
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


class PlaylistInternal:
    playlistComponent = None
    result = None
    continuationKey = None

    def __init__(self, playlistLink: str, componentMode: str):
        self.playlistLink = playlistLink
        self.componentMode = componentMode
    
    async def get(self):
        await self.__makeRequest(self.playlistLink)
        await self.__getComponents()

    async def next(self):
        if self.continuationKey:
            await self.__makeNextRequest()
            await self.__getNextComponents()

    async def __makeRequest(self, playlistLink: str) -> None:
        playlistLink.strip('/')
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    playlistLink,
                    params = {
                        'pbj': '1',
                    },
                    headers = {
                        'User-Agent': userAgent,
                    },
                )
                self.responseSource = response.json()
        except:
            raise Exception('ERROR: Could not make request.')
    
    async def __makeNextRequest(self, requestBody = requestPayload) -> None:
        requestBody['continuation'] = self.continuationKey
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    'https://www.youtube.com/youtubei/v1/browse',
                    params = {
                        'key': searchKey,
                    },
                    headers = {
                        'User-Agent': userAgent,
                    },
                    json = requestBody,
                )
                self.responseSource = response.json()
        except:
            raise Exception('ERROR: Could not make request.')

    async def __getComponents(self) -> None:
        for response in self.responseSource:
            if 'response' in response.keys():
                playlistElement = {
                    'info':                               await self.__getValue(response, playlistInfoPath),
                    'videos':                             await self.__getValue(response, playlistVideosPath),
                }
                if not playlistElement['info']:
                    raise Exception('ERROR: Could not parse YouTube response.')
                self.playlistComponent = await self.__getPlaylistComponent(playlistElement, self.componentMode)

    async def __getNextComponents(self) -> None:
        self.continuationKey = None
        playlistComponent = {
            'videos': [],
        }
        continuationElements = await self.__getValue(self.responseSource, ['onResponseReceivedActions', 0, 'appendContinuationItemsAction', 'continuationItems'])
        for videoElement in continuationElements:
            if playlistVideoKey in videoElement.keys():
                videoComponent = {
                    'id':                                await self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                    'title':                             await self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                    'thumbnails':                        await self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                    'channel': {
                        'name':                          await self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                        'id':                            await self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                    },
                    'duration':                          await self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                    'accessibility': {
                        'title':                         await self.__getValue(videoElement, [playlistVideoKey, 'title', 'accessibility', 'accessibilityData', 'label']),
                        'duration':                      await self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility', 'accessibilityData', 'label']),
                    },
                }
                playlistComponent['videos'].append(
                    videoComponent
                )
            if continuationItemKey in videoElement.keys():
                self.continuationKey = await self.__getValue(videoElement, continuationKeyPath)
        self.playlistComponent['videos'].extend(playlistComponent['videos'])
                
    async def __getPlaylistComponent(self, element: dict, mode: str) -> dict:
        playlistComponent = {}
        if mode in ['getInfo', None]:
            for infoElement in element['info']:
                if playlistPrimaryInfoKey in infoElement.keys():
                    component = {
                        'id':                             await self.__getValue(infoElement, [playlistPrimaryInfoKey, 'title', 'runs', 0, 'navigationEndpoint', 'watchEndpoint', 'playlistId']),
                        'title':                          await self.__getValue(infoElement, [playlistPrimaryInfoKey, 'title', 'runs', 0, 'text']),
                        'videoCount':                     await self.__getValue(infoElement, [playlistPrimaryInfoKey, 'stats', 0, 'runs', 0, 'text']),
                        'viewCount':                      await self.__getValue(infoElement, [playlistPrimaryInfoKey, 'stats', 1, 'simpleText']),
                        'thumbnails':                     await self.__getValue(infoElement, [playlistPrimaryInfoKey, 'thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail']),
                    }
                    if not component['thumbnails']:
                        component['thumbnails'] =         self.__getValue(infoElement, [playlistPrimaryInfoKey, 'thumbnailRenderer', 'playlistCustomThumbnailRenderer', 'thumbnail', 'thumbnails']),
                    component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
                    playlistComponent.update(component)
                if playlistSecondaryInfoKey in infoElement.keys():
                    component = {
                        'channel': {
                            'name':                       await self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'title', 'runs', 0, 'text']),
                            'id':                         await self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'title', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                            'thumbnails':                 await self.__getValue(infoElement, [playlistSecondaryInfoKey, 'videoOwner', 'videoOwnerRenderer', 'thumbnail', 'thumbnails']),
                        },
                    }
                    component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
                    playlistComponent.update(component)
        if mode in ['getVideos', None]:
            playlistComponent['videos'] = []
            for videoElement in element['videos']:
                if playlistVideoKey in videoElement:
                    videoComponent = {
                        'id':                             await self.__getValue(videoElement, [playlistVideoKey, 'videoId']),
                        'title':                          await self.__getValue(videoElement, [playlistVideoKey, 'title', 'runs', 0, 'text']),
                        'thumbnails':                     await self.__getValue(videoElement, [playlistVideoKey, 'thumbnail', 'thumbnails']),
                        'channel': {
                            'name':                       await self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'text']),
                            'id':                         await self.__getValue(videoElement, [playlistVideoKey, 'shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                        },
                        'duration':                       await self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'simpleText']),
                        'accessibility': {
                            'title':                      await self.__getValue(videoElement, [playlistVideoKey, 'title', 'accessibility', 'accessibilityData', 'label']),
                            'duration':                   await self.__getValue(videoElement, [playlistVideoKey, 'lengthText', 'accessibility', 'accessibilityData', 'label']),
                        },
                    }
                    videoComponent['link'] = 'https://www.youtube.com/watch?v=' + videoComponent['id']
                    videoComponent['channel']['link'] = 'https://www.youtube.com/channel/' + videoComponent['channel']['id']
                    playlistComponent['videos'].append(
                        videoComponent
                    )
                if continuationItemKey in videoElement.keys():
                    self.continuationKey = await self.__getValue(videoElement, continuationKeyPath)
        return playlistComponent

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
            self.responseSource = await loads(self.response[self.response.index('(') + 1: self.response.index(')')])
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
