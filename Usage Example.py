##########https://github.com/alexmercerind/youtube-search-python/##########

from youtubesearchpython import searchYoutube

search = searchYoutube("NoCopyrightSounds", offset = 1, mode = "json", max_results = 20)

print(search.result())
