import copy
import json
from typing import Union, List
from urllib.parse import urlencode

from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.core.componenthandler import getValue, getVideoId



class ChannelCore(RequestCore):
    def __init__(self, channelId: str):
        super().__init__()
        self.browseId = channelId

    def prepare_request(self):
        self.url = 'https://www.youtube.com/youtubei/v1/browse' + "?" + urlencode({
            'key': searchKey,
            "prettyPrint": "false"
        })
        self.data = copy.deepcopy(requestPayload)
        self.data["params"] = "EgVhYm91dA%3D%3D"
        self.data["browseId"] = self.browseId

    def parse_response(self):
        response = self.data.json()

        thumbnails = []
        thumbnails.extend(getValue(response, ["header", "c4TabbedHeaderRenderer", "avatar", "thumbnails"]))
        thumbnails.extend(getValue(response, ["metadata", "channelMetadataRenderer", "avatar", "thumbnails"]))
        thumbnails.extend(getValue(response, ["microformat", "microformatDataRenderer", "thumbnail", "thumbnails"]))

        tabData = {}

        for tab in getValue(response, ["contents", "twoColumnBrowseResultsRenderer", "tabs"]):
            t = getValue(tab, ["tabRenderer", "selected"])
            if t:
                tabData = tab["tabRenderer"]
        
        metadata = getValue(tabData, ["content", "sectionListRenderer", "contents", 0, "itemSectionRenderer", "contents", 0, "channelAboutFullMetadataRenderer"])


        self.result = {
            "id": getValue(response, ["metadata", "channelMetadataRenderer", "externalId"]),
            "url": getValue(response, ["metadata", "channelMetadataRenderer", "channelUrl"]),
            "description": getValue(response, ["metadata", "channelMetadataRenderer", "description"]),
            "title": getValue(response, ["metadata", "channelMetadataRenderer", "title"]),
            "banners": getValue(response, ["header", "c4TabbedHeaderRenderer", "banner", "thumbnails"]),
            "subscribers": {
                "simpleText": getValue(response, ["header", "c4TabbedHeaderRenderer", "subscriberCountText", "simpleText"]),
                "label": getValue(response, ["header", "c4TabbedHeaderRenderer", "subscriberCountText", "accessibility", "accessibilityData", "label"])
            },
            "thumbnails": thumbnails,
            "availableCountryCodes": getValue(response, ["metadata", "channelMetadataRenderer", "availableCountryCodes"]),
            "isFamilySafe": getValue(response, ["metadata", "channelMetadataRenderer", "isFamilySafe"]),
            "keywords": getValue(response, ["metadata", "channelMetadataRenderer", "keywords"]),
            "tags": getValue(response, ["microformat", "microformatDataRenderer", "tags"]),
            "views": getValue(metadata, ["viewCountText", "simpleText"]),
            "joinedDate": getValue(metadata, ["joinedDateText", "runs", -1, "text"]),
            "country": getValue(metadata, ["country", "simpleText"])
        }


    async def async_create(self):
        self.prepare_request()
        self.data = await self.asyncPostRequest()
        self.parse_response()
    
    def sync_create(self):
        self.prepare_request()
        self.data = self.syncPostRequest()
        self.parse_response()


