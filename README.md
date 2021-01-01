# [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)

#### :mag_right: Search for videos, channels & playlists in YouTube WITHOUT YouTube Data API v3.

[![PyPI - Version](https://img.shields.io/pypi/v/youtube-search-python?style=for-the-badge)](https://pypi.org/project/youtube-search-python)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/youtube-search-python?label=DOWNLOADS&style=for-the-badge)](https://pypi.org/project/youtube-search-python)

Works without YouTube Data API v3 and has zero dependencies.

This library is intended for personal and non-commercial usage only.

Working as of 2020.


## :floppy_disk: Install

```bash
pip install youtube-search-python
```

## :triangular_ruler: Usage

#### Search for only videos

```python
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

print(videosSearch.result())
```

<details>
 <summary> :page_with_curl: Example Result</summary>

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

#### Search for only channels

```python
from youtubesearchpython import ChannelsSearch

channelsSearch = ChannelsSearch('NoCopyrightSounds', limit = 10, region = 'US')

print(channelsSearch.result())
```

<details>
 <summary> :page_with_curl: Example Result</summary>

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
 <summary> :page_with_curl: Example Result</summary>

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
 <summary> :page_with_curl: Example Result</summary>

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
 <summary> :page_with_curl: Example Result</summary>

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

You may see the [example](https://github.com/alexmercerind/youtube-search-python/blob/main/example.py) for more information.


## :safety_pin: Advanced

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
videoInfo = Video.getInfo('https://youtube.be/z0GKGpObgPY', mode = ResultMode.json)
print(videoInfo)
videoFormats = Video.getFormats('z0GKGpObgPY')
print(videoFormats)
```

<details>
 <summary> :page_with_curl: Example Result</summary>

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
        {
            "itag": 247,
            "mimeType": "video/webm; codecs=\"vp9\"",
            "bitrate": 1411634,
            "width": 1280,
            "height": 720,
            "initRange": {
                "start": "0",
                "end": "219"
            },
            "indexRange": {
                "start": "220",
                "end": "843"
            },
            "lastModified": "1594499983470339",
            "contentLength": "20252155",
            "quality": "hd720",
            "fps": 24,
            "qualityLabel": "720p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 858083,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=t%3DP%3DQ0iWYy2kPwwI-g_U1lhdFZtWfFpY-mM7gxiGMoDQiHjCQICg7O4oTCfO%3Df1-Vlu8EPf27HmFBw1sOWWg_6F6EEpcvNgIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D247%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D20252155%26dur%3D188.813%26lmt%3D1594499983470339%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgIlUxe-kstQRO7uedc6cUb--vhesPvsOGlHw0Ogt8CqoCIGGGwHSDIpZ0Ha5mwTThINlcLuqxFhT6s8wVHv-9UjGJ"
        },
        {
            "itag": 398,
            "mimeType": "video/mp4; codecs=\"av01.0.05M.08\"",
            "bitrate": 1298354,
            "width": 1280,
            "height": 720,
            "initRange": {
                "start": "0",
                "end": "699"
            },
            "indexRange": {
                "start": "700",
                "end": "1187"
            },
            "lastModified": "1602399017348388",
            "contentLength": "22763625",
            "quality": "hd720",
            "fps": 24,
            "qualityLabel": "720p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 964493,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=5OeOuPOIASYOxHu4UZDm_VWnd4Xm77PkxXSIdwSCAIJxBIC8YQV9VKx8O2hyrFfNenipqe9oyEtOwuKu8wCD0ABhCUgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D398%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D22763625%26dur%3D188.813%26lmt%3D1602399017348388%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhALNHVrbAcIz8oeCGewHNCLgOBT6MK1XFAtHQvlcsU_ZeAiEAgtPPX58dlmHFOqwn0kDXSrXiphRS3UXdpRLC0c0S_zI%253D"
        },
        {
            "itag": 135,
            "mimeType": "video/mp4; codecs=\"avc1.4d401e\"",
            "bitrate": 752615,
            "width": 854,
            "height": 480,
            "initRange": {
                "start": "0",
                "end": "738"
            },
            "indexRange": {
                "start": "739",
                "end": "1226"
            },
            "lastModified": "1601811623769408",
            "contentLength": "12595470",
            "quality": "large",
            "fps": 24,
            "qualityLabel": "480p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 533669,
            "approxDurationMs": "188813",
            "signatureCipher": "s=lnbn4QYhuCb2TmNMvs_23hwJGETcfSPmLFJNs7ZMMQ5oFICEESleIu7rfyXf7iffW1NXIb6xEV7T2CzZvZ8WooAz6IgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D135%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D12595470%26dur%3D188.813%26lmt%3D1601811623769408%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgR8GkdQA1550-mvLG9JoMdX20GnJrFfMN9tVCrpK0Vv0CIQDT8CmS1Ow2ZHUTUpG-NwFmqGDRBrX9sXFtkahqfn49rQ%253D%253D"
        },
        {
            "itag": 244,
            "mimeType": "video/webm; codecs=\"vp9\"",
            "bitrate": 754861,
            "width": 854,
            "height": 480,
            "initRange": {
                "start": "0",
                "end": "219"
            },
            "indexRange": {
                "start": "220",
                "end": "838"
            },
            "lastModified": "1594499983400387",
            "contentLength": "11978644",
            "quality": "large",
            "fps": 24,
            "qualityLabel": "480p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 507534,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=yBSBDagdgPCNmqtapE6EQ_7niw66NODAhc7dGuW3dgTEHICUMZYMczDwP4TYbusF2e8TSSs5FoAvbdqB6TuFIDUQAJgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D244%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D11978644%26dur%3D188.813%26lmt%3D1594499983400387%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAM7lCIV1ys-3fC5ujneG4ochMcmUyIikA6cjICnIqBE4AiAxWOlRiKDP4xsZwjTS8uM673yMlSt6YKMhhdtbP_cRvw%253D%253D"
        },
        {
            "itag": 397,
            "mimeType": "video/mp4; codecs=\"av01.0.04M.08\"",
            "bitrate": 720068,
            "width": 854,
            "height": 480,
            "initRange": {
                "start": "0",
                "end": "699"
            },
            "indexRange": {
                "start": "700",
                "end": "1187"
            },
            "lastModified": "1602401012614756",
            "contentLength": "12406224",
            "quality": "large",
            "fps": 24,
            "qualityLabel": "480p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 525651,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=b%3Df%3DQiP6P-brffJXEZyUf-o5w65xnjeELkD_i_6vDQ2Sj7MCQIC4daBWmy2M%3D-sHGY9Ogf3jRvNCHzEOUXgy16F3h02r9BgIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D397%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D12406224%26dur%3D188.813%26lmt%3D1602401012614756%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgONxpzRxgk2V1Mawrk3iqKC83eSzpLhUVUT3whVGjeioCIFaN-vc8HqivkrpWu_bbaq8qr_OOJ0vhTJAoo9uNsT_g"
        },
        {
            "itag": 134,
            "mimeType": "video/mp4; codecs=\"avc1.4d401e\"",
            "bitrate": 578010,
            "width": 640,
            "height": 360,
            "initRange": {
                "start": "0",
                "end": "738"
            },
            "indexRange": {
                "start": "739",
                "end": "1226"
            },
            "lastModified": "1601811623839405",
            "contentLength": "8777298",
            "quality": "medium",
            "fps": 24,
            "qualityLabel": "360p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 371893,
            "highReplication": true,
            "approxDurationMs": "188813",
            "signatureCipher": "s=u%3Dg%3Dgs4HdWb4aM7gSFyso1jmn1Gsue_q8Nkc89zTh2LAdhjAiA2PDquUNjxv%3DvuJLOwF9gJb8EpJCAEmyrzc4oDXCv5HOAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D134%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D8777298%26dur%3D188.813%26lmt%3D1601811623839405%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgBOY1GMg5VpVpU1maFwWdAbpbl7z_azpeE3_xipP9zawCIQClo0N16Z2akgs5J8EfZJIg5uM7z3Vaza2eNqgqHAFHSw%253D%253D"
        },
        {
            "itag": 243,
            "mimeType": "video/webm; codecs=\"vp9\"",
            "bitrate": 412165,
            "width": 640,
            "height": 360,
            "initRange": {
                "start": "0",
                "end": "219"
            },
            "indexRange": {
                "start": "220",
                "end": "838"
            },
            "lastModified": "1594499983386260",
            "contentLength": "7611998",
            "quality": "medium",
            "fps": 24,
            "qualityLabel": "360p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 322520,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=mzIzUQGm6GeQSePhCzqN-Gm6YHAR7rFO4YHH4ltuUcZaGICQNNyZnHuax752Y-LibyVR9ILFV3TPljanLznqPc692agIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D243%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D7611998%26dur%3D188.813%26lmt%3D1594499983386260%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAJgPY7kYXa1Hv4x9FMRpXIDg5q565YQCIu2M8hPMhv8GAiALpEYZNPITAyZbH3AMRUCWJcWDxJB8ZQRxF21pzUbNGw%253D%253D"
        },
        {
            "itag": 396,
            "mimeType": "video/mp4; codecs=\"av01.0.01M.08\"",
            "bitrate": 382566,
            "width": 640,
            "height": 360,
            "initRange": {
                "start": "0",
                "end": "699"
            },
            "indexRange": {
                "start": "700",
                "end": "1187"
            },
            "lastModified": "1609487253789141",
            "contentLength": "6728270",
            "quality": "medium",
            "fps": 24,
            "qualityLabel": "360p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 285076,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=zQbQ9BBip2pdMRscnaNNOolK7E-CQBg4xsJWQVTpQGOvBICEkh50sAnj2c_4ZzE3Tkr1WbZCq-KU_VWvSedPDZ66tDgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D396%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D6728270%26dur%3D188.813%26lmt%3D1609487253789141%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5532434%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgPpoMASZvmpuhhvPuTHYTxJWMKOzB4itzQYjkziHrWksCIQDVqywaqT5pnQDmSaWDWLjiUN1fuJ3u1UsL8d8RWsaoQg%253D%253D"
        },
        {
            "itag": 133,
            "mimeType": "video/mp4; codecs=\"avc1.4d4015\"",
            "bitrate": 305779,
            "width": 426,
            "height": 240,
            "initRange": {
                "start": "0",
                "end": "738"
            },
            "indexRange": {
                "start": "739",
                "end": "1226"
            },
            "lastModified": "1601811623766061",
            "contentLength": "4866855",
            "quality": "small",
            "fps": 24,
            "qualityLabel": "240p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 206208,
            "approxDurationMs": "188813",
            "signatureCipher": "s=qQlQVM2r0eyKHR5xgsBzgeFqizNqLQOpveVXLqgRVWyQE1AEiARgO2Ez2sph%3D1lEEGMaLl7zODxERHYtkHAj_8LLuf9oLAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D133%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D4866855%26dur%3D188.813%26lmt%3D1601811623766061%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAMUb1G7lVcc4WUzgrN0Cnzjny_0Lo-QKEYPEqRno1eIvAiEA0_xk8M6isqhhjHjDduJnTCkJWpqSkquvRFsi8ZoAvmo%253D"
        },
        {
            "itag": 242,
            "mimeType": "video/webm; codecs=\"vp9\"",
            "bitrate": 227782,
            "width": 426,
            "height": 240,
            "initRange": {
                "start": "0",
                "end": "218"
            },
            "indexRange": {
                "start": "219",
                "end": "837"
            },
            "lastModified": "1594499983390711",
            "contentLength": "4309129",
            "quality": "small",
            "fps": 24,
            "qualityLabel": "240p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 182577,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=h%3Dk%3DA4kotVq5so9NyM5zgIDXURnpt-cgzVnddBV_WxA0WWMAiAYCnHLAeTxj%3DvsF2Np_IkNf19CdzmFI64xjh1_Iz1OaJAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D242%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D4309129%26dur%3D188.813%26lmt%3D1594499983390711%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgaTFbb_c-NyxXB6MpPU8WB01pk5rzFiweh_aTpPOe7nACIQD7RUY2rGXiNCjm5z4CcLcbc-YoXkqBxRlJi44VSbE1LA%253D%253D"
        },
        {
            "itag": 395,
            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
            "bitrate": 193091,
            "width": 426,
            "height": 240,
            "initRange": {
                "start": "0",
                "end": "699"
            },
            "indexRange": {
                "start": "700",
                "end": "1187"
            },
            "lastModified": "1602395881376171",
            "contentLength": "3533778",
            "quality": "small",
            "fps": 24,
            "qualityLabel": "240p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 149726,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=1%3Dz%3DQUxrhGZ6ly3nsmhzrfU2CaUl9RnFa6nsoF0cS7RVNLMBiA9gqFDzsh-g%3DU_IUAC9xzpf4BiSoK27ZgiaOCAXH4OaNAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D395%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D3533778%26dur%3D188.813%26lmt%3D1602395881376171%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAIEXsfR9sXnDANSLzD2wgntiXVbmuWq6pCbc-LYdSsSmAiEAudnFO_FiQr8bPTl7SLHUjn1Vv0ggUJ6cNYFN1-b7iCY%253D"
        },
        {
            "itag": 160,
            "mimeType": "video/mp4; codecs=\"avc1.4d400c\"",
            "bitrate": 111021,
            "width": 256,
            "height": 144,
            "initRange": {
                "start": "0",
                "end": "737"
            },
            "indexRange": {
                "start": "738",
                "end": "1225"
            },
            "lastModified": "1601811623837537",
            "contentLength": "2072344",
            "quality": "tiny",
            "fps": 24,
            "qualityLabel": "144p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 87805,
            "approxDurationMs": "188813",
            "signatureCipher": "s=9AfA-zo3wcxGr89oKn8mTGGYATh1fRL56SBu_LYrXmpCHpAEiAM5-Z16Cgnu%3D3GH8KJZ9fjTuXkEr6AcmE77233bRLBbLAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D160%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D2072344%26dur%3D188.813%26lmt%3D1601811623837537%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgHN25FlNVcoDRRQbf9gCjEFly3PrJDjcZ6RDhyIc2tQECIQDppVit7iejBp061kPASpd4C3y-cj7VLUw3ViruWaiuhg%253D%253D"
        },
        {
            "itag": 278,
            "mimeType": "video/webm; codecs=\"vp9\"",
            "bitrate": 98097,
            "width": 256,
            "height": 144,
            "initRange": {
                "start": "0",
                "end": "218"
            },
            "indexRange": {
                "start": "219",
                "end": "837"
            },
            "lastModified": "1594499983383530",
            "contentLength": "2150987",
            "quality": "tiny",
            "fps": 24,
            "qualityLabel": "144p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 91137,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=8UIUvriI_KqTF9N408LlQvzX0aqSJon5nKYHTRrZTN47GtAEiAueTeV6LFNm%3DGF9Sc5pcIS2xTLUpiHhX1C-UkVkW0XqMAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D278%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D2150987%26dur%3D188.813%26lmt%3D1594499983383530%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgUplnWR1Rfu9B11aSVzIAdEJoah-WggPxsxlKE4Ou_PsCIBWaH4h4ERokj__81UzW6YpQxK7DNfb3kUD50mrZIH1-"
        },
        {
            "itag": 394,
            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
            "bitrate": 82683,
            "width": 256,
            "height": 144,
            "initRange": {
                "start": "0",
                "end": "699"
            },
            "indexRange": {
                "start": "700",
                "end": "1187"
            },
            "lastModified": "1609493305821258",
            "contentLength": "1659821",
            "quality": "tiny",
            "fps": 24,
            "qualityLabel": "144p",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 70326,
            "colorInfo": {
                "primaries": "COLOR_PRIMARIES_BT709",
                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
            },
            "approxDurationMs": "188813",
            "signatureCipher": "s=wo4on8xiH4BPRJ-GDa7AAZiQLdvBbEG2JwjGGOLLYHaaBICwu7MH8n-w_CvBS2AKYr8P74x_Ze1_JN1pLJjwn2JfmLgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D394%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D1659821%26dur%3D188.813%26lmt%3D1609493305821258%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5532434%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAJ0SU3XdycCtDCs2lOiV5NJjAsZ6m2la2zN2_wXg_pnuAiBT4abCYN3YqWFzGhdipDTRjMmEzNnn4v8JheGgV2KSGw%253D%253D"
        },
        {
            "itag": 140,
            "mimeType": "audio/mp4; codecs=\"mp4a.40.2\"",
            "bitrate": 130381,
            "initRange": {
                "start": "0",
                "end": "631"
            },
            "indexRange": {
                "start": "632",
                "end": "891"
            },
            "lastModified": "1601809963189273",
            "contentLength": "3057341",
            "quality": "tiny",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 129499,
            "highReplication": true,
            "audioQuality": "AUDIO_QUALITY_MEDIUM",
            "approxDurationMs": "188871",
            "audioSampleRate": "44100",
            "audioChannels": 2,
            "loudnessDb": 6.1900001,
            "signatureCipher": "s=M%3DS%3DAlvT2g7kV36w_b1KoQlrqdCZ4LtCUjMonmkr3p-1PZkAiAbl_qb0lykr%3Dk6cri1mTSk4J6j1xowG3Pw6X34eOyWqMAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D140%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D3057341%26dur%3D188.871%26lmt%3D1601809963189273%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgSRL_e5R8XnRh7pOaPSKaBmC6Jz1mJUbrzf6J9ZfACPcCIFSprO8pqkhCT052gxRHDh2UEwMWinHiPHKZmH4HXr-8"
        },
        {
            "itag": 249,
            "mimeType": "audio/webm; codecs=\"opus\"",
            "bitrate": 54961,
            "initRange": {
                "start": "0",
                "end": "258"
            },
            "indexRange": {
                "start": "259",
                "end": "577"
            },
            "lastModified": "1594498100826963",
            "contentLength": "1151622",
            "quality": "tiny",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 48786,
            "audioQuality": "AUDIO_QUALITY_LOW",
            "approxDurationMs": "188841",
            "audioSampleRate": "48000",
            "audioChannels": 2,
            "loudnessDb": 6.1900001,
            "signatureCipher": "s=a%3De%3DgO5_vFsMvfW5wbJJmgMsUUWnvKXTSPbWDNQV5uTQdPaBiAl2V80AXV7R%3Dpf5f4VnkeRz3dSUE5q_c19KUvT_WSzYLAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D249%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D1151622%26dur%3D188.841%26lmt%3D1594498100826963%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgd_1Ezc5wFz7cIUY0X5hbuGIS3YJHo1XjCfRLc6d629UCIDRrE9mFHG5OyoCc0ySxta56vjqFmHCXh05IrVbkSPzb"
        },
        {
            "itag": 250,
            "mimeType": "audio/webm; codecs=\"opus\"",
            "bitrate": 70403,
            "initRange": {
                "start": "0",
                "end": "258"
            },
            "indexRange": {
                "start": "259",
                "end": "577"
            },
            "lastModified": "1594498110473681",
            "contentLength": "1518207",
            "quality": "tiny",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 64316,
            "audioQuality": "AUDIO_QUALITY_LOW",
            "approxDurationMs": "188841",
            "audioSampleRate": "48000",
            "audioChannels": 2,
            "loudnessDb": 6.1900001,
            "signatureCipher": "s=O%3Dg%3DQMHtYOQBw_YLTXlJ8W5xY0ZYms3jL4-fEAqDNZ7V7qAAiAe3sv6PQID8%3Dy5pkYzGrgnFEslUXBF7J5E2RFBMg_yJMAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D250%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D1518207%26dur%3D188.841%26lmt%3D1594498110473681%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAMhseOQnTni1bj-5JVVe4mUAM1oNoUtXOQFVzWRU8GHHAiAYsOo3Dv8r6gEWnCJWJ8sdXFRuD78hghT-33x8cRGI2g%253D%253D"
        },
        {
            "itag": 251,
            "mimeType": "audio/webm; codecs=\"opus\"",
            "bitrate": 135695,
            "initRange": {
                "start": "0",
                "end": "258"
            },
            "indexRange": {
                "start": "259",
                "end": "577"
            },
            "lastModified": "1594498099017464",
            "contentLength": "2933357",
            "quality": "tiny",
            "projectionType": "RECTANGULAR",
            "averageBitrate": 124267,
            "audioQuality": "AUDIO_QUALITY_MEDIUM",
            "approxDurationMs": "188841",
            "audioSampleRate": "48000",
            "audioChannels": 2,
            "loudnessDb": 6.1900001,
            "signatureCipher": "s=iE1Ev7003kBIMkOGrbRjxXqkm4slwC2pqCY5CJuTxaMqHnAEiAZOk6qgeRcc%3DYgm9kcnF17HeiW_Sjsbna-nN1-3h3SIKAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D251%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D2933357%26dur%3D188.841%26lmt%3D1594498099017464%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAP491Wcaof1Bb3XZxhzH8H5SrvAhR5wh5It1_z-03KPHAiAjP4ZU3ND8aOyEKz32HI1iDA9bku4tuxloXZKBE-Bang%253D%253D"
        }
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
    "expiresInSeconds": "21540"
}
```

</details>

#### Getting search suggestions

```python
from youtubesearchpython import Suggestions

suggestions = Suggestions(language = 'en', region = 'US')

print(suggestions.get('NoCopyrightSounds', mode = ResultMode.json))
```

<details>
 <summary> :page_with_curl: Example Result</summary>

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


## :wrench: Configuration

While instantiating any of the classes, you may provide optional parameters as follows to get the results accordingly.

```py
search = Search('NoCopyrightSounds', limit = 20, language = 'en', region = 'US')
```

You may switch between the types of result, by changing the value of ```mode``` optional parameter while calling the ```result``` method.

##### Getting JSON

```py
result = search.result(mode = ResultMode.json)
```

##### Getting dictionary


```py
result = search.result(mode = ResultMode.dict)
```

## :page_facing_up: License

MIT
