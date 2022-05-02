from youtubesearchpython import *


video = Video.get('https://www.youtube.com/watch?v=z0GKGpObgPY', mode = ResultMode.json, get_upload_date=True)
print(video)
videoInfo = Video.getInfo('https://youtu.be/z0GKGpObgPY', mode = ResultMode.json)
print(videoInfo)
videoFormats = Video.getFormats('z0GKGpObgPY')
print(videoFormats)


suggestions = Suggestions(language = 'en', region = 'US')
print(suggestions.get('NoCopyrightSounds', mode = ResultMode.json))


hashtag = Hashtag('ncs', limit = 1)
print(hashtag.result())


fetcher = StreamURLFetcher()
videoA = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
videoB = Video.get("https://www.youtube.com/watch?v=ZwNxYJfW-eU")

singleUrlA = fetcher.get(videoA, 22)
allUrlsB = fetcher.getAll(videoB)
print(singleUrlA)
print(allUrlsB)


comments = Comments("_ZdsmLgCVdU")

print(len(comments.comments["result"]))

while len(comments.comments["result"]) < 100:
    comments.getNextComments()
    print(len(comments.comments["result"]))
print("Found all comments")


print(Transcript.get("https://www.youtube.com/watch?v=L7kF4MXXCoA"))


url = "https://www.youtube.com/watch?v=-1xu0IP35FI"

transcript_en = Transcript.get(url)
transcript_2 = Transcript.get(url, transcript_en["languages"][-1]["params"]) # in my case, it'd output Spanish.
print(transcript_2)


print(Channel.get("UC_aEa8K-EOJ3D6gOs7HcyNg"))


# Retrieve playlists of a channel
channel = Channel("UC_aEa8K-EOJ3D6gOs7HcyNg")
print(len(channel.result["playlists"]))
while channel.has_more_playlists():
    channel.next()
    print(len(channel.result["playlists"]))
