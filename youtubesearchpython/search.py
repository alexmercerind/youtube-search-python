from youtubesearchpython.base.constants import *
from youtubesearchpython.base.basesearch import BaseSearch


class Search(BaseSearch):
    '''
    Searches for all types of results like videos, channels & playlists in YouTube.
    Parameters
    ----------
    query : str
        Used as a query to search for videos in YouTube.
    page : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    limit : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
       Used to get results in particular language. Defaults to 'en-US'
    region: str, optional
       Used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the result from YouTube.
    '''
    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US'):
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
            if len(self.resultComponents) >= self.limit:
                break

class SearchVideos(BaseSearch):
    '''
    Searches only for videos in YouTube.
    Parameters
    ----------
    query : str
        Used as a query to search for videos in YouTube.
    page : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    limit : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
       Used to get results in particular language. Defaults to 'en-US'
    region: str, optional
       Used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the result from YouTube.
    '''
    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.videos)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if VIDEO_ELEMENT in element.keys():
                self.resultComponents.append(self.getVideoComponent(element))
            if SHELF_ELEMENT in element.keys():
                for shelfElement in self.getShelfComponent(element)['elements']:
                    self.resultComponents.append(self.getVideoComponent(shelfElement, shelfTitle = self.getShelfComponent(element)['title']))
            if len(self.resultComponents) >= self.limit:
                break


class SearchChannels(BaseSearch):
    '''
    Searches only for channels in YouTube.
    Parameters
    ----------
    query : str
        Used as a query to search for videos in YouTube.
    page : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    limit : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
       Used to get results in particular language. Defaults to 'en-US'
    region: str, optional
       Used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the result from YouTube.
    '''
    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.channels)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if CHANNEL_ELEMENT in element.keys():
                self.resultComponents.append(self.getChannelComponent(element))
            if len(self.resultComponents) >= self.limit:
                break


class SearchPlaylists(BaseSearch):
    '''
    Searches only for playlists in YouTube.
    Parameters
    ----------
    query : str
        Used as a query to search for videos in YouTube.
    page : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    limit : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
       Used to get results in particular language. Defaults to 'en-US'
    region: str, optional
       Used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the result from YouTube.
    '''
    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US'):
        super().__init__(query, page = page, limit = limit, language = language, region = region, searchPreferences = SearchMode.playlists)
        self.__makeComponents()
    
    def __makeComponents(self) -> None:
        for element in self.responseSource:
            if PLAYLIST_ELEMENT in element.keys():
                self.resultComponents.append(self.getPlaylistComponent(element))
            if len(self.resultComponents) >= self.limit:
                break

class SearchCustom(BaseSearch):
    '''
   Used to perform custom search in YouTube.
    Parameters
    ----------
    query : str
        Used as a query to search for videos in YouTube.
    searchPreferences : str
        Sets the 'sp' query parameter in the YouTube search requests, which can be used to get results according to your requirement. Example - https://www.youtube.com/results?search_query=NoCopyrightSounds&sp=EgQQARgB
    page : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    limit : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
       Used to get results in particular language. Defaults to 'en-US'
    region: str, optional
       Used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the result from YouTube.
    '''
    def __init__(self, query: str, searchPreferences: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US'):
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
            if len(self.resultComponents) >= self.limit:
                break
