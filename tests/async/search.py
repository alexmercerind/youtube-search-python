from youtubesearchpython.__future__ import *
import asyncio

async def main():
    search = Search('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
    result = await search.next()
    print(result)


    videosSearch = VideosSearch('NoCopyrightSounds', limit = 10, language = 'en', region = 'US')
    videosResult = await videosSearch.next()
    print(videosResult)


    channelsSearch = ChannelsSearch('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
    channelsResult = await channelsSearch.next()
    print(channelsResult)


    playlistsSearch = PlaylistsSearch('NoCopyrightSounds', limit = 1, language = 'en', region = 'US')
    playlistsResult = await playlistsSearch.next()
    print(playlistsResult)


    customSearch = CustomSearch('NoCopyrightSounds', VideoSortOrder.uploadDate, language = 'en', region = 'US')
    customResult = await customSearch.next()
    print(customResult)


    search = ChannelSearch('Watermelon Sugar', "UCZFWPqqPkFlNwIxcpsLOwew")
    result = await search.next()
    print(result)

    channel = ChannelSearch('The Beatles - Topic', 'UC2XdaAVUannpujzv32jcouQ')
    result = await channel.next()
    print(result)

    """
    channel = ChannelPlaylistSearch('PewDiePie', 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')
    result = await channel.next()
    print(result)

    channel = ChannelPlaylistSearch('The Beatles - Topic', 'UC2XdaAVUannpujzv32jcouQ')
    result = await channel.next()
    print(result)
    """


    search = VideosSearch('NoCopyrightSounds')
    index = 0
    result = await search.next()
    for video in result['result']:
        index += 1
        print(f'{index} - {video["title"]}')
    result = await search.next()
    for video in result['result']:
        index += 1
        print(f'{index} - {video["title"]}')
    result = await search.next()
    for video in result['result']:
        index += 1
        print(f'{index} - {video["title"]}')


asyncio.run(main())
