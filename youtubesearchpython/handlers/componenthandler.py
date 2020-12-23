from typing import List, Union
from youtubesearchpython.internal.constants import *


class ComponentHandler:
    def getVideoComponent(self, element: dict, shelfTitle: str = None) -> dict:
        video = element[videoElementKey]
        component = {
            'type':                           'video',
            'id':                              self.__getValue(video, ['videoId']),
            'title':                           self.__getValue(video, ['title', 'runs', 0, 'text']),
            'publishedTime':                   self.__getValue(video, ['publishedTimeText', 'simpleText']),
            'duration':                        self.__getValue(video, ['lengthText', 'simpleText']),
            'viewCount': {
                'text':                        self.__getValue(video, ['viewCountText', 'simpleText']),
                'short':                       self.__getValue(video, ['shortViewCountText', 'simpleText']),
            },
            'thumbnails':                      self.__getValue(video, ['thumbnail', 'thumbnails']),
            'descriptionSnippet':              self.__getValue(video, ['descriptionSnippet', 'runs']),
            'channel': {
                'name':                        self.__getValue(video, ['ownerText', 'runs', 0, 'text']),
                'id':                          self.__getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                'thumbnails':                  self.__getValue(video, ['channelThumbnailSupportedRenderers', 'channelThumbnailWithLinkRenderer', 'thumbnail', 'thumbnails']),
            },
            'accessibility': {
                'title':                       self.__getValue(video, ['title', 'accessibility', 'accessibilityData', 'label']),
                'duration':                    self.__getValue(video, ['lengthText', 'accessibility', 'accessibilityData', 'label']),
            },
        }
        component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        component['shelfTitle'] = shelfTitle
        return component

    def getChannelComponent(self, element: dict) -> dict:
        channel = element[channelElementKey]
        component = {
            'type':                           'channel',
            'id':                              self.__getValue(channel, ['channelId']),
            'title':                           self.__getValue(channel, ['title', 'simpleText']),
            'thumbnails':                      self.__getValue(channel, ['thumbnail', 'thumbnails']),
            'videoCount':                      self.__getValue(channel, ['videoCountText', 'runs', 0, 'text']),
            'descriptionSnippet':              self.__getValue(channel, ['descriptionSnippet', 'runs']),
            'subscribers':                     self.__getValue(channel, ['subscriberCountText', 'simpleText']),
        }
        component['link'] = 'https://www.youtube.com/channel/' + component['id']
        return component

    def getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[playlistElementKey]
        component = {
            'type':                           'playlist',
            'id':                             self.__getValue(playlist, ['playlistId']),
            'title':                          self.__getValue(playlist, ['title', 'simpleText']),
            'videoCount':                     self.__getValue(playlist, ['videoCount']),
            'channel': {
                'name':                       self.__getValue(playlist, ['shortBylineText', 'runs', 0, 'text']),
                'id':                         self.__getValue(playlist, ['shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
            },
            'thumbnails':                     self.__getValue(playlist, ['thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail', 'thumbnails']),
        }
        component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        return component

    def getShelfComponent(self, element: dict) -> dict:
        shelf = element[shelfElementKey]
        return {
            'title':                           self.__getValue(shelf, ['title', 'simpleText']),
            'elements':                        self.__getValue(shelf, ['content', 'verticalListRenderer', 'items']),
        }

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
