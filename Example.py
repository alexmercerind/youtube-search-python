import asyncio
from youtubesearchpython import SearchVideos, SearchPlaylists

async def main():
    youtube = SearchVideos('NoCopyrightSounds', offset = 1, mode = 'json', max_results = 20)
    await youtube.search()
    print(youtube.result())

if __name__ == '__main__':
    asyncio.run(main())