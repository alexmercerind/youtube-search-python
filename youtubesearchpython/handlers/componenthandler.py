from typing import List, Union
from youtubesearchpython.internal.constants import *


class ComponentHandler:
    def _getVideoComponent(self, element: dict, shelfTitle: str = None) -> dict:
        video = element[videoElementKey]
        component = {
            'type':                           'video',
            'id':                              self._getValue(video, ['videoId']),
            'title':                           self._getValue(video, ['title', 'runs', 0, 'text']),
            'publishedTime':                   self._getValue(video, ['publishedTimeText', 'simpleText']),
            'duration':                        self._getValue(video, ['lengthText', 'simpleText']),
            'viewCount': {
                'text':                        self._getValue(video, ['viewCountText', 'simpleText']),
                'short':                       self._getValue(video, ['shortViewCountText', 'simpleText']),
            },
            'thumbnails':                      self._getValue(video, ['thumbnail', 'thumbnails']),
            'richThumbnail':                   self._getValue(video, ['richThumbnail', 'movingThumbnailRenderer', 'movingThumbnailDetails', 'thumbnails', 0]),
            'descriptionSnippet':              self._getValue(video, ['detailedMetadataSnippets', 0, 'snippetText', 'runs']),
            'channel': {
                'name':                        self._getValue(video, ['ownerText', 'runs', 0, 'text']),
                'id':                          self._getValue(video, ['ownerText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
                'thumbnails':                  self._getValue(video, ['channelThumbnailSupportedRenderers', 'channelThumbnailWithLinkRenderer', 'thumbnail', 'thumbnails']),
            },
            'accessibility': {
                'title':                       self._getValue(video, ['title', 'accessibility', 'accessibilityData', 'label']),
                'duration':                    self._getValue(video, ['lengthText', 'accessibility', 'accessibilityData', 'label']),
            },
        }
        component['link'] = 'https://www.youtube.com/watch?v=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        component['shelfTitle'] = shelfTitle
        return component

    def _getChannelComponent(self, element: dict) -> dict:
        channel = element[channelElementKey]
        component = {
            'type':                           'channel',
            'id':                              self._getValue(channel, ['channelId']),
            'title':                           self._getValue(channel, ['title', 'simpleText']),
            'thumbnails':                      self._getValue(channel, ['thumbnail', 'thumbnails']),
            'videoCount':                      self._getValue(channel, ['videoCountText', 'runs', 0, 'text']),
            'descriptionSnippet':              self._getValue(channel, ['descriptionSnippet', 'runs']),
            'subscribers':                     self._getValue(channel, ['subscriberCountText', 'simpleText']),
        }
        component['link'] = 'https://www.youtube.com/channel/' + component['id']
        return component

    def _getPlaylistComponent(self, element: dict) -> dict:
        playlist = element[playlistElementKey]
        component = {
            'type':                           'playlist',
            'id':                             self._getValue(playlist, ['playlistId']),
            'title':                          self._getValue(playlist, ['title', 'simpleText']),
            'videoCount':                     self._getValue(playlist, ['videoCount']),
            'channel': {
                'name':                       self._getValue(playlist, ['shortBylineText', 'runs', 0, 'text']),
                'id':                         self._getValue(playlist, ['shortBylineText', 'runs', 0, 'navigationEndpoint', 'browseEndpoint', 'browseId']),
            },
            'thumbnails':                     self._getValue(playlist, ['thumbnailRenderer', 'playlistVideoThumbnailRenderer', 'thumbnail', 'thumbnails']),
        }
        component['link'] = 'https://www.youtube.com/playlist?list=' + component['id']
        component['channel']['link'] = 'https://www.youtube.com/channel/' + component['channel']['id']
        return component
    
    def _getVideoFromChannelSearch(self, elements: list) -> list:
        channelsearch = []
        for element in elements:
            element = element["childVideoRenderer"]
            json = {
                "id":                                    element["videoId"],
                "title":                                 element["title"]["simpleText"],
                "uri":                                   element["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"],
                "duration": {
                    "simpleText":                        element["lengthText"]["simpleText"],
                    "text":                              element["lengthText"]["accessibility"]["accessibilityData"]["label"]
                }
            }
            channelsearch.append(json)
        return channelsearch
    
    def _getChannelSearchComponent(self, elements: list) -> list:
        channelsearch = []
        for element in elements:
            responsetype = None
            try:
                element = element["itemSectionRenderer"]["contents"][0]["videoRenderer"]
                responsetype = "video"
            except:
                element = element["itemSectionRenderer"]["contents"][0]["playlistRenderer"]
                responsetype = "playlist"
            
            try:
                rich = element["richThumbnail"]["movingThumbnailRenderer"]["movingThumbnailDetails"]["thumbnails"]
            except:
                rich = None
            
            if responsetype == "video":
                json = {
                    "id":                                    element["videoId"],
                    "thumbnails": {
                        "normal":                            element["thumbnail"]["thumbnails"],
                        "rich":                              rich
                    },
                    "title":                                 element["title"]["runs"][0]["text"],
                    "descriptionSnippet":                    element["descriptionSnippet"]["runs"][0]["text"],
                    "uri":                                   element["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"],
                    "views": {
                        "precise":                           element["viewCountText"]["simpleText"],
                        "simple":                            element["shortViewCountText"]["simpleText"],
                        "approximate":                       element["shortViewCountText"]["accessibility"]["accessibilityData"]["label"]
                    },
                    "duration": {
                        "simpleText":                        element["lengthText"]["simpleText"],
                        "text":                              element["lengthText"]["accessibility"]["accessibilityData"]["label"]
                    },
                    "published":                             element["publishedTimeText"]["simpleText"],
                    "channel": {
                        "name":                              element["ownerText"]["runs"][0]["text"],
                        "thumbnails":                        element["channelThumbnailSupportedRenderers"]["channelThumbnailWithLinkRenderer"]["thumbnail"]["thumbnails"]
                    },
                    "type":                                  responsetype
                }
            else:
                json = {
                    "id":                                    element["playlistId"],
                    "videos":                                self._getVideoFromChannelSearch(element["videos"]),
                    "thumbnails": {
                        "normal":                            element["thumbnails"],
                    },
                    "title":                                 element["title"]["simpleText"],
                    "uri":                                   element["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"],
                    "channel": {
                        "name":                              element["longBylineText"]["runs"][0]["text"],
                    },
                    "type":                                  responsetype
                }
            channelsearch.append(json)
        return channelsearch

    def _getShelfComponent(self, element: dict) -> dict:
        shelf = element[shelfElementKey]
        return {
            'title':                           self._getValue(shelf, ['title', 'simpleText']),
            'elements':                        self._getValue(shelf, ['content', 'verticalListRenderer', 'items']),
        }

    def _getValue(self, source: dict, path: List[str]) -> Union[str, int, dict, None]:
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
