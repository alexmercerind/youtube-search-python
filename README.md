# [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)

##### Search for YouTube videos, channels & playlists. Get video & playlist information using link. Get search suggestions.

#### WITHOUT YouTube Data API v3.

[![PyPI - Version](https://img.shields.io/pypi/v/youtube-search-python?style=for-the-badge)](https://pypi.org/project/youtube-search-python)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/youtube-search-python?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/youtube-search-python)

## Installing

```bash
pip3 install youtube-search-python
```

## Sync

#### Search for only videos

```python
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

print(videosSearch.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "video",
            "id": "K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "publishedTime": "5 years ago",
            "duration": "3:28",
            "viewCount": {
                "text": "389,673,774 views",
                "short": "389M views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBkTusCwcZQlmVAaRQ5rH-mvBuA1g",
                    "width": 480,
                    "height": 270
                }
            ],
            "richThumbnail": {
                "url": "https://i.ytimg.com/an_webp/K4DyBUG242c/mqdefault_6s.webp?du=3000&sqp=COCn64IG&rs=AOn4CLBeYxeJ_5lME4jXbFQlv7kIN37kmw",
                "width": 320,
                "height": 180
            },
            "descriptionSnippet": [
                {
                    "text": "NCS: Music Without Limitations NCS Spotify: http://spoti.fi/NCS Free Download / Stream: http://ncs.io/onandon \u25bd Connect with\u00a0..."
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GhS0G5FwV8rMhVCUWSDp36vWEvnNs5Vl97Zww=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "accessibility": {
                "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release] by NoCopyrightSounds 5 years ago 3 minutes, 28 seconds 389,673,774 views",
                "duration": "3 minutes, 28 seconds"
            },
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "shelfTitle": null
        },
        {
            "type": "video",
            "id": "yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "publishedTime": "3 years ago",
            "duration": "3:50",
            "viewCount": {
                "text": "153,353,801 views",
                "short": "153M views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/yJg-Y5byMMw/hqdefault.jpg?sqp=-oaymwEjCOADEI4CSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDY-mve79IweErMo-71AsKEIB1m0A",
                    "width": 480,
                    "height": 270
                }
            ],
            "richThumbnail": {
                "url": "https://i.ytimg.com/an_webp/K4DyBUG242c/mqdefault_6s.webp?du=3000&sqp=COCn64IG&rs=AOn4CLBeYxeJ_5lME4jXbFQlv7kIN37kmw",
                "width": 320,
                "height": 180
            },
            "descriptionSnippet": [
                {
                    "text": "NCS: Music Without Limitations NCS Spotify: http://spoti.fi/NCS Free Download / Stream: http://ncs.io/mortals Connect with NCS:\u00a0..."
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GhS0G5FwV8rMhVCUWSDp36vWEvnNs5Vl97Zww=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "accessibility": {
                "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 50 seconds 153,353,801 views",
                "duration": "3 minutes, 50 seconds"
            },
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "shelfTitle": null
        }
    ]
}
```

</details>

## Async

#### Search for only videos

```python
from youtubesearchpython.__future__ import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)
videosResult = await videosSearch.next()
print(videosResult)
```

Read more about usage & examples of newer asynchronous version of this library [HERE](https://github.com/alexmercerind/youtube-search-python/tree/main/youtubesearchpython/__future__).


## Support

Please consider buying me a coffee, if you like this library.

<a href="https://www.buymeacoffee.com/alexmercerind"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=alexmercerind&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff"></a>

Feel free to ping me on Discord at alexmercerind#3898 for any kind of help! 👌

Thankyou.

## More Examples

#### Search for only channels

```python
from youtubesearchpython import ChannelsSearch

channelsSearch = ChannelsSearch('NoCopyrightSounds', limit = 10, region = 'US')

print(channelsSearch.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "channel",
            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngbenDpBxHNZlecDGyccHeVyQB22dPZnPuhbW8LHw=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngbenDpBxHNZlecDGyccHeVyQB22dPZnPuhbW8LHw=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "850",
            "descriptionSnippet": [
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " is a copyright free / stream safe record label, providing free to use music to the content creator community."
                }
            ],
            "subscribers": "28.7M subscribers",
            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "type": "channel",
            "id": "UCg-vlcyvOyNVPV6Neogmubg",
            "title": "NoCopyrightSounds Hindi",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnjDHXULXSvX7u71Rmb2f-Cqly0ron2F1N3szu8Y=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnjDHXULXSvX7u71Rmb2f-Cqly0ron2F1N3szu8Y=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "56",
            "descriptionSnippet": [
                {
                    "text": "The Official NCS HINDI Songs Channel for Nocopyright hindi audios."
                }
            ],
            "subscribers": "13.7K subscribers",
            "link": "https://www.youtube.com/channel/UCg-vlcyvOyNVPV6Neogmubg"
        },
        {
            "type": "channel",
            "id": "UCrL9x8LllOU2LOVgTo951kA",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnhXShCsmo9VwL4KC8j3GNHgHyBBJ0RCmbAUKrwg=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnhXShCsmo9VwL4KC8j3GNHgHyBBJ0RCmbAUKrwg=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "2",
            "descriptionSnippet": [
                {
                    "text": "NCS [NopCopyrightSounds] is a channel dedicated to promoting the best FREE DOWNLOAD music on the net. Every track\u00a0..."
                }
            ],
            "subscribers": "1.71K subscribers",
            "link": "https://www.youtube.com/channel/UCrL9x8LllOU2LOVgTo951kA"
        },
        {
            "type": "channel",
            "id": "UCYZvaL6G3m4-UbvWGlyFeLg",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnisxA4V_U0Ffh0K-cdnqwGZjs62hKv2-IAfzIqc=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnisxA4V_U0Ffh0K-cdnqwGZjs62hKv2-IAfzIqc=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "33",
            "descriptionSnippet": null,
            "subscribers": null,
            "link": "https://www.youtube.com/channel/UCYZvaL6G3m4-UbvWGlyFeLg"
        },
        {
            "type": "channel",
            "id": "UCi7xVhyWWf2eTc0GO0Ty9HQ",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngOJ2zbLEkNs96PNp0g9h27l64mwRFhR1vZ9W7u=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngOJ2zbLEkNs96PNp0g9h27l64mwRFhR1vZ9W7u=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "1 video",
            "descriptionSnippet": null,
            "subscribers": "2 subscribers",
            "link": "https://www.youtube.com/channel/UCi7xVhyWWf2eTc0GO0Ty9HQ"
        },
        {
            "type": "channel",
            "id": "UCOSiFTIAReRzkPBXaQAuXCQ",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwng1UBDlLdYyqTofL6x_5hqPMTFnMXxAN9C9_t8Y=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwng1UBDlLdYyqTofL6x_5hqPMTFnMXxAN9C9_t8Y=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "8",
            "descriptionSnippet": [
                {
                    "text": "YGW MEDIA GROUP 04."
                }
            ],
            "subscribers": "11 subscribers",
            "link": "https://www.youtube.com/channel/UCOSiFTIAReRzkPBXaQAuXCQ"
        },
        {
            "type": "channel",
            "id": "UCSFpIv5SZlg4ub_IWgGKkIA",
            "title": "NoCopyrightSounds Lyrics",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwng_J1igSuKFWowZ8OFpT1dPCPgzqEvVkGImwM3Dpg=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwng_J1igSuKFWowZ8OFpT1dPCPgzqEvVkGImwM3Dpg=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "82",
            "descriptionSnippet": [
                {
                    "text": "Welcome To "
                },
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " Lyrics "
                },
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " lyrics provides music from a variety of licenses that are certainly\u00a0..."
                }
            ],
            "subscribers": null,
            "link": "https://www.youtube.com/channel/UCSFpIv5SZlg4ub_IWgGKkIA"
        },
        {
            "type": "channel",
            "id": "UCcE-Gvu5j55MdREM1a4_EqA",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnhbzZwQIVabdGA1SteO2BCtmrG3uT_cpzmJvtBY=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnhbzZwQIVabdGA1SteO2BCtmrG3uT_cpzmJvtBY=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "6",
            "descriptionSnippet": null,
            "subscribers": "166 subscribers",
            "link": "https://www.youtube.com/channel/UCcE-Gvu5j55MdREM1a4_EqA"
        },
        {
            "type": "channel",
            "id": "UCCOWDgeFmwW--woYtCYws8Q",
            "title": "NoCopyrightSounds 1 HOUR",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnipj6lV7p6i8Mq7uAlDj5qHsQkiwgwdtPs_vCKy=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwnipj6lV7p6i8Mq7uAlDj5qHsQkiwgwdtPs_vCKy=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "689",
            "descriptionSnippet": [
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " is a record label dedicated to releasing FREE music for the sole purpose of providing creators with the finest\u00a0..."
                }
            ],
            "subscribers": null,
            "link": "https://www.youtube.com/channel/UCCOWDgeFmwW--woYtCYws8Q"
        },
        {
            "type": "channel",
            "id": "UCSI5zGuirscirQc6UOy_yww",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwni92w-CAOUnlNfyIVxdCmvMoQmENZbw1wjFOQKjug=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwni92w-CAOUnlNfyIVxdCmvMoQmENZbw1wjFOQKjug=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "29",
            "descriptionSnippet": [
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " is a Record Label dedicated to giving a platform to the next generation of Artists in Electronic Music,\u00a0..."
                }
            ],
            "subscribers": null,
            "link": "https://www.youtube.com/channel/UCSI5zGuirscirQc6UOy_yww"
        }
    ]
}
```

</details>

#### Search for only playlists

```python
from youtubesearchpython import PlaylistsSearch

playlistsSearch = PlaylistsSearch('NoCopyrightSounds', limit = 1)

print(playlistsSearch.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "playlist",
            "id": "PLGde6kPURikrUszpUgafLZiOgr5o7pBF0",
            "title": "NoCopyrightSounds",
            "videoCount": "6",
            "channel": {
                "name": "Bruno Neves",
                "id": "UCtqpCV2HkMCSi5InFNBNv0g",
                "link": "https://www.youtube.com/channel/UCtqpCV2HkMCSi5InFNBNv0g"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBw6Bf7J9COwl1LxqhmGbSQgdFj3w",
                    "width": 168,
                    "height": 94
                },
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLBjJCIZlrSGSPjc-7yKc0QQuWRdhg",
                    "width": 196,
                    "height": 110
                },
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCRIQ0IochteE0KM2tlK2PVVAQKhA",
                    "width": 246,
                    "height": 138
                },
                {
                    "url": "https://i.ytimg.com/vi/K4DyBUG242c/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAQYBDz8gWKw_q4Zyb_H6J_DdZCaA",
                    "width": 336,
                    "height": 188
                }
            ],
            "link": "https://www.youtube.com/playlist?list=PLGde6kPURikrUszpUgafLZiOgr5o7pBF0"
        }
    ]
}
```

</details>

#### Search with a filter or sort

```python
from youtubesearchpython import *

customSearch = CustomSearch('NoCopyrightSounds', VideoSortOrder.uploadDate, limit = 1)

print(customSearch.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "video",
            "id": "k8-drvf4Ruo",
            "title": "Ambient Music 2020 \ud83c\udfb5 voices \ud83c\udfb5 NoCopyrightSounds",
            "publishedTime": "30 minutes ago",
            "duration": "2:29",
            "viewCount": {
                "text": "4 views",
                "short": "4 views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/k8-drvf4Ruo/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDomB-9ivVHpwci6STdNAqQBMBzJA",
                    "width": 360,
                    "height": 202
                },
                {
                    "url": "https://i.ytimg.com/vi/k8-drvf4Ruo/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCPrVwYygJ3627h8F-oU3khKehm4g",
                    "width": 720,
                    "height": 404
                }
            ],
            "richThumbnail": {
                "url": "https://i.ytimg.com/an_webp/K4DyBUG242c/mqdefault_6s.webp?du=3000&sqp=COCn64IG&rs=AOn4CLBeYxeJ_5lME4jXbFQlv7kIN37kmw",
                "width": 320,
                "height": 180
            },
            "descriptionSnippet": [
                {
                    "text": "Don't forget to like & share if you enjoy it."
                }
            ],
            "channel": {
                "name": "Sky Sound",
                "id": "UCQT8W5qZn7TCZBW39dVoaBw",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/a-/AOh14GhxrkkF27iL3sLTKzWLu3rrO-qtQ7uMPg4SqA=s68-c-k-c0x00ffffff-no-rj-mo",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UCQT8W5qZn7TCZBW39dVoaBw"
            },
            "accessibility": {
                "title": "Ambient Music 2020 \ud83c\udfb5 voices \ud83c\udfb5 NoCopyrightSounds by Sky Sound 30 minutes ago 2 minutes, 29 seconds 4 views",
                "duration": "2 minutes, 29 seconds"
            },
            "link": "https://www.youtube.com/watch?v=k8-drvf4Ruo",
            "shelfTitle": null
        }
    ]
}
```

</details>

#### Search for everything

```python
from youtubesearchpython import Search

allSearch = Search('NoCopyrightSounds', limit = 1)

print(allSearch.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "channel",
            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "title": "NoCopyrightSounds",
            "thumbnails": [
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngbenDpBxHNZlecDGyccHeVyQB22dPZnPuhbW8LHw=s88-c-k-c0x00ffffff-no-rj-mo",
                    "width": 88,
                    "height": 88
                },
                {
                    "url": "//yt3.ggpht.com/ytc/AAUvwngbenDpBxHNZlecDGyccHeVyQB22dPZnPuhbW8LHw=s176-c-k-c0x00ffffff-no-rj-mo",
                    "width": 176,
                    "height": 176
                }
            ],
            "videoCount": "850",
            "descriptionSnippet": [
                {
                    "text": "NoCopyrightSounds",
                    "bold": true
                },
                {
                    "text": " is a copyright free / stream safe record label, providing free to use music to the content creator community."
                }
            ],
            "subscribers": "28.7M subscribers",
            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
    ]
}
```

</details>

You may see the [example](https://github.com/alexmercerind/youtube-search-python/blob/main/syncExample.py) for more information.


## Advanced

#### Getting next page search results

You may call ```next``` method as follows, to get the results on the next pages.

Calling ```result``` method after calling ```next``` will give you result on that the next page.

```python
from youtubesearchpython import VideosSearch

search = VideosSearch('NoCopyrightSounds')

print(search.result()['result'])

''' Getting result from 2nd page. '''
search.next()
print(search.result()['result'])

''' Getting result from 3rd page. '''
search.next()
print(search.result()['result'])

''' Getting result from 4th page. '''
search.next()
print(search.result()['result'])
```

#### Getting video information using video link or video ID

```python
'''
Getting information about video or its formats using video link or video ID.

`Video.get` method will give both information & formats of the video
`Video.getInfo` method will give only information about the video.
`Video.getFormats` method will give only formats of the video.

You may either pass link or ID, method will take care itself.
'''
video = Video.get('https://www.youtube.com/watch?v=z0GKGpObgPY', mode = ResultMode.json)
print(video)
videoInfo = Video.getInfo('https://youtu.be/z0GKGpObgPY', mode = ResultMode.json)
print(videoInfo)
videoFormats = Video.getFormats('z0GKGpObgPY')
print(videoFormats)
```

<details>
 <summary> Example Result</summary>

```json
{
    "id": "E07s5ZYygMg",
    "title": "Harry Styles - Watermelon Sugar (Official Video)",
    "viewCount": {
        "text": "170389228"
    },
    "thumbnails": [
        {
            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCT6nkbmYf-zbqAFgzF0D9PUhtsOQ",
            "width": 168,
            "height": 94
        },
        {
            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA-JdoctyNp4aaj9dVtR0c6l5RDVw",
            "width": 196,
            "height": 110
        },
        {
            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBquHs9OWY5Dy1nE_syglwKP6-pMw",
            "width": 246,
            "height": 138
        },
        {
            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDSjHwdHxt9aU8NTojucGLp4PurTA",
            "width": 336,
            "height": 188
        },
        {
            "url": "https://i.ytimg.com/vi/E07s5ZYygMg/maxresdefault.jpg?v=5ebedc0c",
            "width": 1920,
            "height": 1080
        }
    ],
    "description": "This video is dedicated to touching.\nListen to Harry Styles\u2019 new album \u2018Fine Line\u2019 now: https://HStyles.lnk.to/FineLineAY \n\nFollow Harry Styles:\nFacebook: https://HarryStyles.lnk.to/followFI\nInstagram: https://HarryStyles.lnk.to/followII\nTwitter: https://HarryStyles.lnk.to/followTI\nWebsite: https://HarryStyles.lnk.to/followWI\nSpotify: https://HarryStyles.lnk.to/followSI\nYouTube: https://HarryStyles.lnk.to/subscribeYD\n\nLyrics: \n\nTastes like strawberries\nOn a summer evening\nAnd it sounds just like a song\nI want more berries\nAnd that summer feeling\nIt\u2019s so wonderful and warm\nBreathe me in\nBreathe me out\nI don\u2019t know if I could ever go without\nI\u2019m just thinking out loud\nI don\u2019t know if I could ever go without\n \nWatermelon sugar high\nWatermelon sugar high\nWatermelon sugar high\nWatermelon sugar high\nWatermelon sugar\n \nStrawberries\nOn a summer evening\nBaby, you\u2019re the end of June\nI want your belly\nAnd that summer feeling\nGetting washed away in you\nBreathe me in\nBreathe me out\nI don\u2019t know if I could ever go without\n \nWatermelon sugar high\n \nI just wanna taste it\nI just wanna taste it\nWatermelon sugar high\n \nTastes like strawberries\nOn a summer evening\nAnd it sounds just like a song\nI want your belly\nAnd that summer feeling\nI don\u2019t know if I could ever go without\n \nWatermelon sugar high\n \nI just wanna taste it\nI just wanna taste it\nWatermelon sugar high\nI just wanna taste it\nI just wanna taste it\nWatermelon sugar high\n \nWatermelon Sugar\n\n#HarryStyles #WatermelonSugar #FineLine",
    "channel": {
        "name": "HarryStylesVEVO",
        "id": "UCbOCbp5gXL8jigIBZLqMPrw",
        "link": "https://www.youtube.com/channel/UCbOCbp5gXL8jigIBZLqMPrw"
    },
    "averageRating": 4.9043722,
    "keywords": [
        "Fine Line",
        "Harry Styles Fine Line",
        "New Harry Styles",
        "Harry Styles Album",
        "HS2",
        "One Direction",
        "Eroda",
        "HStyles",
        "HarryStyles",
        "New HS",
        "Watermelon",
        "Sugar",
        "Watermlon Sugar",
        "Harry Styles Watermelon Sugar",
        "Fine Line Watermelon Sugar",
        "Watermelon Sugar Fine Line",
        "Harry Styles Watermelon Sguar Official Audio",
        "Harry Styles Watermelon Sugar Song",
        "HS Watermelon Sugar",
        "Harry Styles Watermelon Sugar Video",
        "Harry Styles Watermelon Sugar Official Video",
        "Harry"
    ],
    "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
    "streamingData": [
        {
            "adaptiveFormats": [
                {
                    "itag": 137,
                    "mimeType": "video/mp4; codecs=\"avc1.640028\"",
                    "bitrate": 4517689,
                    "width": 1920,
                    "height": 1080,
                    "initRange": {
                        "start": "0",
                        "end": "740"
                    },
                    "indexRange": {
                        "start": "741",
                        "end": "1228"
                    },
                    "lastModified": "1601811652909447",
                    "contentLength": "75694686",
                    "quality": "hd1080",
                    "fps": 24,
                    "qualityLabel": "1080p",
                    "projectionType": "RECTANGULAR",
                    "averageBitrate": 3207181,
                    "approxDurationMs": "188813",
                    "signatureCipher": "s=F%3DX%3DgIkn_MWCUvQZ__3tR_7gPNDBeOz8n9M0WGxNtIZ6zwxAiA-VALQ9F5bz%3DW8I_Z8WfXPLHjEGEn_JRVVu7BcNJJfjKAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D137%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D75694686%26dur%3D188.813%26lmt%3D1601811652909447%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgTGJdeFFnVZy97rzAeBnJCSdcY7KWBCa21RQ9ZvkH0KsCIQD1-Vzcj53p39l_DWtK1b69VjQmtBi_SIZOZD0hzXHJNA%253D%253D"
                },
                {
                    "itag": 248,
                    "mimeType": "video/webm; codecs=\"vp9\"",
                    "bitrate": 2677426,
                    "width": 1920,
                    "height": 1080,
                    "initRange": {
                        "start": "0",
                        "end": "219"
                    },
                    "indexRange": {
                        "start": "220",
                        "end": "861"
                    },
                    "lastModified": "1594499920972798",
                    "contentLength": "54314997",
                    "quality": "hd1080",
                    "fps": 24,
                    "qualityLabel": "1080p",
                    "projectionType": "RECTANGULAR",
                    "averageBitrate": 2301324,
                    "colorInfo": {
                        "primaries": "COLOR_PRIMARIES_BT709",
                        "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                        "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                    },
                    "approxDurationMs": "188813",
                    "signatureCipher": "s=4WSWyDZ4VUW0FxNi5blaiF4ilQNYR-3uChA822Y034mMGICMPJy_OPOcgmaH7OjHiz7P3SA11EXoi7xWDBddADzQhXgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D248%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D54314997%26dur%3D188.813%26lmt%3D1594499920972798%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAJHI4m9CrBPc-vEl_qXPYvACMjDAgC7dGWk5cZ5yc4DTAiEA36ijZkSFmCngvJZ5ULpRFJLGB3wWohsxABHZJL_q4_c%253D"
                },
                {
                    "itag": 399,
                    "mimeType": "video/mp4; codecs=\"av01.0.08M.08\"",
                    "bitrate": 2252425,
                    "width": 1920,
                    "height": 1080,
                    "initRange": {
                        "start": "0",
                        "end": "699"
                    },
                    "indexRange": {
                        "start": "700",
                        "end": "1187"
                    },
                    "lastModified": "1602396935824004",
                    "contentLength": "40536309",
                    "quality": "hd1080",
                    "fps": 24,
                    "qualityLabel": "1080p",
                    "projectionType": "RECTANGULAR",
                    "averageBitrate": 1717521,
                    "colorInfo": {
                        "primaries": "COLOR_PRIMARIES_BT709",
                        "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                        "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                    },
                    "approxDurationMs": "188813",
                    "signatureCipher": "s=ZJwJxM3AbUoW4wiucKj-hgbD-KpvS21BYBD1lsDZa7SPCICMZo9flYaa2ePw-6CdA1a_DwNtjbk4KXaTb0U1btiIfDgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D399%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D40536309%26dur%3D188.813%26lmt%3D1602396935824004%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgB9Jm-n4o3HkYm1cr2pVG9NLb_7Tmp22lXGwKkWSiwZ0CIBKSMK5PqbPHniDqOFCPoqa4eT_Y8hQDSWM7k_V8A99p"
                },
                {
                    "itag": 136,
                    "mimeType": "video/mp4; codecs=\"avc1.4d401f\"",
                    "bitrate": 1247138,
                    "width": 1280,
                    "height": 720,
                    "initRange": {
                        "start": "0",
                        "end": "738"
                    },
                    "indexRange": {
                        "start": "739",
                        "end": "1226"
                    },
                    "lastModified": "1601811623765749",
                    "contentLength": "18074560",
                    "quality": "hd720",
                    "fps": 24,
                    "qualityLabel": "720p",
                    "projectionType": "RECTANGULAR",
                    "averageBitrate": 765818,
                    "approxDurationMs": "188813",
                    "signatureCipher": "s=y%3Dp%3DgBSUCkvVl7q-hefXAmtE95tx4YYx2uLiqm0fDKUL2hBCQICspkvlYjtn%3DvRH0iGB5p9zloazr8oDbuPc5yFs81PaJfgIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D136%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D18074560%26dur%3D188.813%26lmt%3D1601811623765749%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgKiY0iSKg4drfMpUtmsfY4DqN0dzkVo9z0NvbppT-vAUCIDajIym2RvvvqEqxK9XltraU3992scXuP8aZD_cXNK_0"
                },
            ],
            "formats": [
                {
                    "itag": 18,
                    "mimeType": "video/mp4; codecs=\"avc1.42001E, mp4a.40.2\"",
                    "bitrate": 635291,
                    "width": 640,
                    "height": 360,
                    "lastModified": "1594495537943093",
                    "contentLength": "14993923",
                    "quality": "medium",
                    "fps": 24,
                    "qualityLabel": "360p",
                    "projectionType": "RECTANGULAR",
                    "averageBitrate": 635096,
                    "audioQuality": "AUDIO_QUALITY_LOW",
                    "approxDurationMs": "188871",
                    "audioSampleRate": "44100",
                    "audioChannels": 2,
                    "signatureCipher": "s=AsPsztt4ZltrQC0ijKLX83bx8smNjCLHwb5D-pJLJvDGAmAEiAhvbstJR8js%3D7g7hscPbPtwrjUDtzwb1GgpkTG53d9kMAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dw-Sn-YFRtfT0kLnFKpo3EA4F%26gir%3Dyes%26clen%3D14993923%26ratebypass%3Dyes%26dur%3D188.871%26lmt%3D1594495537943093%26mt%3D1609499069%26fvip%3D7%26c%3DWEB%26txp%3D5531432%26n%3DV2sNxp4tEzNJkZtb%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgbrfk-x_xucwjZedmoR8sR3UQHP4OUd1jDUL_91palCICIQC0w6urClsmCBTpK27I5DIKKED9T_ci6blRj-c8rSD86A%253D%253D"
                }
            ],
        }
    ],
    "expiresInSeconds": "21540"
}
```

</details>

#### Getting playlist information using link

```python
'''
Getting information about playlist or videos in it using its link.

`Playlist.get` method will give both information & formats of the playlist
`Playlist.getInfo` method will give only information about the playlist.
`Playlist.getVideos` method will give only videos in the playlist.

'''
playlist = Playlist.get('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK', mode = ResultMode.json)
print(playlist)
playlistInfo = Playlist.getInfo('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK', mode = ResultMode.json)
print(playlistInfo)
playlistVideos = Playlist.getVideos('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')
print(playlistVideos)
```

<details>
 <summary> Example Result</summary>

```json
{
    "id": "PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
    "title": "NCS: House",
    "videoCount": "209",
    "viewCount": "155,772,054 views",
    "thumbnails": {
        "thumbnails": [
            {
                "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDHZYoB-WNHmvT3CZy6SpdqygsO4A",
                "width": 168,
                "height": 94
            },
            {
                "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLACCxCIRvCn65_OS1z_4tLAq5Jb8Q",
                "width": 196,
                "height": 110
            },
            {
                "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBt00cYTIVBdrnHsSNLinhq7meCpQ",
                "width": 246,
                "height": 138
            },
            {
                "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBFaqqO6kCAuqya1SIJo5Cf45Ndxg",
                "width": 336,
                "height": 188
            }
        ]
    },
    "link": "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
    "channel": {
        "name": "NoCopyrightSounds",
        "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
        "thumbnails": [
            {
                "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s48-c-k-c0x00ffffff-no-rj",
                "width": 48,
                "height": 48
            },
            {
                "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s88-c-k-c0x00ffffff-no-rj",
                "width": 88,
                "height": 88
            },
            {
                "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s176-c-k-c0x00ffffff-no-rj",
                "width": 176,
                "height": 176
            }
        ],
        "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
    },
    "videos": [
        {
            "id": "gQjAEbWZEgU",
            "title": "Mangoo - Happi (ft. bby ivy) [NCS Release]",
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/gQjAEbWZEgU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLB8IrOoqB1vSj2SMptjc5pG8fyKOQ",
                    "width": 168,
                    "height": 94
                },
                {
                    "url": "https://i.ytimg.com/vi/gQjAEbWZEgU/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDjI1SuDEFCqskIfGEqr8HZi3v54Q",
                    "width": 196,
                    "height": 110
                },
                {
                    "url": "https://i.ytimg.com/vi/gQjAEbWZEgU/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCAFP_0cHcbUnt_eJwozqM0mOPkHg",
                    "width": 246,
                    "height": 138
                },
                {
                    "url": "https://i.ytimg.com/vi/gQjAEbWZEgU/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD4WajUJ8zGjQDuwT6uHBbvZzaCPA",
                    "width": 336,
                    "height": 188
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "duration": "2:41",
            "accessibility": {
                "title": "Mangoo - Happi (ft. bby ivy) [NCS Release] by NoCopyrightSounds 7 months ago 2 minutes, 41 seconds",
                "duration": "2 minutes, 41 seconds"
            },
            "link": "https://www.youtube.com/watch?v=gQjAEbWZEgU"
        },
        {
            "id": "2Kh4y7pJjfQ",
            "title": "MAGNUS x Unread - Cool (feat. Alessia Labate) [NCS Release]",
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/2Kh4y7pJjfQ/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDBtmR1aLs9b5ULxWBpTitm2qfZgQ",
                    "width": 168,
                    "height": 94
                },
                {
                    "url": "https://i.ytimg.com/vi/2Kh4y7pJjfQ/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA1_KVxp3eun3REQPZM3qgdhGGKhw",
                    "width": 196,
                    "height": 110
                },
                {
                    "url": "https://i.ytimg.com/vi/2Kh4y7pJjfQ/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDXxtiCKSoQ7qWsmbyK60HytHlKNg",
                    "width": 246,
                    "height": 138
                },
                {
                    "url": "https://i.ytimg.com/vi/2Kh4y7pJjfQ/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAO6xgKiU0ObnMbcsaLgd5Sp-HA_Q",
                    "width": 336,
                    "height": 188
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "duration": "2:22",
            "accessibility": {
                "title": "MAGNUS x Unread - Cool (feat. Alessia Labate) [NCS Release] by NoCopyrightSounds 8 months ago 2 minutes, 22 seconds",
                "duration": "2 minutes, 22 seconds"
            },
            "link": "https://www.youtube.com/watch?v=2Kh4y7pJjfQ"
        },
        {
            "id": "7dw8wphQ118",
            "title": "Jim Yosef - Let You Go [NCS Release]",
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/7dw8wphQ118/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLAI2xKhoLZTQSKy_E2qLI8vmmLwzQ",
                    "width": 168,
                    "height": 94
                },
                {
                    "url": "https://i.ytimg.com/vi/7dw8wphQ118/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBm88JTaXMyMXgPpH0ANOP-5M7cdg",
                    "width": 196,
                    "height": 110
                },
                {
                    "url": "https://i.ytimg.com/vi/7dw8wphQ118/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDKDPLNxX6SpNNSCmp4oPA7gXZh2w",
                    "width": 246,
                    "height": 138
                },
                {
                    "url": "https://i.ytimg.com/vi/7dw8wphQ118/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCoilNTqi_D4Xu-EQFbiqcjyuewUw",
                    "width": 336,
                    "height": 188
                }
            ],
            "channel": {
                "name": "NoCopyrightSounds",
                "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
            },
            "duration": "3:40",
            "accessibility": {
                "title": "Jim Yosef - Let You Go [NCS Release] by NoCopyrightSounds 9 months ago 3 minutes, 40 seconds",
                "duration": "3 minutes, 40 seconds"
            },
            "link": "https://www.youtube.com/watch?v=7dw8wphQ118"
        }
    ]
}
```

</details>

#### More to the playlists

You can directly instanciate the `Playlist` class as follows to access its information & videos in the `info` and `videos` fields respectively.

YouTube offers only 100 videos in a single request, for getting more videos present in the playlist, you can check `hasMoreVideos` bool to see if playlist contains more videos.
If playlist has more videos, then you can call `getNextVideos` to fetch more videos.

Example below demonstrates a simple way to retrive all videos of a playlist.

```python
from youtubesearchpython import *

playlist = Playlist('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')

print(f'Videos Retrieved: {len(playlist.videos)}')

while playlist.hasMoreVideos:
    print('Getting more videos...')
    playlist.getNextVideos()
    print(f'Videos Retrieved: {len(playlist.videos)}')

print('Found all the videos.')
```

<details>
 <summary> Example Result</summary>

```bash
Videos Retrieved: 100
Getting more videos...
Videos Retrieved: 200
Getting more videos...
Videos Retrieved: 209
Found all the videos.
```

</details>

#### Getting search suggestions

```python
from youtubesearchpython import Suggestions

suggestions = Suggestions(language = 'en', region = 'US')

print(suggestions.get('NoCopyrightSounds', mode = ResultMode.json))
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        "nocopyrightsounds",
        "nocopyrightsounds best songs",
        "nocopyrightsounds gaming music",
        "nocopyrightsounds alan walker",
        "nocopyrightsounds fearless",
        "nocopyrightsounds invincible",
        "nocopyrightsounds background music",
        "nocopyrightsounds instrumental",
        "nocopyrightsounds fade",
        "nocopyrightsounds playlist",
        "nocopyrightsounds on and on",
        "nocopyrightsounds elektronomia",
        "nocopyrightsounds stronger",
        "nocopyrightsounds christmas"
    ]
}
```

</details>

#### Getting videos by hashtag

```python
from youtubesearchpython import Hashtag

hashtag = Hashtag('ncs', limit = 1)

print(hashtag.result())
```

<details>
 <summary> Example Result</summary>

```json
{
    "result": [
        {
            "type": "video",
            "id": "c9FF4Tfj2w8",
            "title": "Ascence - About You [NCS 1 HOUR]",
            "publishedTime": "1 year ago",
            "duration": "1:00:00",
            "viewCount": {
                "text": "226,354 views",
                "short": "226K views"
            },
            "thumbnails": [
                {
                    "url": "https://i.ytimg.com/vi/c9FF4Tfj2w8/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLA8V3x_PigkymVQxQcptr8Wfz20-A",
                    "width": 168,
                    "height": 94
                },
                {
                    "url": "https://i.ytimg.com/vi/c9FF4Tfj2w8/hqdefault.jpg?sqp=-oaymwEbCMQBEG5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLABh5Ylb5wbuulOAWLcSYtfYQKiAQ",
                    "width": 196,
                    "height": 110
                },
                {
                    "url": "https://i.ytimg.com/vi/c9FF4Tfj2w8/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAykmTivOgjlW6a4tKWnLJpL9yqKw",
                    "width": 246,
                    "height": 138
                },
                {
                    "url": "https://i.ytimg.com/vi/c9FF4Tfj2w8/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLC8qRkotPyH9kGGHe29QuyOh-F9KA",
                    "width": 336,
                    "height": 188
                }
            ],
            "richThumbnail": {
                "url": "https://i.ytimg.com/an_webp/c9FF4Tfj2w8/mqdefault_6s.webp?du=3000&sqp=CPGE-YgG&rs=AOn4CLAJAC5zmDOtySflLFMQpAoaPUqHjA",
                "width": 320,
                "height": 180
            },
            "descriptionSnippet": null,
            "channel": {
                "name": "Good Vibes Music",
                "id": "UChCPI0uvKwrkYhTEx8UVrnQ",
                "thumbnails": [
                    {
                        "url": "https://yt3.ggpht.com/ytc/AKedOLSFYY0mvwL0DbRzddMAQdbgFshM42R5byhI9FiEBQ=s68-c-k-c0x00ffffff-no-rj",
                        "width": 68,
                        "height": 68
                    }
                ],
                "link": "https://www.youtube.com/channel/UChCPI0uvKwrkYhTEx8UVrnQ"
            },
            "accessibility": {
                "title": "Ascence - About You [NCS 1 HOUR] by Good Vibes Music 1 year ago 1 hour 226,354 views",
                "duration": "1 hour"
            },
            "link": "https://www.youtube.com/watch?v=c9FF4Tfj2w8",
            "shelfTitle": null
        }
    ]
}
```

</details>

#### Getting videos and playlists in specific channel

```python
from youtubesearchpython import ChannelSearch

search = ChannelSearch('Watermelon Sugar', "UCZFWPqqPkFlNwIxcpsLOwew")
print(search.result(mode = ResultMode.json))
```

<details>
 <summary> Example Result</summary>

```json
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
```

</details>

#### Getting direct stream URL of a video

This class is able fetch video URLs without any additional web requests (that's fast), as one might already have same response at the time of showing it to the user.

For making use of this functionality, you must install [PyTube](https://github.com/pytube/pytube) as a dependency.
StreamURLFetcher makes slight improvements & changes to YouTube class from [PyTube](https://github.com/pytube/pytube).

```py
from youtubesearchpython import *
fetcher = StreamURLFetcher()
video = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
url = fetcher.get(video, 251)
print(url)

'''
`getAll` method returns all stream URLs unlike `get` method which needs itag in its second parameter.
'''
```

<details>
 <summary> Example Result</summary>

```json
"https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=251&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=audio%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=10210834&dur=634.601&lmt=1544629945422176&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5511222&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgKKIEiwQTgXsdKPEyOckgVPs_LMH6KJoeaYmZic_lelECIHXHs1ZnSP5mgtpffNlIMJM3DhxcvDbA-4udFFE6AmVP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D"
```

</details>

## License

MIT License

Copyright (c) 2021 [Hitesh Kumar Saini](https://github.com/alexmercerind)

## Information

- All the research, for making this library possible, is entirely done by myself.
- You can use this library & segments of code from it in your projects in any way you want. Just respect the MIT license & credit the original author of the project.
- Current version of this project (`main` branch) simulates the requests made by YouTube's web client during client side rendering. In simple words, it does not fetch any specific webpage's HTML, but the JSONs internally fetched by YouTube when you navigate the website, after loading the webpage completely.
- I do not resist you from using this library in any possible manner, but YouTube T&C stop you from using this library commercially. Respect the law.
- As you might tell by the name of the project, this library initially only used to support searching of videos. Later on, as the project grew, I added a lot of additional features after requests from people. Now, its really powerful.
