##########https://github.com/alexmercerind/youtube-search-python/##########

##########pip3 install youtube-search-python##########

from youtubesearchpython import searchYoutube

search = searchYoutube("NoCopyrightSounds", 1, "json")

print(search.result());
