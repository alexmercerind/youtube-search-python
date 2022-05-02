from youtubesearchpython.__future__ import *
import asyncio

async def main():
    video = await Video.get('https://www.youtube.com/watch?v=z0GKGpObgPY', get_upload_date=True)
    print(video)
    videoInfo = await Video.getInfo('https://youtu.be/z0GKGpObgPY')
    print(videoInfo)
    videoFormats = await Video.getFormats('z0GKGpObgPY')
    print(videoFormats)


    suggestions = await Suggestions.get('NoCopyrightSounds', language = 'en', region = 'US')
    print(suggestions)


    hashtag = Hashtag('ncs', limit = 1)
    result = await hashtag.next()
    print(result)


    fetcher = StreamURLFetcher()
    await fetcher.getJavaScript()
    videoA = await Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
    videoB = await Video.get("https://www.youtube.com/watch?v=ZwNxYJfW-eU")
    singleUrlA = await fetcher.get(videoA, 22)
    allUrlsB = await fetcher.getAll(videoB)
    print(singleUrlA)
    print(allUrlsB)


    comments = Comments("_ZdsmLgCVdU")
    await comments.getNextComments()
    while len(comments.comments["result"]) < 100:
        print(len(comments.comments["result"]))
        await comments.getNextComments()
    print("Found all comments")

    
    print(await Transcript.get("https://www.youtube.com/watch?v=L7kF4MXXCoA"))


    url = "https://www.youtube.com/watch?v=-1xu0IP35FI"

    transcript_en = await Transcript.get(url)
    transcript_2 = await Transcript.get(url, transcript_en["languages"][-1]["params"]) # in my case, it'd output Spanish.
    print(transcript_2)


    print(await Channel.get("UC_aEa8K-EOJ3D6gOs7HcyNg"))

    # Retrieve playlists of a channel
    channel = Channel("UC_aEa8K-EOJ3D6gOs7HcyNg")
    await channel.init()
    print(len(channel.result["playlists"]))
    while channel.has_more_playlists():
        await channel.next()
        print(len(channel.result["playlists"]))


asyncio.run(main())
