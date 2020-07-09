# youtube-search-python


**Search for videos in YouTube WITHOUT YouTube Data API v3.**


Made without using YouTube Data API v3 and any other third party library.

This library is intended for personal and non-commercial usage only.


Working as of 2020.


## :arrow_down: Install


```
pip3 install youtube-search-python

Alternatively you can clone the repo, and run "Usage Example.py"
```


## :triangular_ruler: Usage


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


## :heart: Like the module?


Consider :star: starring the repository. Feel free to use.
It takes a lot of time to deal with the changes that YouTube makes time to time.


## :heavy_check_mark: Current Progress


Currently search result returns:

- [x] Video Link
- [x] Video Title
- [x] Channel Name
- [x] Video Duration
- [x] Video View Count
- [x] Video ID
- [x] Video Thumbnails

(Nearly everything that YouTube offers in its search result page.)

Feel free to open issue, if you find one.


## :camera: Screenshot


![Screenshot youtube-search-python](https://github.com/alexmercerind/youtube-search-python/blob/master/youtube-search-python.PNG)


## :page_with_curl: Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "id": "mm460AbveF8",
            "link": "https://www.youtube.com/watch?v=mm460AbveF8",
            "title": "Heuse & WOLFHOWL & Riell - Daylight [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:34",
            "views": 460246,
            "thumbnails": [
                "https://img.youtube.com/vi/mm460AbveF8/default.jpg",
                "https://img.youtube.com/vi/mm460AbveF8/hqdefault.jpg",
                "https://img.youtube.com/vi/mm460AbveF8/mqdefault.jpg",
                "https://img.youtube.com/vi/mm460AbveF8/sddefault.jpg",
                "https://img.youtube.com/vi/mm460AbveF8/maxresdefault.jpg"
            ]
        },
        {
            "index": 1,
            "id": "RQ5IkSeMQbc",
            "link": "https://www.youtube.com/watch?v=RQ5IkSeMQbc",
            "title": "Teyeq - Demons [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:35",
            "views": 550176,
            "thumbnails": [
                "https://img.youtube.com/vi/RQ5IkSeMQbc/default.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/hqdefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/mqdefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/sddefault.jpg",
                "https://img.youtube.com/vi/RQ5IkSeMQbc/maxresdefault.jpg"
            ]
        },
        {
            "index": 2,
            "id": "CnekLFazlxo",
            "link": "https://www.youtube.com/watch?v=CnekLFazlxo",
            "title": "Wanden & Slashtaq - Better Off [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:18",
            "views": 559398,
            "thumbnails": [
                "https://img.youtube.com/vi/CnekLFazlxo/default.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/hqdefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/mqdefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/sddefault.jpg",
                "https://img.youtube.com/vi/CnekLFazlxo/maxresdefault.jpg"
            ]
        },
        {
            "index": 3,
            "id": "BG_W8Z74nG8",
            "link": "https://www.youtube.com/watch?v=BG_W8Z74nG8",
            "title": "Jim Yosef - Fall With Me [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:49",
            "views": 866151,
            "thumbnails": [
                "https://img.youtube.com/vi/BG_W8Z74nG8/default.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/hqdefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/mqdefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/sddefault.jpg",
                "https://img.youtube.com/vi/BG_W8Z74nG8/maxresdefault.jpg"
            ]
        },
        {
            "index": 4,
            "id": "ZQHcERGiinM",
            "link": "https://www.youtube.com/watch?v=ZQHcERGiinM",
            "title": "Dark Heart - Crash Test Dummy [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:42",
            "views": 718530,
            "thumbnails": [
                "https://img.youtube.com/vi/ZQHcERGiinM/default.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/hqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/mqdefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/sddefault.jpg",
                "https://img.youtube.com/vi/ZQHcERGiinM/maxresdefault.jpg"
            ]
        },
        {
            "index": 5,
            "id": "2W3Y9KMgNw0",
            "link": "https://www.youtube.com/watch?v=2W3Y9KMgNw0",
            "title": "Brook Xiao - Fire (ft. Rachel Horter) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:54",
            "views": 746650,
            "thumbnails": [
                "https://img.youtube.com/vi/2W3Y9KMgNw0/default.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/hqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/mqdefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/sddefault.jpg",
                "https://img.youtube.com/vi/2W3Y9KMgNw0/maxresdefault.jpg"
            ]
        },
        {
            "index": 6,
            "id": "SxfSpqFWJAg",
            "link": "https://www.youtube.com/watch?v=SxfSpqFWJAg",
            "title": "Arlow - Freefall [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:16",
            "views": 961281,
            "thumbnails": [
                "https://img.youtube.com/vi/SxfSpqFWJAg/default.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/hqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/mqdefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/sddefault.jpg",
                "https://img.youtube.com/vi/SxfSpqFWJAg/maxresdefault.jpg"
            ]
        },
        {
            "index": 7,
            "id": "vIE6cuAhR4o",
            "link": "https://www.youtube.com/watch?v=vIE6cuAhR4o",
            "title": "Facading - Walk Away [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:19",
            "views": 847707,
            "thumbnails": [
                "https://img.youtube.com/vi/vIE6cuAhR4o/default.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/hqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/mqdefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/sddefault.jpg",
                "https://img.youtube.com/vi/vIE6cuAhR4o/maxresdefault.jpg"
            ]
        },
        {
            "index": 8,
            "id": "1hxGuyfAErQ",
            "link": "https://www.youtube.com/watch?v=1hxGuyfAErQ",
            "title": "BH - Holding On [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:57",
            "views": 936608,
            "thumbnails": [
                "https://img.youtube.com/vi/1hxGuyfAErQ/default.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/hqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/mqdefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/sddefault.jpg",
                "https://img.youtube.com/vi/1hxGuyfAErQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 9,
            "id": "klTBagBYXpk",
            "link": "https://www.youtube.com/watch?v=klTBagBYXpk",
            "title": "RudeLies & Clarx - Erase [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:53",
            "views": 1093597,
            "thumbnails": [
                "https://img.youtube.com/vi/klTBagBYXpk/default.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/hqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/mqdefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/sddefault.jpg",
                "https://img.youtube.com/vi/klTBagBYXpk/maxresdefault.jpg"
            ]
        },
        {
            "index": 10,
            "id": "K4DyBUG242c",
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 358141460,
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
            "duration": "15:17",
            "views": 10612191,
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
            "id": "ABuNwLP-z9o",
            "link": "https://www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "\ud83d\udd25 Top 50 NoCopyRightSounds | Best of NCS | Most viewed ! Gaming Music | The Best of All Time | 2020",
            "channel": "Freeme NCS Music",
            "duration": "3:08:06",
            "views": 5891447,
            "thumbnails": [
                "https://img.youtube.com/vi/ABuNwLP-z9o/default.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/hqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/mqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/sddefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/maxresdefault.jpg"
            ]
        },
        {
            "index": 13,
            "id": "yJg-Y5byMMw",
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:50",
            "views": 128317911,
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
            "duration": "1:17:45",
            "views": 10910877,
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
            "id": "zyXmsVwZqX4",
            "link": "https://www.youtube.com/watch?v=zyXmsVwZqX4",
            "title": "Cartoon - Why We Lose (feat. Coleman Trapp) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:34",
            "views": 147982391,
            "thumbnails": [
                "https://img.youtube.com/vi/zyXmsVwZqX4/default.jpg",
                "https://img.youtube.com/vi/zyXmsVwZqX4/hqdefault.jpg",
                "https://img.youtube.com/vi/zyXmsVwZqX4/mqdefault.jpg",
                "https://img.youtube.com/vi/zyXmsVwZqX4/sddefault.jpg",
                "https://img.youtube.com/vi/zyXmsVwZqX4/maxresdefault.jpg"
            ]
        },
        {
            "index": 16,
            "id": "i7MtYfUhfiQ",
            "link": "https://www.youtube.com/watch?v=i7MtYfUhfiQ",
            "title": "Top 20 songs of TheFatRat 2017 - TheFatRat Mega Mix",
            "channel": "Music Store",
            "duration": "1:14:54",
            "views": 15652222,
            "thumbnails": [
                "https://img.youtube.com/vi/i7MtYfUhfiQ/default.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/hqdefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/mqdefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/sddefault.jpg",
                "https://img.youtube.com/vi/i7MtYfUhfiQ/maxresdefault.jpg"
            ]
        },
        {
            "index": 17,
            "id": "LHvYrn3FAgI",
            "link": "https://www.youtube.com/watch?v=LHvYrn3FAgI",
            "title": "Unknown Brain - Superhero (feat. Chris Linton) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:02",
            "views": 79477622,
            "thumbnails": [
                "https://img.youtube.com/vi/LHvYrn3FAgI/default.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/hqdefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/mqdefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/sddefault.jpg",
                "https://img.youtube.com/vi/LHvYrn3FAgI/maxresdefault.jpg"
            ]
        },
        {
            "index": 18,
            "id": "CLEWmT_8ppM",
            "link": "https://www.youtube.com/watch?v=CLEWmT_8ppM",
            "title": "Clarx - Zig Zag [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 9680739,
            "thumbnails": [
                "https://img.youtube.com/vi/CLEWmT_8ppM/default.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/hqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/mqdefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/sddefault.jpg",
                "https://img.youtube.com/vi/CLEWmT_8ppM/maxresdefault.jpg"
            ]
        },
        {
            "index": 19,
            "id": "8Yue9YYdNLM",
            "link": "https://www.youtube.com/watch?v=8Yue9YYdNLM",
            "title": "Dirty Palm - Oblivion (feat. Micah Martin) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:51",
            "views": 21254046,
            "thumbnails": [
                "https://img.youtube.com/vi/8Yue9YYdNLM/default.jpg",
                "https://img.youtube.com/vi/8Yue9YYdNLM/hqdefault.jpg",
                "https://img.youtube.com/vi/8Yue9YYdNLM/mqdefault.jpg",
                "https://img.youtube.com/vi/8Yue9YYdNLM/sddefault.jpg",
                "https://img.youtube.com/vi/8Yue9YYdNLM/maxresdefault.jpg"
            ]
        }
    ]
}
```
