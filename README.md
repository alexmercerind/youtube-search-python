# youtube-search-python


**Search videos in YouTube WITHOUT using YouTube Data API v3.**


(Made from scratch without using YouTube Data API v3 and any other third party library!)


Working as of 2020.


## :arrow_down: Install


```
pip3 install youtube-search-python

Alternatively you can clone the repo, and run "Usage Example.py"
```


## :triangular_ruler: Usage


```python

from youtubesearchpython import searchYoutube

search = searchYoutube("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)

print(search.result())

```


## :heart: Like the module?


Consider starring the repo. Feel free to use.


## :heavy_check_mark: Current Progress


Currently search result returns:


- [x] Video Link
- [x] Video Title
- [x] Channel Name
- [x] Video Duration
- [x] Video View Count
- [x] Video ID
- [x] Video Thumbnails


## :camera: Screenshot


![Image description](https://github.com/alexmercerind/youtube-search-python/blob/master/youtube-search-python.PNG)


## :page_with_curl: Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "id": "RQ5IkSeMQbc",
            "link": "https://www.youtube.com/watch?v=RQ5IkSeMQbc",
            "title": "Teyeq - Demons [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:35",
            "views": 321971,
            "thumbnails": [
                "https://img.youtube.com/vi/RQ5IkSeMQbc/default.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/hqdefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/mqdefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/sddefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/maxresdefault.jpg"
            ]
        },
        {
            "index": 1,
            "id": "CnekLFazlxo",
            "link": "https://www.youtube.com/watch?v=CnekLFazlxo",
            "title": "Wanden \\\\u0026 Slashtaq - Better Off [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:18",
            "views": 455287,
            "thumbnails": [
                "https://img.youtube.com/vi/CnekLFazlxo/default.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/hqdefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/mqdefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/sddefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/maxresdefault.jpg"
            ]
        },
        {
            "index": 2,
            "id": "BG_W8Z74nG8",
            "link": "https://www.youtube.com/watch?v=BG_W8Z74nG8",
            "title": "Jim Yosef - Fall With Me [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:49",
            "views": 819877,
            "thumbnails": [
                "https://img.youtube.com/vi/BG_W8Z74nG8/default.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/hqdefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/mqdefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/sddefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/maxresdefault.jpg"
            ]
        },
        {
            "index": 3,
            "id": "ZQHcERGiinM",
            "link": "https://www.youtube.com/watch?v=ZQHcERGiinM",
            "title": "Dark Heart - Crash Test Dummy [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:42",
            "views": 627903,
            "thumbnails": [
                "https://img.youtube.com/vi/ZQHcERGiinM/default.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/hqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/mqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/sddefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/maxresdefault.jpg"
            ]
        },
        {
            "index": 4,
            "id": "2W3Y9KMgNw0",
            "link": "https://www.youtube.com/watch?v=2W3Y9KMgNw0",
            "title": "Brook Xiao - Fire (ft. Rachel Horter) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:54",
            "views": 689570,
            "thumbnails": [
                "https://img.youtube.com/vi/2W3Y9KMgNw0/default.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/hqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/mqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/sddefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/maxresdefault.jpg"
            ]
        },
        {
            "index": 5,
            "id": "SxfSpqFWJAg",
            "link": "https://www.youtube.com/watch?v=SxfSpqFWJAg",
            "title": "Arlow - Freefall [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:16",
            "views": 891472,
            "thumbnails": [
                "https://img.youtube.com/vi/SxfSpqFWJAg/default.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/hqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/mqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/sddefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/maxresdefault.jpg"
            ]
        },
        {
            "index": 6,
            "id": "vIE6cuAhR4o",
            "link": "https://www.youtube.com/watch?v=vIE6cuAhR4o",
            "title": "Facading - Walk Away [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:19",
            "views": 806660,
            "thumbnails": [
                "https://img.youtube.com/vi/vIE6cuAhR4o/default.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/hqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/mqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/sddefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/maxresdefault.jpg"
            ]
        },
        {
            "index": 7,
            "id": "1hxGuyfAErQ",
            "link": "https://www.youtube.com/watch?v=1hxGuyfAErQ",
            "title": "BH - Holding On [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:57",
            "views": 894190,
            "thumbnails": [
                "https://img.youtube.com/vi/1hxGuyfAErQ/default.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/hqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/mqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/sddefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 8,
            "id": "klTBagBYXpk",
            "link": "https://www.youtube.com/watch?v=klTBagBYXpk",
            "title": "RudeLies \\\\u0026 Clarx - Erase [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:53",
            "views": 1049372,
            "thumbnails": [
                "https://img.youtube.com/vi/klTBagBYXpk/default.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/hqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/mqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/sddefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/maxresdefault.jpg"
            ]
        },
        {
            "index": 9,
            "id": "TeSiiKpbCiM",
            "link": "https://www.youtube.com/watch?v=TeSiiKpbCiM",
            "title": "Heuse \\\\u0026 Caravn - Spirits Say [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:47",
            "views": 890127,
            "thumbnails": [
                "https://img.youtube.com/vi/TeSiiKpbCiM/default.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/hqdefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/mqdefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/sddefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/maxresdefault.jpg"
            ]
        },
        {
            "index": 10,
            "id": "K4DyBUG242c",
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On \\\\u0026 On (feat. Daniel Levi) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 357410023,
            "thumbnails": [
                "https://img.youtube.com/vi/K4DyBUG242c/default.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/hqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/mqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/sddefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/maxresdefault.jpg"
            ]
        },
        {
            "index": 11,
            "id": "yJg-Y5byMMw",
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:50",
            "views": 127760126,
            "thumbnails": [
                "https://img.youtube.com/vi/yJg-Y5byMMw/default.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/hqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/mqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/sddefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/maxresdefault.jpg"
            ]
        },
        {
            "index": 12,
            "id": "EpRJY-hI6Bs",
            "link": "https://www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji",
            "channel": "Monster Boy Music",
            "duration": "15:17",
            "views": 10556704,
            "thumbnails": [
                "https://img.youtube.com/vi/EpRJY-hI6Bs/default.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/hqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/mqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/sddefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/maxresdefault.jpg"
            ]
        },
        {
            "index": 13,
            "id": "-ObdvMkCKws",
            "link": "https://www.youtube.com/watch?v=-ObdvMkCKws",
            "title": "Top 20 Most Popular Songs by NCS | Best of NCS | Most Viewed Songs",
            "channel": "Music Store",
            "duration": "1:12:47",
            "views": 12521694,
            "thumbnails": [
                "https://img.youtube.com/vi/-ObdvMkCKws/default.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/hqdefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/mqdefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/sddefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/maxresdefault.jpg"
            ]
        },
        {
            "index": 14,
            "id": "QglaLzo_aPk",
            "link": "https://www.youtube.com/watch?v=QglaLzo_aPk",
            "title": "Julius Dreisig \\\\u0026 Zeus X Crona - Invisible [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:22",
            "views": 65222602,
            "thumbnails": [
                "https://img.youtube.com/vi/QglaLzo_aPk/default.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/hqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/mqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/sddefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/maxresdefault.jpg"
            ]
        },
        {
            "index": 15,
            "id": "CLiXUT3MS34",
            "link": "https://www.youtube.com/watch?v=CLiXUT3MS34",
            "title": "Heuse \\\\u0026 Zeus x Crona - Pill (feat. Emma Sameth) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:16",
            "views": 28107026,
            "thumbnails": [
                "https://img.youtube.com/vi/CLiXUT3MS34/default.jpg",
                "https://img.youtube.com/vi/CLiXUT3MS34/hqdefault.jpg",
                "https://img.youtube.com/vi/CLiXUT3MS34/mqdefault.jpg",
                "https://img.youtube.com/vi/CLiXUT3MS34/sddefault.jpg",
                "https://img.youtube.com/vi/CLiXUT3MS34/maxresdefault.jpg"
            ]
        },
        {
            "index": 16,
            "id": "_XspQUK22-U",
            "link": "https://www.youtube.com/watch?v=_XspQUK22-U",
            "title": "Diamond Eyes - Everything [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:28",
            "views": 25148753,
            "thumbnails": [
                "https://img.youtube.com/vi/_XspQUK22-U/default.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/hqdefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/mqdefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/sddefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/maxresdefault.jpg"
            ]
        },
        {
            "index": 17,
            "id": "bLZHcnuqscU",
            "link": "https://www.youtube.com/watch?v=bLZHcnuqscU",
            "title": "Unknown Brain x Rival - Control (feat. Jex) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:47",
            "views": 28897461,
            "thumbnails": [
                "https://img.youtube.com/vi/bLZHcnuqscU/default.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/hqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/mqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/sddefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/maxresdefault.jpg"
            ]
        },
        {
            "index": 18,
            "id": "u1I9ITfzqFs",
            "link": "https://www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:24",
            "views": 45159724,
            "thumbnails": [
                "https://img.youtube.com/vi/u1I9ITfzqFs/default.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/hqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/mqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/sddefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/maxresdefault.jpg"
            ]
        },
        {
            "index": 19,
            "id": "L7kF4MXXCoA",
            "link": "https://www.youtube.com/watch?v=L7kF4MXXCoA",
            "title": "Lost Sky - Dreams pt. II (feat. Sara Skinner) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:36",
            "views": 33748099,
            "thumbnails": [
                "https://img.youtube.com/vi/L7kF4MXXCoA/default.jpg",
                "https://img.youtube.com/vi/L7kF4MXXCoA/hqdefault.jpg",
                "https://img.youtube.com/vi/L7kF4MXXCoA/mqdefault.jpg",
                "https://img.youtube.com/vi/L7kF4MXXCoA/sddefault.jpg",
                "https://img.youtube.com/vi/L7kF4MXXCoA/maxresdefault.jpg"
            ]
        },
        {
            "index": 20,
            "id": "CLEWmT_8ppM",
            "link": "https://www.youtube.com/watch?v=CLEWmT_8ppM",
            "title": "Clarx - Zig Zag [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 9641714,
            "thumbnails": [
                "https://img.youtube.com/vi/CLEWmT_8ppM/default.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/hqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/mqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/sddefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/maxresdefault.jpg"
            ]
        }
    ]
}
```
