# [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)


**Search for videos and playlists in YouTube WITHOUT YouTube Data API v3.**


Made without using YouTube Data API v3 and any other third party library.

This library is intended for personal and non-commercial usage only.


Working as of 2020.


## :floppy_disk: Install


###### Supports both Python 3 & Python 2
```bash
pip install youtube-search-python
```
###### Alternatively you can clone the repo, and run "Usage Example.py"


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


## :gift_heart: Like the module?


Consider starring the repository. Feel free to use.

It takes a lot of time to deal with the changes that YouTube makes time to time.

Feel free to open issue, in case you find one.


## :heavy_check_mark: Current Progress


Currently search result returns:

- Video Link
- Video Title
- Channel Name
- Video Duration
- Video View Count
- Video ID
- Video Thumbnails
- Channel ID
- Video Publish Time

(Nearly everything that YouTube offers in its search result page.)


## :page_with_curl: Example Result


```json
{
    "search_result": [
        {
            "index": 0,
            "id": "QnL5P0tFkwM",
            "link": "https://www.youtube.com/watch?v=QnL5P0tFkwM",
            "title": "Rogers & Dean - Jungle [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:22",
            "views": 126560,
            "thumbnails": [
                "https://img.youtube.com/vi/QnL5P0tFkwM/default.jpg",
                "https://img.youtube.com/vi/QnL5P0tFkwM/hqdefault.jpg",
                "https://img.youtube.com/vi/QnL5P0tFkwM/mqdefault.jpg",
                "https://img.youtube.com/vi/QnL5P0tFkwM/sddefault.jpg",
                "https://img.youtube.com/vi/QnL5P0tFkwM/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "12 hours ago"
        },
        {
            "index": 1,
            "id": "K4DyBUG242c",
            "link": "https://www.youtube.com/watch?v=K4DyBUG242c",
            "title": "Cartoon - On & On (feat. Daniel Levi) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:28",
            "views": 380778599,
            "thumbnails": [
                "https://img.youtube.com/vi/K4DyBUG242c/default.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/hqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/mqdefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/sddefault.jpg",
                "https://img.youtube.com/vi/K4DyBUG242c/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 2,
            "id": "yJg-Y5byMMw",
            "link": "https://www.youtube.com/watch?v=yJg-Y5byMMw",
            "title": "Warriyo - Mortals (feat. Laura Brehm) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:50",
            "views": 145980997,
            "thumbnails": [
                "https://img.youtube.com/vi/yJg-Y5byMMw/default.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/hqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/mqdefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/sddefault.jpg",
                "https://img.youtube.com/vi/yJg-Y5byMMw/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "3 years ago"
        },
        {
            "index": 3,
            "id": "S19UcWdOA-I",
            "link": "https://www.youtube.com/watch?v=S19UcWdOA-I",
            "title": "Lost Sky - Fearless pt.II (feat. Chris Linton) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:14",
            "views": 84577781,
            "thumbnails": [
                "https://img.youtube.com/vi/S19UcWdOA-I/default.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/hqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/mqdefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/sddefault.jpg",
                "https://img.youtube.com/vi/S19UcWdOA-I/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "2 years ago"
        },
        {
            "index": 4,
            "id": "QglaLzo_aPk",
            "link": "https://www.youtube.com/watch?v=QglaLzo_aPk",
            "title": "Julius Dreisig & Zeus X Crona - Invisible [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:22",
            "views": 83220946,
            "thumbnails": [
                "https://img.youtube.com/vi/QglaLzo_aPk/default.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/hqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/mqdefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/sddefault.jpg",
                "https://img.youtube.com/vi/QglaLzo_aPk/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "2 years ago"
        },
        {
            "index": 5,
            "id": "yHLtE1wFeRQ",
            "link": "https://www.youtube.com/watch?v=yHLtE1wFeRQ",
            "title": "Jim Yosef & Anna Yvette - Linked [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:43",
            "views": 26104112,
            "thumbnails": [
                "https://img.youtube.com/vi/yHLtE1wFeRQ/default.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/hqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/mqdefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/sddefault.jpg",
                "https://img.youtube.com/vi/yHLtE1wFeRQ/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "2 years ago"
        },
        {
            "index": 6,
            "id": "EpRJY-hI6Bs",
            "link": "https://www.youtube.com/watch?v=EpRJY-hI6Bs",
            "title": "4 The Most Popular of NCS - NoCopyrightSounds | Cartoon | Disfigure | Electro-Light | Janji",
            "channel": "Monster Boy Music",
            "duration": "15:17",
            "views": 15007567,
            "thumbnails": [
                "https://img.youtube.com/vi/EpRJY-hI6Bs/default.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/hqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/mqdefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/sddefault.jpg",
                "https://img.youtube.com/vi/EpRJY-hI6Bs/maxresdefault.jpg"
            ],
            "channelId": "UC2lqMWiqD-XbV9NJ6x6mj8g",
            "publishTime": "1 year ago"
        },
        {
            "index": 7,
            "id": "u1I9ITfzqFs",
            "link": "https://www.youtube.com/watch?v=u1I9ITfzqFs",
            "title": "Diviners - Savannah (feat. Philly K) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:24",
            "views": 48342487,
            "thumbnails": [
                "https://img.youtube.com/vi/u1I9ITfzqFs/default.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/hqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/mqdefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/sddefault.jpg",
                "https://img.youtube.com/vi/u1I9ITfzqFs/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "4 years ago"
        },
        {
            "index": 8,
            "id": "Tv6WImqSuxA",
            "link": "https://www.youtube.com/watch?v=Tv6WImqSuxA",
            "title": "JPB - High [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:13",
            "views": 39427456,
            "thumbnails": [
                "https://img.youtube.com/vi/Tv6WImqSuxA/default.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/hqdefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/mqdefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/sddefault.jpg",
                "https://img.youtube.com/vi/Tv6WImqSuxA/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 9,
            "id": "xYfn7MWU7TQ",
            "link": "https://www.youtube.com/watch?v=xYfn7MWU7TQ",
            "title": "Axol & The Tech Thieves - Bleed [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:12",
            "views": 14529585,
            "thumbnails": [
                "https://img.youtube.com/vi/xYfn7MWU7TQ/default.jpg",
                "https://img.youtube.com/vi/xYfn7MWU7TQ/hqdefault.jpg",
                "https://img.youtube.com/vi/xYfn7MWU7TQ/mqdefault.jpg",
                "https://img.youtube.com/vi/xYfn7MWU7TQ/sddefault.jpg",
                "https://img.youtube.com/vi/xYfn7MWU7TQ/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "3 years ago"
        },
        {
            "index": 10,
            "id": "bM7SZ5SBzyY",
            "link": "https://www.youtube.com/watch?v=bM7SZ5SBzyY",
            "title": "Alan Walker - Fade [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:21",
            "views": 423471018,
            "thumbnails": [
                "https://img.youtube.com/vi/bM7SZ5SBzyY/default.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/hqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/mqdefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/sddefault.jpg",
                "https://img.youtube.com/vi/bM7SZ5SBzyY/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 11,
            "id": "__CRWE-L45k",
            "link": "https://www.youtube.com/watch?v=__CRWE-L45k",
            "title": "Electro-Light - Symbolism [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:52",
            "views": 176322397,
            "thumbnails": [
                "https://img.youtube.com/vi/__CRWE-L45k/default.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/hqdefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/mqdefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/sddefault.jpg",
                "https://img.youtube.com/vi/__CRWE-L45k/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 12,
            "id": "TW9d8vYrVFQ",
            "link": "https://www.youtube.com/watch?v=TW9d8vYrVFQ",
            "title": "Elektronomia - Sky High [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:58",
            "views": 173356794,
            "thumbnails": [
                "https://img.youtube.com/vi/TW9d8vYrVFQ/default.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/hqdefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/mqdefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/sddefault.jpg",
                "https://img.youtube.com/vi/TW9d8vYrVFQ/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "3 years ago"
        },
        {
            "index": 13,
            "id": "3nQNiWdeH2Q",
            "link": "https://www.youtube.com/watch?v=3nQNiWdeH2Q",
            "title": "Janji - Heroes Tonight (feat. Johnning) [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:29",
            "views": 217081192,
            "thumbnails": [
                "https://img.youtube.com/vi/3nQNiWdeH2Q/default.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/hqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/mqdefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/sddefault.jpg",
                "https://img.youtube.com/vi/3nQNiWdeH2Q/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 14,
            "id": "J2X5mJ3HDYE",
            "link": "https://www.youtube.com/watch?v=J2X5mJ3HDYE",
            "title": "DEAF KEV - Invincible [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "4:34",
            "views": 231661372,
            "thumbnails": [
                "https://img.youtube.com/vi/J2X5mJ3HDYE/default.jpg",
                "https://img.youtube.com/vi/J2X5mJ3HDYE/hqdefault.jpg",
                "https://img.youtube.com/vi/J2X5mJ3HDYE/mqdefault.jpg",
                "https://img.youtube.com/vi/J2X5mJ3HDYE/sddefault.jpg",
                "https://img.youtube.com/vi/J2X5mJ3HDYE/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        },
        {
            "index": 15,
            "id": "p7ZsBPK656s",
            "link": "https://www.youtube.com/watch?v=p7ZsBPK656s",
            "title": "Disfigure - Blank [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:30",
            "views": 194926588,
            "thumbnails": [
                "https://img.youtube.com/vi/p7ZsBPK656s/default.jpg",
                "https://img.youtube.com/vi/p7ZsBPK656s/hqdefault.jpg",
                "https://img.youtube.com/vi/p7ZsBPK656s/mqdefault.jpg",
                "https://img.youtube.com/vi/p7ZsBPK656s/sddefault.jpg",
                "https://img.youtube.com/vi/p7ZsBPK656s/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "7 years ago"
        },
        {
            "index": 16,
            "id": "Hn4sfC2PbhI",
            "link": "https://www.youtube.com/watch?v=Hn4sfC2PbhI",
            "title": "Sub Urban - Cradles [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:29",
            "views": 96184059,
            "thumbnails": [
                "https://img.youtube.com/vi/Hn4sfC2PbhI/default.jpg",
                "https://img.youtube.com/vi/Hn4sfC2PbhI/hqdefault.jpg",
                "https://img.youtube.com/vi/Hn4sfC2PbhI/mqdefault.jpg",
                "https://img.youtube.com/vi/Hn4sfC2PbhI/sddefault.jpg",
                "https://img.youtube.com/vi/Hn4sfC2PbhI/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "1 year ago"
        },
        {
            "index": 17,
            "id": "8xlDwukxjnA",
            "link": "https://www.youtube.com/watch?v=8xlDwukxjnA",
            "title": "Ship Wrek & Zookeepers - Ark [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "2:59",
            "views": 63847995,
            "thumbnails": [
                "https://img.youtube.com/vi/8xlDwukxjnA/default.jpg",
                "https://img.youtube.com/vi/8xlDwukxjnA/hqdefault.jpg",
                "https://img.youtube.com/vi/8xlDwukxjnA/mqdefault.jpg",
                "https://img.youtube.com/vi/8xlDwukxjnA/sddefault.jpg",
                "https://img.youtube.com/vi/8xlDwukxjnA/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "4 years ago"
        },
        {
            "index": 18,
            "id": "ABuNwLP-z9o",
            "link": "https://www.youtube.com/watch?v=ABuNwLP-z9o",
            "title": "\ud83d\udd25 Top 50 NoCopyRightSounds | Best of NCS | Most viewed ! Gaming Music | The Best of All Time | 2020",
            "channel": "Freeme NCS Music",
            "duration": "2:59:26",
            "views": 7875306,
            "thumbnails": [
                "https://img.youtube.com/vi/ABuNwLP-z9o/default.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/hqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/mqdefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/sddefault.jpg",
                "https://img.youtube.com/vi/ABuNwLP-z9o/maxresdefault.jpg"
            ],
            "channelId": "UCG0SzK_t4-Ylf1yZq9Xmi_g",
            "publishTime": "1 year ago"
        },
        {
            "index": 19,
            "id": "AOeY-nDp7hI",
            "link": "https://www.youtube.com/watch?v=AOeY-nDp7hI",
            "title": "Alan Walker - Spectre [NCS Release]",
            "channel": "NoCopyrightSounds",
            "duration": "3:47",
            "views": 272985458,
            "thumbnails": [
                "https://img.youtube.com/vi/AOeY-nDp7hI/default.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/hqdefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/mqdefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/sddefault.jpg",
                "https://img.youtube.com/vi/AOeY-nDp7hI/maxresdefault.jpg"
            ],
            "channelId": "UC_aEa8K-EOJ3D6gOs7HcyNg",
            "publishTime": "5 years ago"
        }
    ]
}
```
