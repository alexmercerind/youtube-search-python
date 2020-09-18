# [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)


**Search for videos and playlists in YouTube WITHOUT YouTube Data API v3.**


Made without using YouTube Data API v3 and any other third party library.

This library is intended for personal and non-commercial usage only.


Working as of 2020.


## Install


###### Supports both Python 3 & Python 2
```bash
pip install youtube-search-python
```
###### Alternatively you can clone the repo, and run "Usage Example.py"


## Usage


###### Search for Videos

```python

from youtubesearchpython import SearchVideos

search = SearchVideos("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)

print(search.result())

```

###### Search for Playlists

```python

from youtubesearchpython import SearchPlaylists

search = SearchPlaylists("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)

print(search.result())

```


## Like the module?


Consider starring the repository. Feel free to use.

It takes a lot of time to deal with the changes that YouTube makes time to time.

Feel free to open issue, in case you find one.


## Current Progress


Currently search result returns:

- Video Link
- Video Title
- Channel Name
- Video Duration
- Video View Count
- Video ID
- Video Thumbnails
- Channel ID

(Nearly everything that YouTube offers in its search result page.)


## Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "id": "K4DyBUG242c",
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 373000758,
            "thumbnails": [
                "https://img.youtube.com/vi/K4DyBUG242c/default.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/hqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/mqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/sddefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 1,
            "id": "QyE1bu1jaDU",
            "link": "https://www.youtube.com/watch?v=QyE1bu1jaDU",
            "title": "Egzod & Wasiu - Mutiny [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:40",
            "views": 172495,
            "thumbnails": [
                "https://img.youtube.com/vi/QyE1bu1jaDU/default.jpg",
                "https://img.youtube.com/vi/QyE1bu1jaDU/hqdefault.jpg",
                "https://img.youtube.com/vi/QyE1bu1jaDU/mqdefault.jpg",
                "https://img.youtube.com/vi/QyE1bu1jaDU/sddefault.jpg",
                "https://img.youtube.com/vi/QyE1bu1jaDU/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 2,
            "id": "yJg-Y5byMMw",
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:50",
            "views": 139859586,
            "thumbnails": [
                "https://img.youtube.com/vi/yJg-Y5byMMw/default.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/hqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/mqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/sddefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 3,
            "id": "u1I9ITfzqFs",
            "link": "https://www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:24",
            "views": 47298143,
            "thumbnails": [
                "https://img.youtube.com/vi/u1I9ITfzqFs/default.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/hqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/mqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/sddefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 4,
            "id": "bLZHcnuqscU",
            "link": "https://www.youtube.com/watch?v=bLZHcnuqscU",
            "title": "Unknown Brain x Rival - Control (feat. Jex) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:47",
            "views": 34146177,
            "thumbnails": [
                "https://img.youtube.com/vi/bLZHcnuqscU/default.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/hqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/mqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/sddefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 5,
            "id": "QglaLzo_aPk",
            "link": "https://www.youtube.com/watch?v=QglaLzo_aPk",
            "title": "Julius Dreisig & Zeus X Crona - Invisible [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:22",
            "views": 77080876,
            "thumbnails": [
                "https://img.youtube.com/vi/QglaLzo_aPk/default.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/hqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/mqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/sddefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 6,
            "id": "S19UcWdOA-I",
            "link": "https://www.youtube.com/watch?v=S19UcWdOA-I",
            "title": "Lost Sky - Fearless pt.II (feat. Chris Linton) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:15",
            "views": 77813332,
            "thumbnails": [
                "https://img.youtube.com/vi/S19UcWdOA-I/default.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/hqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/mqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/sddefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 7,
            "id": "x_OwcYTNbHs",
            "link": "https://www.youtube.com/watch?v=x_OwcYTNbHs",
            "title": "Jim Yosef - Firefly [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:17",
            "views": 52762535,
            "thumbnails": [
                "https://img.youtube.com/vi/x_OwcYTNbHs/default.jpg",
                "https://img.youtube.com/vi/x_OwcYTNbHs/hqdefault.jpg",
                "https://img.youtube.com/vi/x_OwcYTNbHs/mqdefault.jpg",
                "https://img.youtube.com/vi/x_OwcYTNbHs/sddefault.jpg",
                "https://img.youtube.com/vi/x_OwcYTNbHs/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 8,
            "id": "xzyRoshFFaA",
            "link": "https://www.youtube.com/watch?v=xzyRoshFFaA",
            "title": "Fareoh - Under Water [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:46",
            "views": 10418606,
            "thumbnails": [
                "https://img.youtube.com/vi/xzyRoshFFaA/default.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/hqdefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/mqdefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/sddefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 9,
            "id": "yHLtE1wFeRQ",
            "link": "https://www.youtube.com/watch?v=yHLtE1wFeRQ",
            "title": "Jim Yosef & Anna Yvette - Linked [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:44",
            "views": 25212675,
            "thumbnails": [
                "https://img.youtube.com/vi/yHLtE1wFeRQ/default.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/hqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/mqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/sddefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 10,
            "id": "bM7SZ5SBzyY",
            "link": "https://www.youtube.com/watch?v=bM7SZ5SBzyY",
            "title": "Alan Walker - Fade [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:21",
            "views": 420168717,
            "thumbnails": [
                "https://img.youtube.com/vi/bM7SZ5SBzyY/default.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/hqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/mqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/sddefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 11,
            "id": "TW9d8vYrVFQ",
            "link": "https://www.youtube.com/watch?v=TW9d8vYrVFQ",
            "title": "Elektronomia - Sky High [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:59",
            "views": 168765821,
            "thumbnails": [
                "https://img.youtube.com/vi/TW9d8vYrVFQ/default.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/hqdefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/mqdefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/sddefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 12,
            "id": "__CRWE-L45k",
            "link": "https://www.youtube.com/watch?v=__CRWE-L45k",
            "title": "Electro-Light - Symbolism [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:52",
            "views": 173690251,
            "thumbnails": [
                "https://img.youtube.com/vi/__CRWE-L45k/default.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/hqdefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/mqdefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/sddefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 13,
            "id": "EpRJY-hI6Bs",
            "link": "https://www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji",
            "channel": "Monster Boy Music",
            "duration": "15:17",
            "views": 13121620,
            "thumbnails": [
                "https://img.youtube.com/vi/EpRJY-hI6Bs/default.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/hqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/mqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/sddefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/maxresdefault.jpg"
            ],
            "channelId": "UC2lqMWiqD-XbV9NJ6x6mj8g"
        },
        {
            "index": 14,
            "id": "ABuNwLP-z9o",
            "link": "https://www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "\ud83d\udd25 Top 50 NoCopyRightSounds | Best of NCS | Most viewed ! Gaming Music | The Best of All Time | 2020",
            "channel": "Freeme NCS Music",
            "duration": "2:59:26",
            "views": 7346545,
            "thumbnails": [
                "https://img.youtube.com/vi/ABuNwLP-z9o/default.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/hqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/mqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/sddefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/maxresdefault.jpg"
            ],
            "channelId": "UCG0SzK_t4-Ylf1yZq9Xmi_g"
        },
        {
            "index": 15,
            "id": "AOeY-nDp7hI",
            "link": "https://www.youtube.com/watch?v=AOeY-nDp7hI",
            "title": "Alan Walker - Spectre [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:47",
            "views": 269904545,
            "thumbnails": [
                "https://img.youtube.com/vi/AOeY-nDp7hI/default.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/hqdefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/mqdefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/sddefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 16,
            "id": "triXo_xCqms",
            "link": "https://www.youtube.com/watch?v=triXo_xCqms",
            "title": "TOP 100 NoCopyrightSounds | Best Of NCS | 6H NoCopyRightSounds | The Best of all time",
            "channel": "Musicbot",
            "duration": "6:17:45",
            "views": 4159975,
            "thumbnails": [
                "https://img.youtube.com/vi/triXo_xCqms/default.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/hqdefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/mqdefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/sddefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/maxresdefault.jpg"
            ],
            "channelId": "UCDsbBjIl0lYZB4IokDLyWIQ"
        },
        {
            "index": 17,
            "id": "DDOFL8IS_x0",
            "link": "https://www.youtube.com/watch?v=DDOFL8IS_x0",
            "title": "LFZ |Popsicle |Release |NoCopyRightSounds",
            "channel": "DuaSallapan",
            "duration": "4:25",
            "views": 31,
            "thumbnails": [
                "https://img.youtube.com/vi/DDOFL8IS_x0/default.jpg",
                "https://img.youtube.com/vi/DDOFL8IS_x0/hqdefault.jpg",
                "https://img.youtube.com/vi/DDOFL8IS_x0/mqdefault.jpg",
                "https://img.youtube.com/vi/DDOFL8IS_x0/sddefault.jpg",
                "https://img.youtube.com/vi/DDOFL8IS_x0/maxresdefault.jpg"
            ],
            "channelId": "UC-qLVnRkj70-f34Sk3QaYwg"
        },
        {
            "index": 18,
            "id": "3nQNiWdeH2Q",
            "link": "https://www.youtube.com/watch?v=3nQNiWdeH2Q",
            "title": "Janji - Heroes Tonight (feat. Johnning) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:29",
            "views": 209609214,
            "thumbnails": [
                "https://img.youtube.com/vi/3nQNiWdeH2Q/default.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/hqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/mqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/sddefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg"
        },
        {
            "index": 19,
            "id": "HPhHr6h4Qjc",
            "link": "https://www.youtube.com/watch?v=HPhHr6h4Qjc",
            "title": "Top 30 NoCopyrightSounds | Best of NCS | 2H NoCopyrightSounds | NCS : The Best of all time",
            "channel": "Music Store",
            "duration": "1:48:05",
            "views": 1519378,
            "thumbnails": [
                "https://img.youtube.com/vi/HPhHr6h4Qjc/default.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/hqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/mqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/sddefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/maxresdefault.jpg"
            ],
            "channelId": "UCoDZIZuadPBixSPFR7jAq2A"
        }
    ]
}
```
