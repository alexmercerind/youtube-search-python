# youtube-search-python


**Search videos in YouTube without using YouTube Data API v3.**


(Made from scratch without using YouTube Data API v3 and any other third party library!)


Working as of 2020.


## :arrow_down: Install


```pip3 install youtube-search-python```


## :triangular_ruler: Usage


```python

from youtubesearchpython import searchYoutube

search = searchYoutube("NoCopyrightSounds", 1, "json")

print(search.result());

```


## :heart: Like the module?


Consider starring the repo. Feel free to use.


## :heavy_check_mark: Current Progress


Currently search result returns:


- [x] Video Link
- [x] Video Title
- [ ] Channel Name
- [x] Video Duration
- [x] Video View Count
- [x] Video ID
- [x] Video Thumbnails
- [ ] Likes / Dislikess


## :camera: Screenshot


![Image description](https://github.com/alexmercerind/youtube-search-python/blob/master/youtube-search-python.PNG)


## :page_with_curl: Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "id": "ZQHcERGiinM",
            "link": "www.youtube.com/watch?v=ZQHcERGiinM",
            "title": "Dark Heart - Crash Test Dummy [NCS Release]",
            "duration": "2:42",
            "views": 187296,
            "thumbnails": [
                "https://img.youtube.com/vi/ZQHcERGiinM/default.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/hqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/mqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/sddefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/maxresdefault.jpg"
            ]
        },
        {
            "index": 1,
            "id": "2W3Y9KMgNw0",
            "link": "www.youtube.com/watch?v=2W3Y9KMgNw0",
            "title": "Brook Xiao - Fire (ft. Rachel Horter) [NCS Release]",
            "duration": "2:54",
            "views": 441426,
            "thumbnails": [
                "https://img.youtube.com/vi/2W3Y9KMgNw0/default.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/hqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/mqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/sddefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/maxresdefault.jpg"
            ]
        },
        {
            "index": 2,
            "id": "SxfSpqFWJAg",
            "link": "www.youtube.com/watch?v=SxfSpqFWJAg",
            "title": "Arlow - Freefall [NCS Release]",
            "duration": "3:16",
            "views": 692579,
            "thumbnails": [
                "https://img.youtube.com/vi/SxfSpqFWJAg/default.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/hqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/mqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/sddefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/maxresdefault.jpg"
            ]
        },
        {
            "index": 3,
            "id": "vIE6cuAhR4o",
            "link": "www.youtube.com/watch?v=vIE6cuAhR4o",
            "title": "Facading - Walk Away [NCS Release]",
            "duration": "3:19",
            "views": 636559,
            "thumbnails": [
                "https://img.youtube.com/vi/vIE6cuAhR4o/default.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/hqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/mqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/sddefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/maxresdefault.jpg"
            ]
        },
        {
            "index": 4,
            "id": "1hxGuyfAErQ",
            "link": "www.youtube.com/watch?v=1hxGuyfAErQ",
            "title": "BH - Holding On [NCS Release]",
            "duration": "3:57",
            "views": 692673,
            "thumbnails": [
                "https://img.youtube.com/vi/1hxGuyfAErQ/default.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/hqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/mqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/sddefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 5,
            "id": "klTBagBYXpk",
            "link": "www.youtube.com/watch?v=klTBagBYXpk",
            "title": "RudeLies & Clarx - Erase [NCS Release]",
            "duration": "2:53",
            "views": 892359,
            "thumbnails": [
                "https://img.youtube.com/vi/klTBagBYXpk/default.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/hqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/mqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/sddefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/maxresdefault.jpg"
            ]
        },
        {
            "index": 6,
            "id": "TeSiiKpbCiM",
            "link": "www.youtube.com/watch?v=TeSiiKpbCiM",
            "title": "Heuse & Caravn - Spirits Say [NCS Release]",
            "duration": "2:47",
            "views": 760985,
            "thumbnails": [
                "https://img.youtube.com/vi/TeSiiKpbCiM/default.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/hqdefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/mqdefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/sddefault.jpg",
                "https://img.youtube.com/vi/TeSiiKpbCiM/maxresdefault.jpg"
            ]
        },
        {
            "index": 7,
            "id": "wJXB_wyEPg4",
            "link": "www.youtube.com/watch?v=wJXB_wyEPg4",
            "title": "Jonth - Collapse [NCS Release]",
            "duration": "2:32",
            "views": 723589,
            "thumbnails": [
                "https://img.youtube.com/vi/wJXB_wyEPg4/default.jpg",
                "https://img.youtube.com/vi/wJXB_wyEPg4/hqdefault.jpg",
                "https://img.youtube.com/vi/wJXB_wyEPg4/mqdefault.jpg",
                "https://img.youtube.com/vi/wJXB_wyEPg4/sddefault.jpg",
                "https://img.youtube.com/vi/wJXB_wyEPg4/maxresdefault.jpg"
            ]
        },
        {
            "index": 8,
            "id": "-CKtswUBm-U",
            "link": "www.youtube.com/watch?v=-CKtswUBm-U",
            "title": "Clarx - Money [NCS Official Video]",
            "duration": "2:46",
            "views": 847435,
            "thumbnails": [
                "https://img.youtube.com/vi/-CKtswUBm-U/default.jpg",
                "https://img.youtube.com/vi/-CKtswUBm-U/hqdefault.jpg",
                "https://img.youtube.com/vi/-CKtswUBm-U/mqdefault.jpg",
                "https://img.youtube.com/vi/-CKtswUBm-U/sddefault.jpg",
                "https://img.youtube.com/vi/-CKtswUBm-U/maxresdefault.jpg"
            ]
        },
        {
            "index": 9,
            "id": "lIOcVJGd1Sk",
            "link": "www.youtube.com/watch?v=lIOcVJGd1Sk",
            "title": "Au5 - Interstellar (feat. Danyka Nadeau) [NCS Release]",
            "duration": "6:13",
            "views": 925895,
            "thumbnails": [
                "https://img.youtube.com/vi/lIOcVJGd1Sk/default.jpg",
                "https://img.youtube.com/vi/lIOcVJGd1Sk/hqdefault.jpg",
                "https://img.youtube.com/vi/lIOcVJGd1Sk/mqdefault.jpg",
                "https://img.youtube.com/vi/lIOcVJGd1Sk/sddefault.jpg",
                "https://img.youtube.com/vi/lIOcVJGd1Sk/maxresdefault.jpg"
            ]
        },
        {
            "index": 10,
            "id": "K4DyBUG242c",
            "link": "www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "duration": "3:28",
            "views": 355900852,
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
            "id": "-Mypt378fkc",
            "link": "www.youtube.com/watch?v=-Mypt378fkc",
            "title": "NCS 24/7 Gaming Music Livestream",
            "duration": "15:17",
            "views": 10350614,
            "thumbnails": [
                "https://img.youtube.com/vi/-Mypt378fkc/default.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/hqdefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/mqdefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/sddefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/maxresdefault.jpg"
            ]
        },
        {
            "index": 12,
            "id": "EpRJY-hI6Bs",
            "link": "www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji",
            "duration": "3:37",
            "views": 10679631,
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
            "id": "Srqs4CitU2U",
            "link": "www.youtube.com/watch?v=Srqs4CitU2U",
            "title": "Jarico - Landscape [NCS BEST OF]",
            "duration": "4:04",
            "views": 9500152,
            "thumbnails": [
                "https://img.youtube.com/vi/Srqs4CitU2U/default.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/hqdefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/mqdefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/sddefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/maxresdefault.jpg"
            ]
        },
        {
            "index": 14,
            "id": "XEymPGxopmg",
            "link": "www.youtube.com/watch?v=XEymPGxopmg",
            "title": "Barren Gates & M.I.M.E - Enslaved [NCS Release]",
            "duration": "4:26",
            "views": 13994361,
            "thumbnails": [
                "https://img.youtube.com/vi/XEymPGxopmg/default.jpg",
                "https://img.youtube.com/vi/XEymPGxopmg/hqdefault.jpg",
                "https://img.youtube.com/vi/XEymPGxopmg/mqdefault.jpg",
                "https://img.youtube.com/vi/XEymPGxopmg/sddefault.jpg",
                "https://img.youtube.com/vi/XEymPGxopmg/maxresdefault.jpg"
            ]
        },
        {
            "index": 15,
            "id": "K8DUjObr_tU",
            "link": "www.youtube.com/watch?v=K8DUjObr_tU",
            "title": "LFZ - Popsicle [NCS Release]",
            "duration": "3:26",
            "views": 6509124,
            "thumbnails": [
                "https://img.youtube.com/vi/K8DUjObr_tU/default.jpg",
                "https://img.youtube.com/vi/K8DUjObr_tU/hqdefault.jpg",
                "https://img.youtube.com/vi/K8DUjObr_tU/mqdefault.jpg",
                "https://img.youtube.com/vi/K8DUjObr_tU/sddefault.jpg",
                "https://img.youtube.com/vi/K8DUjObr_tU/maxresdefault.jpg"
            ]
        },
        {
            "index": 16,
            "id": "V-mP3VU0DCg",
            "link": "www.youtube.com/watch?v=V-mP3VU0DCg",
            "title": "NIVIRO - Flares [NCS Release]",
            "duration": "4:34",
            "views": 8710857,
            "thumbnails": [
                "https://img.youtube.com/vi/V-mP3VU0DCg/default.jpg",
                "https://img.youtube.com/vi/V-mP3VU0DCg/hqdefault.jpg",
                "https://img.youtube.com/vi/V-mP3VU0DCg/mqdefault.jpg",
                "https://img.youtube.com/vi/V-mP3VU0DCg/sddefault.jpg",
                "https://img.youtube.com/vi/V-mP3VU0DCg/maxresdefault.jpg"
            ]
        },
        {
            "index": 17,
            "id": "Q_ojhcx-wrk",
            "link": "www.youtube.com/watch?v=Q_ojhcx-wrk",
            "title": "LFZ - Echoes [NCS Release]",
            "duration": "3:24",
            "views": 44900536,
            "thumbnails": [
                "https://img.youtube.com/vi/Q_ojhcx-wrk/default.jpg",
                "https://img.youtube.com/vi/Q_ojhcx-wrk/hqdefault.jpg",
                "https://img.youtube.com/vi/Q_ojhcx-wrk/mqdefault.jpg",
                "https://img.youtube.com/vi/Q_ojhcx-wrk/sddefault.jpg",
                "https://img.youtube.com/vi/Q_ojhcx-wrk/maxresdefault.jpg"
            ]
        },
        {
            "index": 18,
            "id": "u1I9ITfzqFs",
            "link": "www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]",
            "duration": "3:28",
            "views": 9521689,
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
            "id": "CLEWmT_8ppM",
            "link": "www.youtube.com/watch?v=CLEWmT_8ppM",
            "title": "Clarx - Zig Zag [NCS Release]",
            "duration": "4:28",
            "views": 24796909,
            "thumbnails": [
                "https://img.youtube.com/vi/CLEWmT_8ppM/default.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/hqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/mqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/sddefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/maxresdefault.jpg"
            ]
        },
        {
            "index": 20,
            "id": "_XspQUK22-U",
            "link": "www.youtube.com/watch?v=_XspQUK22-U",
            "title": "Diamond Eyes - Everything [NCS Release]",
            "duration": "1:14:54",
            "views": 15533344,
            "thumbnails": [
                "https://img.youtube.com/vi/_XspQUK22-U/default.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/hqdefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/mqdefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/sddefault.jpg",
                "https://img.youtube.com/vi/_XspQUK22-U/maxresdefault.jpg"
            ]
        },
        {
            "index": 21,
            "id": "i7MtYfUhfiQ",
            "link": "www.youtube.com/watch?v=i7MtYfUhfiQ",
            "title": "Top 20 songs of TheFatRat 2017 - TheFatRat Mega Mix",
            "duration": "1:00:35",
            "views": 6138273,
            "thumbnails": [
                "https://img.youtube.com/vi/i7MtYfUhfiQ/default.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/hqdefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/mqdefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/sddefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 22,
            "id": "MEkaqZecpUQ",
            "link": "www.youtube.com/watch?v=MEkaqZecpUQ",
            "title": "NCS: 2019 \u201820 Million\u2019 Mix | Future Hits",
            "duration": "3:44",
            "views": 30892424,
            "thumbnails": [
                "https://img.youtube.com/vi/MEkaqZecpUQ/default.jpg",
                "https://img.youtube.com/vi/MEkaqZecpUQ/hqdefault.jpg",
                "https://img.youtube.com/vi/MEkaqZecpUQ/mqdefault.jpg",
                "https://img.youtube.com/vi/MEkaqZecpUQ/sddefault.jpg",
                "https://img.youtube.com/vi/MEkaqZecpUQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 23,
            "id": "tcHJodG5hX8",
            "link": "www.youtube.com/watch?v=tcHJodG5hX8",
            "title": "Unknown Brain - Why Do I? (feat. Bri Tolani) [NCS Release]",
            "duration": "1:30:31",
            "views": 673,
            "thumbnails": [
                "https://img.youtube.com/vi/tcHJodG5hX8/default.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/hqdefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/mqdefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/sddefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/maxresdefault.jpg"
            ]
        },
        {
            "index": 24,
            "id": "1cE0YlJLhNs",
            "link": "www.youtube.com/watch?v=1cE0YlJLhNs",
            "title": "Best Music Mix 2020 \u266b Gaming Music x Nocopyrightsounds \u266b Best Trap, EDM, Dubstep, DnB, Electro House",
            "duration": "3:50",
            "views": 126521551,
            "thumbnails": [
                "https://img.youtube.com/vi/1cE0YlJLhNs/default.jpg",
                "https://img.youtube.com/vi/1cE0YlJLhNs/hqdefault.jpg",
                "https://img.youtube.com/vi/1cE0YlJLhNs/mqdefault.jpg",
                "https://img.youtube.com/vi/1cE0YlJLhNs/sddefault.jpg",
                "https://img.youtube.com/vi/1cE0YlJLhNs/maxresdefault.jpg"
            ]
        },
        {
            "index": 25,
            "id": "yJg-Y5byMMw",
            "link": "www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "duration": "3:13",
            "views": 34745643,
            "thumbnails": [
                "https://img.youtube.com/vi/yJg-Y5byMMw/default.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/hqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/mqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/sddefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/maxresdefault.jpg"
            ]
        },
        {
            "index": 26,
            "id": "Tv6WImqSuxA",
            "link": "www.youtube.com/watch?v=Tv6WImqSuxA",
            "title": "JPB - High [NCS Release]",
            "duration": "3:08:06",
            "views": 5702077,
            "thumbnails": [
                "https://img.youtube.com/vi/Tv6WImqSuxA/default.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/hqdefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/mqdefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/sddefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/maxresdefault.jpg"
            ]
        },
        {
            "index": 27,
            "id": "ABuNwLP-z9o",
            "link": "www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "Alan Walker - Fade [NCS Release]",
            "duration": "4:21",
            "views": 413177306,
            "thumbnails": [
                "https://img.youtube.com/vi/ABuNwLP-z9o/default.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/hqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/mqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/sddefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/maxresdefault.jpg"
            ]
        },
        {
            "index": 28,
            "id": "bM7SZ5SBzyY",
            "link": "www.youtube.com/watch?v=bM7SZ5SBzyY",
            "title": "Jim Yosef & Anna Yvette - Linked [NCS Release]",
            "duration": "3:44",
            "views": 23377374,
            "thumbnails": [
                "https://img.youtube.com/vi/bM7SZ5SBzyY/default.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/hqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/mqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/sddefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/maxresdefault.jpg"
            ]
        },
        {
            "index": 29,
            "id": "yHLtE1wFeRQ",
            "link": "www.youtube.com/watch?v=yHLtE1wFeRQ",
            "title": "Janji - Heroes Tonight (feat. Johnning) [NCS Release]",
            "duration": "3:29",
            "views": 196300116,
            "thumbnails": [
                "https://img.youtube.com/vi/yHLtE1wFeRQ/default.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/hqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/mqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/sddefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 30,
            "id": "3nQNiWdeH2Q",
            "link": "www.youtube.com/watch?v=3nQNiWdeH2Q",
            "title": "JJD - Adventure [NCS Release]",
            "duration": "4:40",
            "views": 36470861,
            "thumbnails": [
                "https://img.youtube.com/vi/3nQNiWdeH2Q/default.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/hqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/mqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/sddefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/maxresdefault.jpg"
            ]
        },
        {
            "index": 31,
            "id": "f2xGxd9xPYA",
            "link": "www.youtube.com/watch?v=f2xGxd9xPYA",
            "title": "Culture Code - Make Me Move (feat. Karra) [NCS Release]",
            "duration": "3:17",
            "views": 41689104,
            "thumbnails": [
                "https://img.youtube.com/vi/f2xGxd9xPYA/default.jpg",
                "https://img.youtube.com/vi/f2xGxd9xPYA/hqdefault.jpg",
                "https://img.youtube.com/vi/f2xGxd9xPYA/mqdefault.jpg",
                "https://img.youtube.com/vi/f2xGxd9xPYA/sddefault.jpg",
                "https://img.youtube.com/vi/f2xGxd9xPYA/maxresdefault.jpg"
            ]
        },
        {
            "index": 32,
            "id": "vBGiFtb8Rpw",
            "link": "www.youtube.com/watch?v=vBGiFtb8Rpw",
            "title": "Axol x Alex Skrindo - You [NCS Release]",
            "duration": "3:16",
            "views": 25964677,
            "thumbnails": [
                "https://img.youtube.com/vi/vBGiFtb8Rpw/default.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/hqdefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/mqdefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/sddefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/maxresdefault.jpg"
            ]
        },
        {
            "index": 33,
            "id": "sA_p0rQtDXE",
            "link": "www.youtube.com/watch?v=sA_p0rQtDXE",
            "title": "Valence - Infinite [NCS Release]",
            "duration": "3:23",
            "views": 12531256,
            "thumbnails": [
                "https://img.youtube.com/vi/sA_p0rQtDXE/default.jpg",
                "https://img.youtube.com/vi/sA_p0rQtDXE/hqdefault.jpg",
                "https://img.youtube.com/vi/sA_p0rQtDXE/mqdefault.jpg",
                "https://img.youtube.com/vi/sA_p0rQtDXE/sddefault.jpg",
                "https://img.youtube.com/vi/sA_p0rQtDXE/maxresdefault.jpg"
            ]
        },
        {
            "index": 34,
            "id": "QHoqD47gQG8",
            "link": "www.youtube.com/watch?v=QHoqD47gQG8",
            "title": "Unknown Brain x Rival - Control (feat. Jex) [NCS Release]",
            "duration": "2:47",
            "views": 28415392,
            "thumbnails": [
                "https://img.youtube.com/vi/QHoqD47gQG8/default.jpg",
                "https://img.youtube.com/vi/QHoqD47gQG8/hqdefault.jpg",
                "https://img.youtube.com/vi/QHoqD47gQG8/mqdefault.jpg",
                "https://img.youtube.com/vi/QHoqD47gQG8/sddefault.jpg",
                "https://img.youtube.com/vi/QHoqD47gQG8/maxresdefault.jpg"
            ]
        },
        {
            "index": 35,
            "id": "bLZHcnuqscU",
            "link": "www.youtube.com/watch?v=bLZHcnuqscU",
            "title": "Top 30 NoCopyrightSounds | Best of NCS | 2H NoCopyrightSounds | NCS : The Best of all time",
            "duration": "1:52:25",
            "views": 1099974,
            "thumbnails": [
                "https://img.youtube.com/vi/bLZHcnuqscU/default.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/hqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/mqdefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/sddefault.jpg",
                "https://img.youtube.com/vi/bLZHcnuqscU/maxresdefault.jpg"
            ]
        },
        {
            "index": 36,
            "id": "HPhHr6h4Qjc",
            "link": "www.youtube.com/watch?v=HPhHr6h4Qjc",
            "title": "Unknown Brain - Superhero (feat. Chris Linton) [NCS Release]",
            "duration": "3:02",
            "views": 78927257,
            "thumbnails": [
                "https://img.youtube.com/vi/HPhHr6h4Qjc/default.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/hqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/mqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/sddefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/maxresdefault.jpg"
            ]
        }
    ]
}
```
