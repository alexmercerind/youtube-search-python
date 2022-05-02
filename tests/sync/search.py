from youtubesearchpython import *


allSearch = Search('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
print(allSearch.result())


videosSearch = VideosSearch('NoCopyrightSounds', limit = 10, language = 'en', region = 'US')
print(videosSearch.result(mode = ResultMode.json))


channelsSearch = ChannelsSearch('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
print(channelsSearch.result(mode = ResultMode.json))


playlistsSearch = PlaylistsSearch('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
print(playlistsSearch.result())


customSearch = CustomSearch('NoCopyrightSounds', VideoSortOrder.uploadDate, language = 'en', region = 'US')
print(customSearch.result())


search = VideosSearch('NoCopyrightSounds')
index = 0
for video in search.result()['result']:
    print(str(index) + ' - ' + video['title'])
    index += 1
search.next()
for video in search.result()['result']:
    print(str(index) + ' - ' + video['title'])
    index += 1
search.next()
for video in search.result()['result']:
    print(str(index) + ' - ' + video['title'])
    index += 1



channel = ChannelSearch("Watermelon Sugar", "UCZFWPqqPkFlNwIxcpsLOwew")
print(channel.result(mode=ResultMode.json))

channel = ChannelSearch('The Beatles - Topic', 'UC2XdaAVUannpujzv32jcouQ')
print(channel.result(mode=ResultMode.json))

#channel = ChannelPlaylistSearch('PewDiePie', 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')
#print(channel.result())

#channel = ChannelPlaylistSearch('The Beatles - Topic', 'UC2XdaAVUannpujzv32jcouQ')
#print(channel.result())
