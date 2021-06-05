from typing import List, Union
from youtubesearchpython.__future__.internal.constants import *


class ComponentHandler:
    async def _getVideoComponent(self, element: dict, shelfTitle: str = None) -> dict:
        video = element[videoElementKey]
        component = {
            'type':                           'video',
            'id':                              await self._getValue(video, ['videoId']),
            'title':                           await self._getValue(video, ['title', 'runs', 0, 'text']),
            'publishedTime':                   await self._getValue(video, ['publishedTimeText', 'simpleText']),
            'duration':                        await self._getValue(video, ['lengthText', 'simpleText']),
            'viewCount': {
                'text':                        await self._getValue(video, ['viewCountText', 'simpleText']),
                'short':                       await self._getValue(video, ['shortViewCountText', 'simpleText']),
            },
            'thumbnails':                      await self._getValue(video, ['thumbnail', 'thumbnails']),
            'richThumbnail':                   await self._getValue(video, ['richThumbnail', 'movingThumbnailRenderer', 'movingThumbnailDetails', 'thumbnails', 0]),
            'descriptionSnippet':              await self._getValue(video, ['detailedMetadataSnippets', 0, 'snippetText', 'runs']),
            'channel': {
                'name':                        await self._getValue(video, ['ownerText', 'runs', 0, 'text']),
                'id':                          await self._getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                'thumbnails':                  await self._getValue(video, ['channelThumbnailSupportedRenderers', 'channelThumbnailWithLinkRenderer', 'thumbnail', 'thumbnails']),
            },
            'accessibility': {
                'title':                       await self._getValue(video, ['title', 'accessibility', 'accessibilityData', 'label']),
                'duration':                    await self._getValue(video, ['lengthText', 'accessibility', 'accessibilityData', 'label']),
            },
        }
        component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        component['shelfTitle'] = shelfTitle
        return component

    async def _getChannelComponent(self, element: dict) -> dict:
        channel = element[channelElementKey]
        component = {
            'type':                           'channel',
            'id':                              await self._getValue(channel, ['channelId']),
            'title':                           await self._getValue(channel, ['title', 'simpleText']),
            'thumbnails':                      await self._getValue(channel, ['thumbnail', 'thumbnails']),
            'videoCount':                      await self._getValue(channel, ['videoCountText', 'runs', 0, 'text']),
            'descriptionSnippet':              await self._getValue(channel, ['descriptionSnippet', 'runs']),
            'subscribers':                     await self._getValue(channel, ['subscriberCountText', 'simpleText']),
        }
        component['link'] = 'https://www.youtube.com/channel/' + component['id']
        return component

    async def _getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[playlistElementKey]
        component = {
            'type':                           'playlist',
            'id':                             await self._getValue(playlist, ['playlistId']),
            'title':                          await self._getValue(playlist, ['title', 'simpleText']),
            'videoCount':                     await self._getValue(playlist, ['videoCount']),
            'channel': {
                'name':                       await self._getValue(playlist, ['shortBylineText', 'runs', 0, 'text']),
                'id':                         await self._getValue(playlist, ['shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
            },
            'thumbnails':                     await self._getValue(playlist, ['thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail', 'thumbnails']),
        }
        component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        return component

    async def _getShelfComponent(self, element: dict) -> dict:
        shelf = element[shelfElementKey]
        return {
            'title':                           await self._getValue(shelf, ['title', 'simpleText']),
            'elements':                        await self._getValue(shelf, ['content', 'verticalListRenderer', 'items']),
        }

    async def _getValue(self, source: dict, path: List[Union[str, int]]) -> Union[str, int, dict, None]:
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
