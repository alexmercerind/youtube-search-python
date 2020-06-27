##########https://github.com/alexmercerind/youtube-search-python/##########

from youtubesearchpython import searchYoutube

search = searchYoutube("NoCopyrightSounds", 1, "json")

print(search.result())
