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

search = searchYoutube("NoCopyrightSounds", 1, "json")

print(search.result());

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
            "duration": "2 minutes, 35 seconds",
            "views": 164874,
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
            "title": "Wanden & Slashtaq - Better Off [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2 minutes, 18 seconds",
            "views": 401957,
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
            "duration": "2 minutes, 49 seconds",
            "views": 780178,
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
            "duration": "2 minutes, 42 seconds",
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
            "duration": "2 minutes, 54 seconds",
            "views": 619337,
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
            "duration": "3 minutes, 16 seconds",
            "views": 860716,
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
            "duration": "3 minutes, 19 seconds",
            "views": 794532,
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
            "duration": "3 minutes, 57 seconds",
            "views": 878986,
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
            "title": "RudeLies & Clarx - Erase [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2 minutes, 53 seconds",
            "views": 1029630,
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
            "title": "Heuse & Caravn - Spirits Say [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2 minutes, 47 seconds",
            "views": 876066,
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
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 28 seconds",
            "views": 357239715,
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
            "id": "EpRJY-hI6Bs",
            "link": "https://www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji",
            "channel": "Monster Boy Music",
            "duration": "15 minutes",
            "views": 10503508,
            "thumbnails": [
                "https://img.youtube.com/vi/EpRJY-hI6Bs/default.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/hqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/mqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/sddefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/maxresdefault.jpg"
            ]
        },
        {
            "index": 12,
            "id": "CYhO8vDupik",
            "link": "https://www.youtube.com/watch?v=CYhO8vDupik",
            "title": "NoCopyrightSounds - Mini Mix 2020 | Matt McGuire Drum Cover",
            "channel": "Matt McGuire",
            "duration": "6 minutes, 51 seconds",
            "views": 39320,
            "thumbnails": [
                "https://img.youtube.com/vi/CYhO8vDupik/default.jpg",
                "https://img.youtube.com/vi/CYhO8vDupik/hqdefault.jpg",
                "https://img.youtube.com/vi/CYhO8vDupik/mqdefault.jpg",
                "https://img.youtube.com/vi/CYhO8vDupik/sddefault.jpg",
                "https://img.youtube.com/vi/CYhO8vDupik/maxresdefault.jpg"
            ]
        },
        {
            "index": 13,
            "id": "yJg-Y5byMMw",
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 50 seconds",
            "views": 127634474,
            "thumbnails": [
                "https://img.youtube.com/vi/yJg-Y5byMMw/default.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/hqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/mqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/sddefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/maxresdefault.jpg"
            ]
        },
        {
            "index": 14,
            "id": "pLZq3jgE6qA",
            "link": "https://www.youtube.com/watch?v=pLZq3jgE6qA",
            "title": "Top 20 songs of Tobu - Best Of Tobu",
            "channel": "Music Store",
            "duration": "1 hour, 17 minutes",
            "views": 10902560,
            "thumbnails": [
                "https://img.youtube.com/vi/pLZq3jgE6qA/default.jpg",
                "https://img.youtube.com/vi/pLZq3jgE6qA/hqdefault.jpg",
                "https://img.youtube.com/vi/pLZq3jgE6qA/mqdefault.jpg",
                "https://img.youtube.com/vi/pLZq3jgE6qA/sddefault.jpg",
                "https://img.youtube.com/vi/pLZq3jgE6qA/maxresdefault.jpg"
            ]
        },
        {
            "index": 15,
            "id": "xgcLwtGlgLU",
            "link": "https://www.youtube.com/watch?v=xgcLwtGlgLU",
            "title": "BEAUZ & JVNA - Crazy [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 9 seconds",
            "views": 7855532,
            "thumbnails": [
                "https://img.youtube.com/vi/xgcLwtGlgLU/default.jpg",
                "https://img.youtube.com/vi/xgcLwtGlgLU/hqdefault.jpg",
                "https://img.youtube.com/vi/xgcLwtGlgLU/mqdefault.jpg",
                "https://img.youtube.com/vi/xgcLwtGlgLU/sddefault.jpg",
                "https://img.youtube.com/vi/xgcLwtGlgLU/maxresdefault.jpg"
            ]
        },
        {
            "index": 16,
            "id": "_XspQUK22-U",
            "link": "https://www.youtube.com/watch?v=_XspQUK22-U",
            "title": "Diamond Eyes - Everything [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4 minutes, 28 seconds",
            "views": 25119386,
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
            "id": "Au6fH-6xrEU",
            "link": "https://www.youtube.com/watch?v=Au6fH-6xrEU",
            "title": "Mountkid - Dino [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 9 seconds",
            "views": 5600988,
            "thumbnails": [
                "https://img.youtube.com/vi/Au6fH-6xrEU/default.jpg",
                "https://img.youtube.com/vi/Au6fH-6xrEU/hqdefault.jpg",
                "https://img.youtube.com/vi/Au6fH-6xrEU/mqdefault.jpg",
                "https://img.youtube.com/vi/Au6fH-6xrEU/sddefault.jpg",
                "https://img.youtube.com/vi/Au6fH-6xrEU/maxresdefault.jpg"
            ]
        },
        {
            "index": 18,
            "id": "tcHJodG5hX8",
            "link": "https://www.youtube.com/watch?v=tcHJodG5hX8",
            "title": "Unknown Brain - Why Do I? (feat. Bri Tolani) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 44 seconds",
            "views": 31021997,
            "thumbnails": [
                "https://img.youtube.com/vi/tcHJodG5hX8/default.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/hqdefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/mqdefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/sddefault.jpg",
                "https://img.youtube.com/vi/tcHJodG5hX8/maxresdefault.jpg"
            ]
        },
        {
            "index": 19,
            "id": "LHvYrn3FAgI",
            "link": "https://www.youtube.com/watch?v=LHvYrn3FAgI",
            "title": "Unknown Brain - Superhero (feat. Chris Linton) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 2 seconds",
            "views": 79266817,
            "thumbnails": [
                "https://img.youtube.com/vi/LHvYrn3FAgI/default.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/hqdefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/mqdefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/sddefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/maxresdefault.jpg"
            ]
        },
        {
            "index": 20,
            "id": "kddC4gi72UE",
            "link": "https://www.youtube.com/watch?v=kddC4gi72UE",
            "title": "Rival x Cadmium - Willow Tree (feat. Rosendale) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 9 seconds",
            "views": 7530654,
            "thumbnails": [
                "https://img.youtube.com/vi/kddC4gi72UE/default.jpg",
                "https://img.youtube.com/vi/kddC4gi72UE/hqdefault.jpg",
                "https://img.youtube.com/vi/kddC4gi72UE/mqdefault.jpg",
                "https://img.youtube.com/vi/kddC4gi72UE/sddefault.jpg",
                "https://img.youtube.com/vi/kddC4gi72UE/maxresdefault.jpg"
            ]
        },
        {
            "index": 21,
            "id": "CLEWmT_8ppM",
            "link": "https://www.youtube.com/watch?v=CLEWmT_8ppM",
            "title": "Clarx - Zig Zag [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 28 seconds",
            "views": 9623814,
            "thumbnails": [
                "https://img.youtube.com/vi/CLEWmT_8ppM/default.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/hqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/mqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/sddefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/maxresdefault.jpg"
            ]
        },
        {
            "index": 22,
            "id": "S19UcWdOA-I",
            "link": "https://www.youtube.com/watch?v=S19UcWdOA-I",
            "title": "Lost Sky - Fearless pt.II (feat. Chris Linton) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 15 seconds",
            "views": 64877530,
            "thumbnails": [
                "https://img.youtube.com/vi/S19UcWdOA-I/default.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/hqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/mqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/sddefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/maxresdefault.jpg"
            ]
        },
        {
            "index": 23,
            "id": "IIwiM777OzQ",
            "link": "https://www.youtube.com/watch?v=IIwiM777OzQ",
            "title": "Prismo - Stronger [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 33 seconds",
            "views": 26558909,
            "thumbnails": [
                "https://img.youtube.com/vi/IIwiM777OzQ/default.jpg",
                "https://img.youtube.com/vi/IIwiM777OzQ/hqdefault.jpg",
                "https://img.youtube.com/vi/IIwiM777OzQ/mqdefault.jpg",
                "https://img.youtube.com/vi/IIwiM777OzQ/sddefault.jpg",
                "https://img.youtube.com/vi/IIwiM777OzQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 24,
            "id": "ABuNwLP-z9o",
            "link": "https://www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "\u00f0\u009f\u0094\u00a5 Top 50 NoCopyRightSounds | Best of NCS | Most viewed ! Gaming Music | The Best of All Time | 2020",
            "channel": "Freeme NCS Music",
            "duration": "3 hours, 8 minutes",
            "views": 5828972,
            "thumbnails": [
                "https://img.youtube.com/vi/ABuNwLP-z9o/default.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/hqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/mqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/sddefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/maxresdefault.jpg"
            ]
        },
        {
            "index": 25,
            "id": "-ObdvMkCKws",
            "link": "https://www.youtube.com/watch?v=-ObdvMkCKws",
            "title": "Top 20 Most Popular Songs",
            "channel": "NCS | Best of NCS | Most Viewed Songs Music Store",
            "duration": "1 hour, 12 minutes",
            "views": 12450374,
            "thumbnails": [
                "https://img.youtube.com/vi/-ObdvMkCKws/default.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/hqdefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/mqdefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/sddefault.jpg",
                "https://img.youtube.com/vi/-ObdvMkCKws/maxresdefault.jpg"
            ]
        },
        {
            "index": 26,
            "id": "xzyRoshFFaA",
            "link": "https://www.youtube.com/watch?v=xzyRoshFFaA",
            "title": "Fareoh - Under Water [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2 minutes, 46 seconds",
            "views": 9390979,
            "thumbnails": [
                "https://img.youtube.com/vi/xzyRoshFFaA/default.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/hqdefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/mqdefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/sddefault.jpg",
                "https://img.youtube.com/vi/xzyRoshFFaA/maxresdefault.jpg"
            ]
        },
        {
            "index": 27,
            "id": "Srqs4CitU2U",
            "link": "https://www.youtube.com/watch?v=Srqs4CitU2U",
            "title": "Jarico - Landscape [NCS BEST OF]",
            "channel": "No Copyright Sounds - Best OF",
            "duration": "3 minutes, 37 seconds",
            "views": 11160119,
            "thumbnails": [
                "https://img.youtube.com/vi/Srqs4CitU2U/default.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/hqdefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/mqdefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/sddefault.jpg",
                "https://img.youtube.com/vi/Srqs4CitU2U/maxresdefault.jpg"
            ]
        },
        {
            "index": 28,
            "id": "QglaLzo_aPk",
            "link": "https://www.youtube.com/watch?v=QglaLzo_aPk",
            "title": "Julius Dreisig & Zeus X Crona - Invisible [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 22 seconds",
            "views": 65118904,
            "thumbnails": [
                "https://img.youtube.com/vi/QglaLzo_aPk/default.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/hqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/mqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/sddefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/maxresdefault.jpg"
            ]
        },
        {
            "index": 29,
            "id": "u1I9ITfzqFs",
            "link": "https://www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 24 seconds",
            "views": 45128104,
            "thumbnails": [
                "https://img.youtube.com/vi/u1I9ITfzqFs/default.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/hqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/mqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/sddefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/maxresdefault.jpg"
            ]
        },
        {
            "index": 30,
            "id": "triXo_xCqms",
            "link": "https://www.youtube.com/watch?v=triXo_xCqms",
            "title": "TOP 100 NoCopyrightSounds | Best Of NCS | 6H NoCopyRightSounds | The Best of all time",
            "channel": "Musicbot",
            "duration": "6 hours, 17 minutes",
            "views": 2952241,
            "thumbnails": [
                "https://img.youtube.com/vi/triXo_xCqms/default.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/hqdefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/mqdefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/sddefault.jpg",
                "https://img.youtube.com/vi/triXo_xCqms/maxresdefault.jpg"
            ]
        },
        {
            "index": 31,
            "id": "vBGiFtb8Rpw",
            "link": "https://www.youtube.com/watch?v=vBGiFtb8Rpw",
            "title": "Culture Code - Make Me Move (feat. Karra) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3 minutes, 17 seconds",
            "views": 41928885,
            "thumbnails": [
                "https://img.youtube.com/vi/vBGiFtb8Rpw/default.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/hqdefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/mqdefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/sddefault.jpg",
                "https://img.youtube.com/vi/vBGiFtb8Rpw/maxresdefault.jpg"
            ]
        },
        {
            "index": 32,
            "id": "HPhHr6h4Qjc",
            "link": "https://www.youtube.com/watch?v=HPhHr6h4Qjc",
            "title": "Top 30 NoCopyrightSounds | Best of NCS | 2H NoCopyrightSounds | NCS : The Best of all time",
            "channel": "Music Store",
            "duration": "1 hour, 52 minutes",
            "views": 1116020,
            "thumbnails": [
                "https://img.youtube.com/vi/HPhHr6h4Qjc/default.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/hqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/mqdefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/sddefault.jpg",
                "https://img.youtube.com/vi/HPhHr6h4Qjc/maxresdefault.jpg"
            ]
        },
        {
            "index": 33,
            "id": "bM7SZ5SBzyY",
            "link": "https://www.youtube.com/watch?v=bM7SZ5SBzyY",
            "title": "Alan Walker - Fade [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4 minutes, 21 seconds",
            "views": 413751193,
            "thumbnails": [
                "https://img.youtube.com/vi/bM7SZ5SBzyY/default.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/hqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/mqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/sddefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/maxresdefault.jpg"
            ]
        },
        {
            "index": 34,
            "id": "-Mypt378fkc",
            "link": "https://www.youtube.com/watch?v=-Mypt378fkc",
            "title": "NCS 24/7 Gaming Music Livestream",
            "channel": "NCS Arcade",
            "duration": "",
            "views": 1476780,
            "thumbnails": [
                "https://img.youtube.com/vi/-Mypt378fkc/default.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/hqdefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/mqdefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/sddefault.jpg",
                "https://img.youtube.com/vi/-Mypt378fkc/maxresdefault.jpg"
            ]
        },
        {
            "index": 35,
            "id": "YnmOmNqBWtM",
            "link": "https://www.youtube.com/watch?v=YnmOmNqBWtM",
            "title": "Spektrum & Sara Skinner - Keep You [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4 minutes, 50 seconds",
            "views": 8720451,
            "thumbnails": [
                "https://img.youtube.com/vi/YnmOmNqBWtM/default.jpg",
                "https://img.youtube.com/vi/YnmOmNqBWtM/hqdefault.jpg",
                "https://img.youtube.com/vi/YnmOmNqBWtM/mqdefault.jpg",
                "https://img.youtube.com/vi/YnmOmNqBWtM/sddefault.jpg",
                "https://img.youtube.com/vi/YnmOmNqBWtM/maxresdefault.jpg"
            ]
        }
    ]
}
```
