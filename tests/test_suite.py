##########https://github.com/alexmercerind/youtube-search-python/##########

from youtubesearchpython import SearchVideos, SearchPlaylists

import sys

print(sys.version)

while True:
    if (sys.version[0]=="2"):
        what = raw_input("Playlist (p) search / Video (v) search? ")
        q = what.lower()
        if (q=="v" or q=="video" or q=="videos"):
            videos = SearchVideos(raw_input("Your video: "), offset = 1, mode = "json", max_results = 20)
            videos_result = videos.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
            print(videos_result)
        if (q=="p" or q=="playlist" or q=="playlists"):
            playlists = SearchPlaylists(raw_input("Your playlist: "), offset = 1, mode = "json", max_results = 20)
            playlists_result = playlists.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
            print(playlists_result)
    else if (sys.version[0]=="3"):
        what = input("Playlist (p) search / Video (v) search? ")
        q = what.lower()
        if (q=="v" or q=="video" or q=="videos"):
            videos = SearchVideos(input("Your video: "), offset = 1, mode = "json", max_results = 20)
            videos_result = videos.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
            print(videos_result)
        if (q=="p" or q=="playlist" or q=="playlists"):
            playlists = SearchPlaylists(input("Your playlist: "), offset = 1, mode = "json", max_results = 20)
            playlists_result = playlists.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
            print(playlists_result)
