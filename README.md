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


## :camera: Screenshot


![Image description](https://github.com/HiteshKumarSaini/youtube-search-python/blob/master/youtube-search-python.PNG)


## :page_with_curl: Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "link": "www.youtube.com/watch?v=2W3Y9KMgNw0",
            "title": "Brook Xiao - Fire (ft. Rachel Horter) [NCS Release]"
        },
        {
            "index": 1,
            "link": "www.youtube.com/watch?v=SxfSpqFWJAg",
            "title": "Arlow - Freefall [NCS Release]"
        },
        {
            "index": 2,
            "link": "www.youtube.com/watch?v=vIE6cuAhR4o",
            "title": "Facading - Walk Away [NCS Release]"
        },
        {
            "index": 3,
            "link": "www.youtube.com/watch?v=1hxGuyfAErQ",
            "title": "BH - Holding On [NCS Release]"
        },
        {
            "index": 4,
            "link": "www.youtube.com/watch?v=klTBagBYXpk",
            "title": "RudeLies & Clarx - Erase [NCS Release]"
        },
        {
            "index": 5,
            "link": "www.youtube.com/watch?v=TeSiiKpbCiM",
            "title": "Heuse & Caravn - Spirits Say [NCS Release]"
        },
        {
            "index": 6,
            "link": "www.youtube.com/watch?v=wJXB_wyEPg4",
            "title": "Jonth - Collapse [NCS Release]"
        },
        {
            "index": 7,
            "link": "www.youtube.com/watch?v=-CKtswUBm-U",
            "title": "Clarx - Money [NCS Official Video]"
        },
        {
            "index": 8,
            "link": "www.youtube.com/watch?v=lIOcVJGd1Sk",
            "title": "Au5 - Interstellar (feat. Danyka Nadeau) [NCS Release]"
        },
        {
            "index": 9,
            "link": "www.youtube.com/watch?v=rKofUcl4qt4",
            "title": "Stereotype - TOKYO 2099 [NCS Release]"
        },
        {
            "index": 10,
            "link": "www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]"
        },
        {
            "index": 11,
            "link": "www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji"
        },
        {
            "index": 12,
            "link": "www.youtube.com/watch?v=Tv6WImqSuxA",
            "title": "JPB - High [NCS Release]"
        },
        {
            "index": 13,
            "link": "www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]"
        },
        {
            "index": 14,
            "link": "www.youtube.com/watch?v=f2xGxd9xPYA",
            "title": "JJD - Adventure [NCS Release]"
        },
        {
            "index": 15,
            "link": "www.youtube.com/watch?v=XEymPGxopmg",
            "title": "Barren Gates & M.I.M.E - Enslaved [NCS Release]"
        },
        {
            "index": 16,
            "link": "www.youtube.com/watch?v=gEbRqpFkTBk",
            "title": "Zaza - Be Together [NCS Release]"
        },
        {
            "index": 17,
            "link": "www.youtube.com/watch?v=zyXmsVwZqX4",
            "title": "Cartoon - Why We Lose (feat. Coleman Trapp) [NCS Release]"
        },
        {
            "index": 18,
            "link": "www.youtube.com/watch?v=CLEWmT_8ppM",
            "title": "Clarx - Zig Zag [NCS Release]"
        },
        {
            "index": 19,
            "link": "www.youtube.com/watch?v=_XspQUK22-U",
            "title": "Diamond Eyes - Everything [NCS Release]"
        },
        {
            "index": 20,
            "link": "www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]"
        },
        {
            "index": 21,
            "link": "www.youtube.com/watch?v=Q_ojhcx-wrk",
            "title": "LFZ - Echoes [NCS Release]"
        },
        {
            "index": 22,
            "link": "www.youtube.com/watch?v=gDwVGS75sUA",
            "title": "Lemon Fight - Stronger (feat. Jessica Reynoso) [NCS Release]"
        },
        {
            "index": 23,
            "link": "www.youtube.com/watch?v=i7MtYfUhfiQ",
            "title": "Top 20 songs of TheFatRat 2017 - TheFatRat Mega Mix"
        },
        {
            "index": 24,
            "link": "www.youtube.com/watch?v=LHvYrn3FAgI",
            "title": "Unknown Brain - Superhero (feat. Chris Linton) [NCS Release]"
        },
        {
            "index": 25,
            "link": "www.youtube.com/watch?v=yHLtE1wFeRQ",
            "title": "Jim Yosef & Anna Yvette - Linked [NCS Release]"
        },
        {
            "index": 26,
            "link": "www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "Jarico - Landscape [NCS BEST OF]"
        },
        {
            "index": 27,
            "link": "www.youtube.com/watch?v=Srqs4CitU2U",
            "title": "Valence - Infinite [NCS Release]"
        },
        {
            "index": 28,
            "link": "www.youtube.com/watch?v=QHoqD47gQG8",
            "title": "Top 30 NoCopyrightSounds | Best of NCS | 2H NoCopyrightSounds | NCS : The Best of all time"
        },
        {
            "index": 29,
            "link": "www.youtube.com/watch?v=HPhHr6h4Qjc",
            "title": "Lost Sky - Fearless pt.II (feat. Chris Linton) [NCS Release]"
        },
        {
            "index": 30,
            "link": "www.youtube.com/watch?v=S19UcWdOA-I",
            "title": "Culture Code - Make Me Move (feat. Karra) [NCS Release]"
        },
        {
            "index": 31,
            "link": "www.youtube.com/watch?v=vBGiFtb8Rpw",
            "title": "Alan Walker - Fade [NCS Release]"
        },
        {
            "index": 32,
            "link": "www.youtube.com/watch?v=bM7SZ5SBzyY",
            "title": "Aero Chord feat. DDARK - Shootin Stars [NCS Release]"
        },
        {
            "index": 33,
            "link": "www.youtube.com/watch?v=PTF5xgT-pm8",
            "title": "Elektronomia - Sky High [NCS Release]"
        },
        {
            "index": 34,
            "link": "www.youtube.com/watch?v=TW9d8vYrVFQ",
            "title": "NCS 24/7 Gaming Music Livestream"
        },
        {
            "index": 35,
            "link": "www.youtube.com/watch?v=-Mypt378fkc",
            "title": "Axol x Alex Skrindo - You [NCS Release]"
        },
        {
            "index": 36,
            "link": "www.youtube.com/watch?v=sA_p0rQtDXE",
            "title": "Top 20 Most Popular Songs by NCS | Best of NCS | Most Viewed Songs"
        }
    ]
}
```