##########https://github.com/alexmercerind/youtube-search-python/##########

from youtubesearchpython import SearchVideos, SearchPlaylists

##########Search For Videos##########

videos = SearchVideos("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)
videos_result = videos.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
print(videos_result)

##########Search For Playlists##########

playlists = SearchPlaylists("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)
playlists_result = playlists.result() #Getting JSON result (You can set mode = "json", "dict" or "list")
print(playlists_result)
