from typing import Any, Dict, Optional

from youtubesearchpython.core.channelsearch import ChannelSearchCore
from youtubesearchpython.core.constants import *
from youtubesearchpython.core.search import SearchCore


class Search(SearchCore):
    '''Searches for videos, channels & playlists in YouTube.

    Args:
        query (str): Sets the search query.
        limit (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = Search('Watermelon Sugar', limit = 1)
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "type": "video",
                    "id": "E07s5ZYygMg",
                    "title": "Harry Styles - Watermelon Sugar (Official Video)",
                    "publishedTime": "6 months ago",
                    "duration": "3:09",
                    "viewCount": {
                        "text": "162,235,006 views",
                        "short": "162M views"
                    },
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAOWBTE1SDrtrDQ1aWNzpDZ7YiMIw",
                            "width": 360,
                            "height": 202
                        },
                        {
                            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD7U54pGZLPKTuMP-J3kpm4LIDPVg",
                            "width": 720,
                            "height": 404
                        }
                    ],
                    "descriptionSnippet": [
                        {
                            "text": "This video is dedicated to touching. Listen to Harry Styles' new album 'Fine Line' now: https://HStyles.lnk.to/FineLineAY Follow\u00a0..."
                        }
                    ],
                    "channel": {
                        "name": "Harry Styles",
                        "id": "UCZFWPqqPkFlNwIxcpsLOwew",
                        "thumbnails": [
                            {
                                "url": "https://yt3.ggpht.com/a-/AOh14GgNUvHxwlnz4RpHamcGnZF1px13VHj01TPksw=s68-c-k-c0x00ffffff-no-rj-mo",
                                "width": 68,
                                "height": 68
                            }
                        ],
                        "link": "https://www.youtube.com/channel/UCZFWPqqPkFlNwIxcpsLOwew"
                    },
                    "accessibility": {
                        "title": "Harry Styles - Watermelon Sugar (Official Video) by Harry Styles 6 months ago 3 minutes, 9 seconds 162,235,006 views",
                        "duration": "3 minutes, 9 seconds"
                    },
                    "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
                    "shelfTitle": null
                }
            ]
        }
    '''
    def __init__(self, query: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: Optional[int] = None):
        self.searchMode = (True, True, True)
        super().__init__(query, limit, language, region, None, timeout)  # type: ignore

    async def next(self) -> Dict[str, Any]:
        return await self._nextAsync()  # type: ignore


class VideosSearch(SearchCore):
    '''Searches for videos in YouTube.

    Args:
        query (str): Sets the search query.
        limit (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = VideosSearch('Watermelon Sugar', limit = 1)
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "type": "video",
                    "id": "E07s5ZYygMg",
                    "title": "Harry Styles - Watermelon Sugar (Official Video)",
                    "publishedTime": "6 months ago",
                    "duration": "3:09",
                    "viewCount": {
                        "text": "162,235,006 views",
                        "short": "162M views"
                    },
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAOWBTE1SDrtrDQ1aWNzpDZ7YiMIw",
                            "width": 360,
                            "height": 202
                        },
                        {
                            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD7U54pGZLPKTuMP-J3kpm4LIDPVg",
                            "width": 720,
                            "height": 404
                        }
                    ],
                    "descriptionSnippet": [
                        {
                            "text": "This video is dedicated to touching. Listen to Harry Styles' new album 'Fine Line' now: https://HStyles.lnk.to/FineLineAY Follow\u00a0..."
                        }
                    ],
                    "channel": {
                        "name": "Harry Styles",
                        "id": "UCZFWPqqPkFlNwIxcpsLOwew",
                        "thumbnails": [
                            {
                                "url": "https://yt3.ggpht.com/a-/AOh14GgNUvHxwlnz4RpHamcGnZF1px13VHj01TPksw=s68-c-k-c0x00ffffff-no-rj-mo",
                                "width": 68,
                                "height": 68
                            }
                        ],
                        "link": "https://www.youtube.com/channel/UCZFWPqqPkFlNwIxcpsLOwew"
                    },
                    "accessibility": {
                        "title": "Harry Styles - Watermelon Sugar (Official Video) by Harry Styles 6 months ago 3 minutes, 9 seconds 162,235,006 views",
                        "duration": "3 minutes, 9 seconds"
                    },
                    "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
                    "shelfTitle": null
                }
            ]
        }
    '''
    def __init__(self, query: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: Optional[int] = None):
        self.searchMode = (True, False, False)
        super().__init__(query, limit, language, region, SearchMode.videos, timeout)  # type: ignore

    async def next(self) -> Dict[str, Any]:
        return await self._nextAsync()  # type: ignore


class ChannelsSearch(SearchCore):
    '''Searches for channels in YouTube.

    Args:
        query (str): Sets the search query.
        limit (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = ChannelsSearch('Harry Styles', limit = 1)
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "type": "channel",
                    "id": "UCZFWPqqPkFlNwIxcpsLOwew",
                    "title": "Harry Styles",
                    "thumbnails": [
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhR81ocC_KalYEk5ItnJcfMBqaiIpuM1B0lJyg4Rw=s88-c-k-c0x00ffffff-no-rj-mo",
                            "width": 88,
                            "height": 88
                        },
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhR81ocC_KalYEk5ItnJcfMBqaiIpuM1B0lJyg4Rw=s176-c-k-c0x00ffffff-no-rj-mo",
                            "width": 176,
                            "height": 176
                        }
                    ],
                    "videoCount": "7",
                    "descriptionSnippet": null,
                    "subscribers": "9.25M subscribers",
                    "link": "https://www.youtube.com/channel/UCZFWPqqPkFlNwIxcpsLOwew"
                }
            ]
        }
    '''
    def __init__(self, query: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: Optional[int] = None):
        self.searchMode = (False, True, False)
        super().__init__(query, limit, language, region, SearchMode.channels, timeout)  # type: ignore

    async def next(self) -> Dict[str, Any]:
        return await self._nextAsync()  # type: ignore


class PlaylistsSearch(SearchCore):
    '''Searches for playlists in YouTube.

    Args:
        query (str): Sets the search query.
        limit (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = PlaylistsSearch('Harry Styles', limit = 1)
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "type": "playlist",
                    "id": "PL-Rt4gIwHnyvxpEl-9Le0ePztR7WxGDGV",
                    "title": "fine line harry styles full album lyrics",
                    "videoCount": "12",
                    "channel": {
                        "name": "ourmemoriestonight",
                        "id": "UCZCmb5a8LE9LMxW9I3-BFjA",
                        "link": "https://www.youtube.com/channel/UCZCmb5a8LE9LMxW9I3-BFjA"
                    },
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/raTh8Mu5oyM/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLCdCfOQYMrPImHMObdrMcNimKi1PA",
                            "width": 168,
                            "height": 94
                        },
                        {
                            "url": "https://i.ytimg.com/vi/raTh8Mu5oyM/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDsKmyGH8bkmt9MzZqIoXI4UaduBw",
                            "width": 196,
                            "height": 110
                        },
                        {
                            "url": "https://i.ytimg.com/vi/raTh8Mu5oyM/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD9v7S0KeHLBLr0bF-LrRjYVycUFA",
                            "width": 246,
                            "height": 138
                        },
                        {
                            "url": "https://i.ytimg.com/vi/raTh8Mu5oyM/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAIzQIVxZsC0PfvLOt-v9UWJ-109Q",
                            "width": 336,
                            "height": 188
                        }
                    ],
                    "link": "https://www.youtube.com/playlist?list=PL-Rt4gIwHnyvxpEl-9Le0ePztR7WxGDGV"
                }
            ]
        }
    '''
    def __init__(self, query: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: Optional[int] = None):
        self.searchMode = (False, False, True)
        super().__init__(query, limit, language, region, SearchMode.playlists, timeout)  # type: ignore

    async def next(self) -> Dict[str, Any]:
        return await self._nextAsync()  # type: ignore

class CustomSearch(SearchCore):
    '''Performs custom search in YouTube with search filters or sorting orders. 
    Few of the predefined filters and sorting orders are:

        1 - SearchMode.videos
        2 - VideoUploadDateFilter.lastHour
        3 - VideoDurationFilter.long
        4 - VideoSortOrder.viewCount

    There are many other to use.
    The value of `sp` parameter in the YouTube search query can be used as a search filter e.g. 
    `EgQIBRAB` from https://www.youtube.com/results?search_query=NoCopyrightSounds&sp=EgQIBRAB can be passed as `searchPreferences`, to get videos, which are uploaded this year.

    Args:
        query (str): Sets the search query.
        searchPreferences (str): Sets the `sp` query parameter in the YouTube search request.
        limit (int, optional): Sets limit to the number of results. Defaults to 20.
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.
    
    Examples:
        Calling `result` method gives the search result.

        >>> search = CustomSearch('Harry Styles', VideoSortOrder.viewCount, limit = 1)
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "type": "video",
                    "id": "QJO3ROT-A4E",
                    "title": "One Direction - What Makes You Beautiful (Official Video)",
                    "publishedTime": "9 years ago",
                    "duration": "3:27",
                    "viewCount": {
                        "text": "1,212,146,802 views",
                        "short": "1.2B views"
                    },
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/QJO3ROT-A4E/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDeFKrH99gmpnvKyG4czdd__YRDkw",
                            "width": 360,
                            "height": 202
                        },
                        {
                            "url": "https://i.ytimg.com/vi/QJO3ROT-A4E/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBJ_wUjsRFXGsbvRpwYpSLlsGmbkw",
                            "width": 720,
                            "height": 404
                        }
                    ],
                    "descriptionSnippet": [
                        {
                            "text": "One Direction \u2013 What Makes You Beautiful (Official Video) Follow on Spotify - https://1D.lnk.to/Spotify Listen on Apple Music\u00a0..."
                        }
                    ],
                    "channel": {
                        "name": "One Direction",
                        "id": "UCb2HGwORFBo94DmRx4oLzow",
                        "thumbnails": [
                            {
                                "url": "https://yt3.ggpht.com/a-/AOh14Gj3SMvtIAvVNUrHWFTJFubPN7qozzPl5gFkoA=s68-c-k-c0x00ffffff-no-rj-mo",
                                "width": 68,
                                "height": 68
                            }
                        ],
                        "link": "https://www.youtube.com/channel/UCb2HGwORFBo94DmRx4oLzow"
                    },
                    "accessibility": {
                        "title": "One Direction - What Makes You Beautiful (Official Video) by One Direction 9 years ago 3 minutes, 27 seconds 1,212,146,802 views",
                        "duration": "3 minutes, 27 seconds"
                    },
                    "link": "https://www.youtube.com/watch?v=QJO3ROT-A4E",
                    "shelfTitle": null
                }
            ]
        }
    '''
    def __init__(self, query: str, searchPreferences: str, limit: int = 20, language: str = 'en', region: str = 'US', timeout: Optional[int] = None):
        self.searchMode = (True, True, True)
        super().__init__(query, limit, language, region, searchPreferences, timeout)  # type: ignore

    async def next(self) -> Dict[str, Any]:
        return await self._nextAsync()  # type: ignore

class ChannelSearch(ChannelSearchCore):
    '''Searches for videos in specific channel in YouTube.

    Args:
        query (str): Sets the search query.
        browseId (str): Channel ID
        language (str, optional): Sets the result language. Defaults to 'en'.
        region (str, optional): Sets the result region. Defaults to 'US'.

    Examples:
        Calling `result` method gives the search result.

        >>> search = ChannelSearch('Watermelon Sugar', "UCZFWPqqPkFlNwIxcpsLOwew")
        >>> result = await search.next()
        >>> print(result)
        {
            "result": [
                {
                    "id": "WMcIfZuRuU8",
                    "thumbnails": {
                        "normal": [
                            {
                                "url": "https://i.ytimg.com/vi/WMcIfZuRuU8/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLClFg6C1r5NfTQy7TYUq6X5qHUmPA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/WMcIfZuRuU8/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAoOyftwY0jLV4geWb5hejULYp3Zw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/WMcIfZuRuU8/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCdqkhn7JDwLvRtTNx3jq-olz7k-Q",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/WMcIfZuRuU8/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAhYedsqBFKI0Ra2qzIv9cVoZhfKQ",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "rich": null
                    },
                    "title": "Harry Styles \u2013 Watermelon Sugar (Lost Tour Visual)",
                    "descriptionSnippet": "This video is dedicated to touching.\nListen to Harry Styles\u2019 new album \u2018Fine Line\u2019 now: https://HStyles.lnk.to/FineLineAY \n\nFollow Harry Styles:\nFacebook: https://HarryStyles.lnk.to/followFI...",
                    "uri": "/watch?v=WMcIfZuRuU8",
                    "views": {
                        "precise": "3,888,287 views",
                        "simple": "3.8M views",
                        "approximate": "3.8 million views"
                    },
                    "duration": {
                        "simpleText": "2:55",
                        "text": "2 minutes, 55 seconds"
                    },
                    "published": "10 months ago",
                    "channel": {
                        "name": "Harry Styles",
                        "thumbnails": [
                            {
                                "url": "https://yt3.ggpht.com/ytc/AAUvwnhR81ocC_KalYEk5ItnJcfMBqaiIpuM1B0lJyg4Rw=s88-c-k-c0x00ffffff-no-rj",
                                "width": 68,
                                "height": 68
                            }
                        ]
                    },
                    "type": "video"
                },
            ]
        }
    '''

    def __init__(self, query: str, browseId: str, language: str = 'en', region: str = 'US', searchPreferences: str = "EgZzZWFyY2g%3D", timeout: Optional[int] = None):
        super().__init__(query, language, region, searchPreferences, browseId, timeout)  # type: ignore
