# [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)

#### Search for YouTube videos, channels & playlists & get video information using link WITHOUT YouTube Data API v3.

##### Important: As of v1.6.1, we no longer use PyTube (see https://github.com/alexmercerind/youtube-search-python/pull/155). You have to install yt-dlp in order to use StreamURLFetcher: `pip install yt-dlp`

Works without YouTube Data API v3 and has zero dependencies.

Working as of 2022.

## Support

If you really want to be kind to me, then you may buy me a coffee.

<a href="https://www.buymeacoffee.com/alexmercerind"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=alexmercerind&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff"></a>

Thankyou!

## Asynchronous

For making use of Asynchronous version of this library, import from the ```__future__``` subpackage as follows.

```py
from youtubesearchpython.__future__ import *
```

It is non-blocking & substantially faster than sync youtube-search-python.

**This may eventually replace the old version in future. Please upgrade your projects & packages.**

## Install

```bash
pip install youtube-search-python
```

## Usage

#### Search for only videos

```python
from youtubesearchpython.__future__ import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)
videosResult = await videosSearch.next()
print(videosResult)
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

#### Search for only channels

```python
from youtubesearchpython.__future__ import ChannelsSearch

channelsSearch = ChannelsSearch('NoCopyrightSounds', limit = 10, region = 'US')
channelsResult = await channelsSearch.next()
print(channelsResult)
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
from youtubesearchpython.__future__ import PlaylistsSearch

playlistsSearch = PlaylistsSearch('NoCopyrightSounds', limit = 1)
playlistsResult = await playlistsSearch.next()
print(playlistsResult)
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
from youtubesearchpython.__future__ import *

customSearch = CustomSearch('NoCopyrightSounds', VideoSortOrder.uploadDate, limit = 1)
customResult = await customSearch.next()
print(customResult)
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
from youtubesearchpython.__future__ import Search

search = Search('NoCopyrightSounds', limit = 1)
result = await search.next()
print(result)
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

You may see the [example](https://github.com/alexmercerind/youtube-search-python/blob/main/asyncExample.py) for more information.


## Advanced

#### Getting next page search results

You may call ```next``` method as follows, to get the results on the next pages.

Calling ```result``` method after calling ```next``` will give you result on that the next page.

```python
from youtubesearchpython.__future__ import VideosSearch

search = VideosSearch('NoCopyrightSounds')
result = await search.next()
print(result['result'])

''' Getting result from 2nd page. '''
result = await search.next()
print(result['result'])

''' Getting result from 3rd page. '''
result = await search.next()
print(result['result'])

''' Getting result from 4th page. '''
result = await search.next()
print(result['result'])
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
video = await Video.get('https://www.youtube.com/watch?v=z0GKGpObgPY')
print(video)
videoInfo = await Video.getInfo('https://youtu.be/z0GKGpObgPY')
print(videoInfo)
videoFormats = await Video.getFormats('z0GKGpObgPY')
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
    ],
    "expiresInSeconds": "21540"
}
```

</details>

#### Get all videos of a channel
You can use a Playlist class for that, alongside some helpful functions.
```python
from youtubesearchpython.__future__ import *

channel_id = "UC_aEa8K-EOJ3D6gOs7HcyNg"
playlist = Playlist(playlist_from_channel_id(channel_id))

print(f'Videos Retrieved: {len(playlist.videos)}')

while playlist.hasMoreVideos:
    print('Getting more videos...')
    await playlist.getNextVideos()
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
Videos Retrieved: 300
Getting more videos...
Videos Retrieved: 400
Getting more videos...
Videos Retrieved: 500
Getting more videos...
Videos Retrieved: 600
Getting more videos...
Videos Retrieved: 700
Getting more videos...
Videos Retrieved: 800
Getting more videos...
Videos Retrieved: 900
Getting more videos...
Videos Retrieved: 1000
Getting more videos...
Videos Retrieved: 1002
Found all the videos.
```

</details>


#### More to the playlists

You can directly instantiate the `Playlist` class as follows to access its information & videos in the `info` and `videos` fields respectively.

YouTube offers only 100 videos in a single request, for getting more videos present in the playlist, you can check `hasMoreVideos` bool to see if playlist contains more videos.
If playlist has more videos, then you can call `getNextVideos` to fetch more videos.

Example below demonstrates a simple way to retrive all videos of a playlist.

```python
playlist = Playlist('https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK')
while playlist.hasMoreVideos:
    print('Getting more videos...')
    await playlist.getNextVideos()
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
from youtubesearchpython.__future__ import Suggestions

suggestions = await Suggestions.get('NoCopyrightSounds', language = 'en', region = 'US')

print(suggestions)
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
from youtubesearchpython.__future__ import Hashtag

hashtag = Hashtag('ncs', limit = 1)
result = await hashtag.next()

print(result)
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

#### Getting direct stream URL of a video

This class is able fetch video URLs without any additional web requests (that's fast), as one might already have same response at the time of showing it to the user.

For making use of this functionality, you must install [yt-dlp](https://github.com/yt-dlp/yt-dlp) as a dependency.
StreamURLFetcher makes slight improvements & changes to YouTube class from [yt-dlp](https://github.com/yt-dlp/yt-dlp).

```py
from youtubesearchpython.__future__ import *
fetcher = StreamURLFetcher()
''' It is recommended to call this method only once & avoid reinstantiating this class '''
await fetcher.getJavaScript()
video = await Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
url = await fetcher.get(video, 251)
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

#### Get comments of a video
You can use a Comments class for that.
```python
from youtubesearchpython.__future__ import *

# You can either pass an ID or a URL
video_id = "_ZdsmLgCVdU"
comments = Comments(video_id)

while comments.hasMoreComments:
    print('Getting more comments...')
    await comments.getNextComments()
    print(len(comments.comments["result"]))

print('Found all the comments.')
```

<details>
 <summary> Example Result</summary>

```bash
Getting more comments...
20
Getting more comments...
40
Getting more comments...
60
Getting more comments...
80
Getting more comments...
100
Getting more comments...
...
```

</details>

#### Get first 20 comments of a video
You can use a Comments.get method for that.
```python
from youtubesearchpython.__future__ import *

# You can either pass an ID or a URL
video_id = "_ZdsmLgCVdU"
comments = await Comments.get(video_id)

print(comments)
```

<details>
 <summary> Example Result</summary>

```bash
{
   "result":[
      {
         "id":"Ugh2UTT69BnjaHgCoAEC",
         "author":{
            "id":"UCBykgwvHh2SX5HH7dVWLkqQ",
            "name":"Daikaiju Danielle",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSC8WrgmUHF5l6DYEb8jabim9nE0Ko1vQ_KFOly0w=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSC8WrgmUHF5l6DYEb8jabim9nE0Ko1vQ_KFOly0w=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSC8WrgmUHF5l6DYEb8jabim9nE0Ko1vQ_KFOly0w=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"The boy probably represents youth and the pure, free spirit of being young. When you grow up, it's hard to find that spirit again. You have to search for it.",
         "published":"5 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"5.9K",
            "label":"5.9K likes"
         },
         "replyCount":81
      },
      {
         "id":"UgzyjWeS_wVmoVrcyVZ4AaABAg",
         "author":{
            "id":"UCMMJk2iiIanIFtTwnLK8XBA",
            "name":"naomi",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/wzrS0agEf0NBFXvcpQJFF-6BwdciRFqzVf_dmgv4Unk7e9AFA7Sb7K7hsLeXdZsOX26J0J4Y=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/wzrS0agEf0NBFXvcpQJFF-6BwdciRFqzVf_dmgv4Unk7e9AFA7Sb7K7hsLeXdZsOX26J0J4Y=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/wzrS0agEf0NBFXvcpQJFF-6BwdciRFqzVf_dmgv4Unk7e9AFA7Sb7K7hsLeXdZsOX26J0J4Y=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"Strange that I showed this to my brother three days before his death not knowing I would soon relate to it.",
         "published":"1 year ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"5.2K",
            "label":"5.2K likes"
         },
         "replyCount":147
      },
      {
         "id":"UgyP3NpP-qA9T80YRVh4AaABAg",
         "author":{
            "id":"UCCekImfpPQw94ZHeQy98S_A",
            "name":"Noura",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSA9_Di2v12v_MycDkKjvhD8D3dRSt9pyZIcCekeg=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSA9_Di2v12v_MycDkKjvhD8D3dRSt9pyZIcCekeg=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSA9_Di2v12v_MycDkKjvhD8D3dRSt9pyZIcCekeg=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"In Arabic when we want to express how much we love and cherish someone we say \"you are my eyes\".. And for some reason that line \"don\\'t you know you got my eyes\" makes me really nostalgic and sad.",
         "published":"1 year ago (edited)",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"3.8K",
            "label":"3.8K likes"
         },
         "replyCount":65
      },
      {
         "id":"Ugy-JqQw3w3MXwxGZHZ4AaABAg",
         "author":{
            "id":"UC6irqN4Fk_z-CdK47pkLTgQ",
            "name":"Leo Trombetta",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTogXyBXEX1LAzehhiYyx9amCWGkcMRCaa3e-pEgg=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTogXyBXEX1LAzehhiYyx9amCWGkcMRCaa3e-pEgg=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTogXyBXEX1LAzehhiYyx9amCWGkcMRCaa3e-pEgg=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"As a mother whose had to let her son go for his life to be better, this song is about exactly that. The pain and sacrifice and love and the warm memories you pray they will have of the sweetest moments you've shared when you held them so long ago.. I miss you.",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"2K",
            "label":"2K likes"
         },
         "replyCount":23
      },
      {
         "id":"Ugwv8lwT4LS906Y9P1p4AaABAg",
         "author":{
            "id":"UClMs_LKpgCPC9acJQpGRcbQ",
            "name":"Arundhati",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTHadgrB-BvJ2zqtN9_f2ttscQEH0Sc3awtvg73ug=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTHadgrB-BvJ2zqtN9_f2ttscQEH0Sc3awtvg73ug=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTHadgrB-BvJ2zqtN9_f2ttscQEH0Sc3awtvg73ug=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"It’s been 3 years and I still can’t sing that chorus without tearing up",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"1K",
            "label":"1K likes"
         },
         "replyCount":16
      },
      {
         "id":"Ugx5NiWjHQI1aGWI8ex4AaABAg",
         "author":{
            "id":"UCeuMECoMfhC9Fyn5veduj1w",
            "name":"dona nova",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQC9P35p4nKLBaoDkWwsGjQCVrrBs_lPVCNsTQ5oPg=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQC9P35p4nKLBaoDkWwsGjQCVrrBs_lPVCNsTQ5oPg=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQC9P35p4nKLBaoDkWwsGjQCVrrBs_lPVCNsTQ5oPg=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"My dad passed away in 2012 and now he communicates to me sometimes through songs. If I ask him a question the next song I hear will have the answer. This year I had to start my life over completely and I have moved across the country away from a toxic person, and then I moved again from the next place I lived from another toxic person, all during the pandemic. I am also legally blind and otherwise disabled so I worried about how I would make it on my own  after my  losses and divorce. I don't know anybody here and I'm completely alone. This comes after 10 years of loss and change that started with his death. Anyway, When I asked him how could I ever have a life again he sent me this song. He always does. I have been told he is my spirit guide and I can tell when he's here. I love glass animals",
         "published":"1 year ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"1.6K",
            "label":"1.6K likes"
         },
         "replyCount":72
      },
      {
         "id":"UgyHLTfBhMAh39IcPAp4AaABAg",
         "author":{
            "id":"UCK8evpEndlyLgjcXTYfOVtQ",
            "name":"UnforgettableAlice",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSlrVENCyh_Wk6p8UrZAPEIS3pmUnGOiTb2zwIx1g=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSlrVENCyh_Wk6p8UrZAPEIS3pmUnGOiTb2zwIx1g=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSlrVENCyh_Wk6p8UrZAPEIS3pmUnGOiTb2zwIx1g=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"Vocalist/guitarist Dave Bayley explained the story behind this song to Paste magazine: \"The idea for this one came from a story someone told me once. They were telling me about their child, and something awful had happened to them. She was crying - but at the same time the memories that they had from that previous life made her so happy - so she was also smiling. That combination of emotions kind of made me feel like my heart was being ripped apart but also optimistic in a weird way. She had found a way to see happiness in this awful thing that had happened to her. That combination of emotions is what this song is getting at.\"",
         "published":"3 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"5.6K",
            "label":"5.6K likes"
         },
         "replyCount":31
      },
      {
         "id":"Ugwq4Hc5dcjphfdabi14AaABAg",
         "author":{
            "id":"UChtQ0Lhb3UvlSjPJ_1gcRdQ",
            "name":"Later",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTmkn0CgPeiW8hmoP3VEokLg-AN2Y7xkTz7HeOa1w=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTmkn0CgPeiW8hmoP3VEokLg-AN2Y7xkTz7HeOa1w=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLTmkn0CgPeiW8hmoP3VEokLg-AN2Y7xkTz7HeOa1w=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"\"Don\\'t you know you got my eyes\"",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"3.3K",
            "label":"3.3K likes"
         },
         "replyCount":19
      },
      {
         "id":"UgxC1mFXH9ddTB6qa5h4AaABAg",
         "author":{
            "id":"UC8iw4k1Ojbd5QsK35IeT5mg",
            "name":"Anna Dunne",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSzwmG3DSiHB8XuKUqe6CjdlbSPuln1e1kOKS7i6w=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSzwmG3DSiHB8XuKUqe6CjdlbSPuln1e1kOKS7i6w=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSzwmG3DSiHB8XuKUqe6CjdlbSPuln1e1kOKS7i6w=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I lost my little sons to the care system because i had depression and experienced domestic abuse. I see them now sometimes. It doesn't get any easier and I miss them a lot. <3 This song means a lot. ",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"1.9K",
            "label":"1.9K likes"
         },
         "replyCount":25
      },
      {
         "id":"Ugw4ux8km05TQ3kGHmV4AaABAg",
         "author":{
            "id":"UCfqMzgWyCUuUWBBaD4WgynA",
            "name":"Jemma Scott",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLT44n2_05S_bMU2ME_Z1WSk6xTIJ3cs82vSF920pg=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLT44n2_05S_bMU2ME_Z1WSk6xTIJ3cs82vSF920pg=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLT44n2_05S_bMU2ME_Z1WSk6xTIJ3cs82vSF920pg=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"Warning ⚠️: ",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"2.1K",
            "label":"2.1K likes"
         },
         "replyCount":5
      },
      {
         "id":"Ugy5hJrVHhrZ25VZoDd4AaABAg",
         "author":{
            "id":"UCCooCkWoIN-QmHrVo0t5d9Q",
            "name":"Samy Lind",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSHCXYVj0EyiLYxeBvhP6E4gnS1gRzDSYleBQ=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSHCXYVj0EyiLYxeBvhP6E4gnS1gRzDSYleBQ=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSHCXYVj0EyiLYxeBvhP6E4gnS1gRzDSYleBQ=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I know no one cares about stuff like this but I just wanted to speak on the power of art because it’s beautiful. This video and this entire album has been a huge catalyst and help in me saving myself and my family. I was forcing my husband and 3 kids to live with my abusive parents so that I could try to make them love us before they died. All they did was hurt us more and instead of dealing with it I kept staying there and started doing pain pills. This video helped hit home how much I don’t need my parents and it made me never want to escape from my reality again. I hadn’t quite gotten to a stage of disgust, but I sure have done a lot of regrettable things. This album helps me have the strength to keep doing my best to learn to be better and to learn to be the best I can be for my kids. I don’t want to be held back by anything anymore and I don’t want to hold back my family. Thank you glass animal and crew:) your saving lives with this music",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"493",
            "label":"493 likes"
         },
         "replyCount":7
      },
      {
         "id":"UgyfG6DRZQZe5NtvY9t4AaABAg",
         "author":{
            "id":"UCFlsa-V7ZjC3SJG1MgHeTxA",
            "name":"Adi ☆",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/2r2ZQYcZaViZp8n37bmAnJx-irYy7mOUkpkC7nprEaoeSY2jEJ9wQ-kQnpxN6Z4WMWFMT9JzUw=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/2r2ZQYcZaViZp8n37bmAnJx-irYy7mOUkpkC7nprEaoeSY2jEJ9wQ-kQnpxN6Z4WMWFMT9JzUw=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/2r2ZQYcZaViZp8n37bmAnJx-irYy7mOUkpkC7nprEaoeSY2jEJ9wQ-kQnpxN6Z4WMWFMT9JzUw=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"Lyrics:[Verse 1]",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"955",
            "label":"955 likes"
         },
         "replyCount":9
      },
      {
         "id":"Ugi30kIt00U573gCoAEC",
         "author":{
            "id":"UCZbJ_Q3ClurxYlthgTecgow",
            "name":"love, doggo",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/IJF61exnEIJZDlnphGN9yXnV_fQSJhdAyPqgF_e3pJ42iwvTQprgQaty-uVyvjiMJpnaekxeBg=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/IJF61exnEIJZDlnphGN9yXnV_fQSJhdAyPqgF_e3pJ42iwvTQprgQaty-uVyvjiMJpnaekxeBg=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/IJF61exnEIJZDlnphGN9yXnV_fQSJhdAyPqgF_e3pJ42iwvTQprgQaty-uVyvjiMJpnaekxeBg=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"This is a rare thing... I like every song a band makes",
         "published":"5 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"3.9K",
            "label":"3.9K likes"
         },
         "replyCount":67
      },
      {
         "id":"UgzDNmCLzmkNIGV_iB14AaABAg",
         "author":{
            "id":"UCrdOXfYndK2UEjAKRg-hUcw",
            "name":"Cherry",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/oRPZKN6SL1SoMc5J7FQIHiA1C1wQZe1YfRHbkxaLnNp9Vi7Vl2PCY11oTK5mDms-NHXSGqFsKQ=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/oRPZKN6SL1SoMc5J7FQIHiA1C1wQZe1YfRHbkxaLnNp9Vi7Vl2PCY11oTK5mDms-NHXSGqFsKQ=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/oRPZKN6SL1SoMc5J7FQIHiA1C1wQZe1YfRHbkxaLnNp9Vi7Vl2PCY11oTK5mDms-NHXSGqFsKQ=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I hope the mother who inspired this can hear it and feel her child close to her again.",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"410",
            "label":"410 likes"
         },
         "replyCount":1
      },
      {
         "id":"UgyQEih224ElUkT2AXl4AaABAg",
         "author":{
            "id":"UC7M3_B55yIvo4DZS3BvgA1g",
            "name":"Sirce Guevara",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRJhxg_aeXmbGuH8wbuCcGWVtRs6tFKPqkxw4-lcJ8=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRJhxg_aeXmbGuH8wbuCcGWVtRs6tFKPqkxw4-lcJ8=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRJhxg_aeXmbGuH8wbuCcGWVtRs6tFKPqkxw4-lcJ8=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I cried watching this video, this is my first time seeing it.. It just reminded me of my mother,  how she raised me alone.  Seeing me happy and dancing all her life . How she works hard day by day just so I have a roof on my head and food on the table. She's amazing...",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"271",
            "label":"271 likes"
         },
         "replyCount":1
      },
      {
         "id":"UgxSKtnwJ1fL1cGECFN4AaABAg",
         "author":{
            "id":"UCaWu5P4tl4leNsq0d6K5JfA",
            "name":"Brylee D",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSnWU59WluXZehM5VxmcbX6Unk_rgJc699gUp7lxw=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSnWU59WluXZehM5VxmcbX6Unk_rgJc699gUp7lxw=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSnWU59WluXZehM5VxmcbX6Unk_rgJc699gUp7lxw=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I have a crush on that background wind instrument",
         "published":"2 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"4.5K",
            "label":"4.5K likes"
         },
         "replyCount":36
      },
      {
         "id":"Ugx885faaugZ-KS2ht14AaABAg",
         "author":{
            "id":"UCAv-kFdFs9zZX4IR9y77sTg",
            "name":"berry tart subs ✿",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/RIEhlWERKQrY6oscMFEVW9pyDVKwndKkfFfnMTGxJIFHV2np4asu1syE-C016cZlcgZYtkdvrCA=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/RIEhlWERKQrY6oscMFEVW9pyDVKwndKkfFfnMTGxJIFHV2np4asu1syE-C016cZlcgZYtkdvrCA=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/RIEhlWERKQrY6oscMFEVW9pyDVKwndKkfFfnMTGxJIFHV2np4asu1syE-C016cZlcgZYtkdvrCA=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"This song literally makes me cry every time I hear it it's just so sweet",
         "published":"1 year ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"73",
            "label":"73 likes"
         },
         "replyCount":1
      },
      {
         "id":"UgxfMf3PW8muQIKHeX54AaABAg",
         "author":{
            "id":"UCs5_3PBRo9VoCCbDWDMpa-g",
            "name":"Victor Rodriguez",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRe_mumWc8G4a9DvzNQ7FBA_hctTvwTJskAdw=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRe_mumWc8G4a9DvzNQ7FBA_hctTvwTJskAdw=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLRe_mumWc8G4a9DvzNQ7FBA_hctTvwTJskAdw=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"I hope my son can find some type of solace or message in this song one day. We lost his mother my wife when she passed suddenly three months ago at 23 years young. He was only 2 years old and 7 months when it happened. It was a short time for him but so many happy memories. They spent every single hour of every single day together. We’re so lost and devasted without you, We love you Deja C Rodriguez",
         "published":"8 months ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"126",
            "label":"126 likes"
         },
         "replyCount":2
      },
      {
         "id":"UgiuS-ehhcqhHXgCoAEC",
         "author":{
            "id":"UCd6gX2dxkokyH70cbUocq7Q",
            "name":"bunnyluveable",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSt6NFUcOAfGB1C0BL0f18q8sPUX0UQBhYV_A=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSt6NFUcOAfGB1C0BL0f18q8sPUX0UQBhYV_A=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLSt6NFUcOAfGB1C0BL0f18q8sPUX0UQBhYV_A=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"their music is like being wrapped in a warm blanket on a chilly day.",
         "published":"5 years ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"563",
            "label":"563 likes"
         },
         "replyCount":6
      },
      {
         "id":"UgwEdhuY0RUuiyBqpVN4AaABAg",
         "author":{
            "id":"UC8GIfeF1UytnIdBUx7eODBg",
            "name":"TheBnjmnMiles",
            "thumbnails":[
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQjQG6jvrGnj9ejtjfO-pbXWwekST4e_qxK=s48-c-k-c0x00ffffff-no-rj",
                  "width":48,
                  "height":48
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQjQG6jvrGnj9ejtjfO-pbXWwekST4e_qxK=s88-c-k-c0x00ffffff-no-rj",
                  "width":88,
                  "height":88
               },
               {
                  "url":"https://yt3.ggpht.com/ytc/AKedOLQjQG6jvrGnj9ejtjfO-pbXWwekST4e_qxK=s176-c-k-c0x00ffffff-no-rj",
                  "width":176,
                  "height":176
               }
            ]
         },
         "content":"Why is nobody talking about this kid’s freakin’ sweet dance moves?",
         "published":"7 months ago",
         "isLiked":false,
         "authorIsChannelOwner":false,
         "voteStatus":"INDIFFERENT",
         "votes":{
            "simpleText":"210",
            "label":"210 likes"
         },
         "replyCount":4
      }
   ]
}
```

</details>

#### Retrieve video transcript
YouTube auto-generates transcripts (subtitles) for videos. You can retrieve those transcripts using Transcript class:
```py
from youtubesearchpython.__future__ import Transcript

print(await Transcript.get("https://www.youtube.com/watch?v=-1xu0IP35FI"))
```

In response, you'll get available languages with `params` parameter. If you want to retrieve a different language, you have to pass the function that parameter. Example:
```py
from youtubesearchpython.__future__ import Transcript

url = "https://www.youtube.com/watch?v=-1xu0IP35FI"

transcript_en = await Transcript.get(url)
# you actually don't have to pass a valid URL in following Transcript call. You can input an empty string, but I do recommend still inputing a valid URL.
transcript_2 = await Transcript.get(url, transcript_en["languages"][-1]["params"]) # in my case, it'd output Spanish.
print(transcript_2)
```

<details>
 <summary> Example Result</summary>

```json
{
   "segments":[
      {
         "startMs":"210",
         "endMs":"2129",
         "text":"- When Steve Jobs unveiled the original",
         "startTime":"0:00"
      },
      {
         "startMs":"2130",
         "endMs":"3670",
         "text":"iPhone back in 2007,",
         "startTime":"0:02"
      },
      {
         "startMs":"3670",
         "endMs":"4940",
         "text":"the year I graduated high school,",
         "startTime":"0:03"
      },
      {
         "startMs":"4940",
         "endMs":"7610",
         "text":"he pitched it as a music player, a phone,",
         "startTime":"0:04"
      },
      {
         "startMs":"7610",
         "endMs":"10760",
         "text":"and an internet communicator\nall rolled into one.",
         "startTime":"0:07"
      },
      {
         "startMs":"10760",
         "endMs":"11593",
         "text":"- Are you getting it?",
         "startTime":"0:10"
      },
      ...
   ],
   "languages":[
      {
         "params":"CgstMXh1MElQMzVGSRIOQ2dBU0FtVnVHZ0ElM0QYASozZW5nYWdlbWVudC1wYW5lbC1zZWFyY2hhYmxlLXRyYW5zY3JpcHQtc2VhcmNoLXBhbmVsMAE%3D",
         "selected":true,
         "title":"English"
      },
      {
         "params":"CgstMXh1MElQMzVGSRISQ2dOaGMzSVNBbVZ1R2dBJTNEGAEqM2VuZ2FnZW1lbnQtcGFuZWwtc2VhcmNoYWJsZS10cmFuc2NyaXB0LXNlYXJjaC1wYW5lbDAB",
         "selected":false,
         "title":"English (auto-generated)"
      },
      {
         "params":"CgstMXh1MElQMzVGSRISQ2dBU0JYQjBMVUpTR2dBJTNEGAEqM2VuZ2FnZW1lbnQtcGFuZWwtc2VhcmNoYWJsZS10cmFuc2NyaXB0LXNlYXJjaC1wYW5lbDAB",
         "selected":false,
         "title":"Portuguese (Brazil)"
      },
      {
         "params":"CgstMXh1MElQMzVGSRIQQ2dBU0JtVnpMVFF4T1JvQRgBKjNlbmdhZ2VtZW50LXBhbmVsLXNlYXJjaGFibGUtdHJhbnNjcmlwdC1zZWFyY2gtcGFuZWwwAQ%3D%3D",
         "selected":false,
         "title":"Spanish (Latin America)"
      }
   ]
}
```
</details>


#### Retrieve channel info
```py
from youtubesearchpython.__future__ import Channel

print(await Channel.get("UC_aEa8K-EOJ3D6gOs7HcyNg"))
```

<details>
 <summary> Example Result</summary>

```json
{
    "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
    "url": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg",
    "description": "NoCopyrightSounds is a copyright free / stream safe record label, providing free to use music to the content creator community. \n\nWe work with artists from around the world in electronic music, representing genres from House to Dubstep via Trap, Drum & Bass, Electro Pop and more. \n\nNCS Music is free to use for independent Creators and their UGC (User Generated Content) on YouTube & Twitch - always remember to credit the Artist, track and NCS and link back to our original NCS upload.\n\nView our usage policy and some frequently asked questions here: http://ncs.io/UsagePolicy\n\nGrab our new apparel range here: http://ncs.io/Store",
    "title": "NoCopyrightSounds",
    "banners": [
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 1060,
            "height": 175
        },
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 1138,
            "height": 188
        },
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w1707-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 1707,
            "height": 283
        },
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w2120-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 2120,
            "height": 351
        },
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w2276-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 2276,
            "height": 377
        },
        {
            "url": "https://yt3.ggpht.com/ZdXDhvCVn73Shu-QkqWFoUS_TlZ9MSkAXb8VJBeI6ZKSN6oH4QBvTG2BCfuFRegjXwdp6qH3=w2560-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            "width": 2560,
            "height": 424
        }
    ],
    "subscribers": {
        "simpleText": "32.2M subscribers",
        "label": "32.2 million subscribers"
    },
    "thumbnails": [
        {
            "url": "https://yt3.ggpht.com/YIBi8NVC87fMfJHfQ2O0dyzjis7tUlO7VqWLhk1lq1fkIOQTrpX_Ip7G6S_u0IJosXYSe_Z9=s48-c-k-c0x00ffffff-no-rj",
            "width": 48,
            "height": 48
        },
        {
            "url": "https://yt3.ggpht.com/YIBi8NVC87fMfJHfQ2O0dyzjis7tUlO7VqWLhk1lq1fkIOQTrpX_Ip7G6S_u0IJosXYSe_Z9=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
        },
        {
            "url": "https://yt3.ggpht.com/YIBi8NVC87fMfJHfQ2O0dyzjis7tUlO7VqWLhk1lq1fkIOQTrpX_Ip7G6S_u0IJosXYSe_Z9=s176-c-k-c0x00ffffff-no-rj",
            "width": 176,
            "height": 176
        },
        {
            "url": "https://yt3.ggpht.com/YIBi8NVC87fMfJHfQ2O0dyzjis7tUlO7VqWLhk1lq1fkIOQTrpX_Ip7G6S_u0IJosXYSe_Z9=s900-c-k-c0x00ffffff-no-rj",
            "width": 900,
            "height": 900
        },
        {
            "url": "https://yt3.ggpht.com/YIBi8NVC87fMfJHfQ2O0dyzjis7tUlO7VqWLhk1lq1fkIOQTrpX_Ip7G6S_u0IJosXYSe_Z9=s200-c-k-c0x00ffffff-no-rj?days_since_epoch=19098",
            "width": 200,
            "height": 200
        }
    ],
    "isFamilySafe": true,
    "keywords": "NoCopyrightSounds ncs no copyright sounds copyrighted music free royalty royaltyfree uncopyrighted copyrightfree",
    "tags": [
        "NoCopyrightSounds",
        "ncs",
        "no",
        "copyright",
        "sounds",
        "copyrighted",
        "music",
        "free",
        "royalty",
        "royaltyfree",
        "uncopyrighted",
        "copyrightfree"
    ],
    "views": "10,094,707,992 views",
    "joinedDate": "Aug 14, 2011",
    "country": "United Kingdom"
}
```
</details>

#### Retrieve channel playlists
```py
from youtubesearchpython.__future__ import Channel

channel = Channel("UC_aEa8K-EOJ3D6gOs7HcyNg")
await channel.init()
print(len(channel.result["playlists"]))
while channel.has_more_playlists():
    await channel.next()
    print(len(channel.result["playlists"]))
```

<details>
 <summary> Example Result</summary>

```
30
49
```
</details>

## Dependencies

- Thanks to [Encode](https://github.com/encode) for [httpx](https://github.com/encode/httpx).

## License

MIT
