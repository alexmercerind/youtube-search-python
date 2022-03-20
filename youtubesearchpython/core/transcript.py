import copy
import json
from typing import Union, List
from urllib.parse import urlencode

from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore
from youtubesearchpython.core.componenthandler import getValue, getVideoId



class TranscriptCore(RequestCore):
    def __init__(self, videoLink: str, key: str):
        super().__init__()
        self.videoLink = videoLink
        self.key = key

    def prepare_params_request(self):
        self.url = 'https://www.youtube.com/youtubei/v1/next' + "?" + urlencode({
            'key': searchKey,
            "prettyPrint": "false"
        })
        self.data = copy.deepcopy(requestPayload)
        self.data["videoId"] = getVideoId(self.videoLink)

    def extract_continuation_key(self, r):
        j = r.json()
        panels = getValue(j, ["engagementPanels"])
        if not panels:
            raise Exception("Failed to create first request - No engagementPanels is present.")
        key = ""
        for panel in panels:
            panel = panel["engagementPanelSectionListRenderer"]
            if getValue(panel, ["targetId"]) == "engagement-panel-searchable-transcript":
                key = getValue(panel, ["content", "continuationItemRenderer", "continuationEndpoint", "getTranscriptEndpoint", "params"])
        if key == "" or not key:
            self.result = {"segments": [], "languages": []}
            return True
        self.key = key
        return False
    
    def prepare_transcript_request(self):
        self.url = 'https://www.youtube.com/youtubei/v1/get_transcript' + "?" + urlencode({
            'key': searchKey,
            "prettyPrint": "false"
        })
        # clientVersion must be newer than in requestPayload
        self.data = {
            "context": {
                "client": {
                    "clientName": "WEB",
                    "clientVersion": "2.20220318.00.00",
                    "newVisitorCookie": True,
                },
                "user": {
                    "lockedSafetyMode": False,
                }
            },
            "params": self.key
        }
    
    def extract_transcript(self):
        response = self.data.json()
        transcripts = getValue(response, ["actions", 0, "updateEngagementPanelAction", "content", "transcriptRenderer", "content", "transcriptSearchPanelRenderer", "body", "transcriptSegmentListRenderer", "initialSegments"])
        segments = []
        languages = []
        for segment in transcripts:
            segment = getValue(segment, ["transcriptSegmentRenderer"])
            j = {
                "startMs": getValue(segment, ["startMs"]),
                "endMs": getValue(segment, ["endMs"]),
                "text": getValue(segment, ["snippet", "simpleText"]),
                "startTime": getValue(segment, ["startTimeText", "simpleText"])
            }
            segments.append(j)
        langs = getValue(response, ["actions", 0, "updateEngagementPanelAction", "content", "transcriptRenderer", "content", "transcriptSearchPanelRenderer", "footer", "transcriptFooterRenderer", "languageMenu", "sortFilterSubMenuRenderer", "subMenuItems"])
        if langs:
            for language in langs:
                j = {
                    "params": getValue(language, ["continuation", "reloadContinuationData", "continuation"]),
                    "selected": getValue(language, ["selected"]),
                    "title": getValue(language, ["title"])
                }
                languages.append(j)
        self.result = {
            "segments": segments,
            "languages": languages
        }

    async def async_create(self):
        if not self.key:
            self.prepare_params_request()
            r = await self.asyncPostRequest()
            end = self.extract_continuation_key(r)
            if end:
                return
        self.prepare_transcript_request()
        self.data = await self.asyncPostRequest()
        self.extract_transcript()
    
    def sync_create(self):
        if not self.key:
            self.prepare_params_request()
            r = self.syncPostRequest()
            end = self.extract_continuation_key(r)
            if end:
                return
        self.prepare_transcript_request()
        self.data = self.syncPostRequest()
        self.extract_transcript()


