from youtubesearchpython import SearchVideos, SearchPlaylists

videos = SearchVideos(
    "NoCopyrightSounds",
    offset = 1,
    mode = "json",
    max_results = 20,
    language = "en-US",
    region="US"
)
videosResult = videos.result()
print(videosResult)

playlists = SearchPlaylists(
    "NoCopyrightSounds",
    offset = 1,
    mode = "json",
    max_results = 20,
    language = "ru-RU",
    region="US"
)
playlistsResult = playlists.result()
print(playlistsResult)
