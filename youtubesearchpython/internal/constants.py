
videoElementKey      = 'videoRenderer'
channelElementKey    = 'channelRenderer'
playlistElementKey   = 'playlistRenderer'
shelfElementKey      = 'shelfRenderer'
itemSectionKey       = 'itemSectionRenderer'
continuationItemKey  = 'continuationItemRenderer'

searchKey = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'

contentPath = ['contents', 'twoColumnSearchResultsRenderer', 'primaryContents', 'sectionListRenderer', 'contents']
continuationContentPath = ['onResponseReceivedCommands', 0, 'appendContinuationItemsAction', 'continuationItems']

class ResultMode:
    json = 0
    dict = 1

class SearchMode:
    videos = 'EgIQAQ%3D%3D'
    channels = 'EgIQAg%3D%3D'
    playlists = 'EgIQAw%3D%3D'

class VideoUploadDateFilter:
    lastHour = 'EgQIARAB'
    today = 'EgQIAhAB'
    thisWeek = 'EgQIAxAB'
    thisMonth = 'EgQIBBAB'
    thisYear = 'EgQIBRAB'

class VideoDurationFilter:
    short = 'EgQQARgB'
    long = 'EgQQARgC'

class VideoSortOrder:
    relevance = 'CAASAhAB'
    uploadDate = 'CAISAhAB'
    viewCount = 'CAMSAhAB'
    rating = 'CAESAhAB'
