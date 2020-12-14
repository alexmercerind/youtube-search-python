from youtubesearchpython.base.constants import *
from youtubesearchpython.base.basesearch import BaseSearch


class Search(BaseSearch):
    def __init__(self, query, page = 1, limit = 20, language = 'en-US', region = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys():
                self.resultComponents.append(self.getVideoComponent(element))
            if CHANNEL_ELEMENT in element.keys():
                self.resultComponents.append(self.getChannelComponent(element))
            if PLAYLIST_ELEMENT in element.keys():
                self.resultComponents.append(self.getPlaylistComponent(element))
            if SHELF_ELEMENT in element.keys():
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))


class SearchVideos(BaseSearch):
    def __init__(self, query, page = 1, limit = 20, language = 'en-US', region = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.videos)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys():
                self.resultComponents.append(self.getVideoComponent(element))
            if SHELF_ELEMENT in element.keys():
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))


class SearchChannels(BaseSearch):
    def __init__(self, query, page = 1, limit = 20, language = 'en-US', region = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.channels)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if CHANNEL_ELEMENT in element.keys():
                self.resultComponents.append(self.getChannelComponent(element))


class SearchPlaylists(BaseSearch):
    def __init__(self, query, page = 1, limit = 20, language = 'en-US', region = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.playlists)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if PLAYLIST_ELEMENT in element.keys():
                self.resultComponents.append(self.getPlaylistComponent(element))

class SearchCustom(BaseSearch):
    def __init__(self, query, searchPreferences: str, page = 1, limit = 20, language = 'en-US', region = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = searchPreferences)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys():
                self.resultComponents.append(self.getVideoComponent(element))
            if CHANNEL_ELEMENT in element.keys():
                self.resultComponents.append(self.getChannelComponent(element))
            if PLAYLIST_ELEMENT in element.keys():
                self.resultComponents.append(self.getPlaylistComponent(element))
            if SHELF_ELEMENT in element.keys():
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))