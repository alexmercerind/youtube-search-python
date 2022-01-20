import collections
import copy
import itertools
import json
from typing import Iterable, Mapping, Tuple, TypeVar, Union, List
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from youtubesearchpython.core.componenthandler import getVideoId, getValue
from youtubesearchpython.core.constants import *
from youtubesearchpython.core.requests import RequestCore

K = TypeVar("K")
T = TypeVar("T")


class CommentsCore(RequestCore):
    commentsComponent = {"result": []}
    result = None
    continuationKey = None
    isNextRequest = False
    response = None

    def __init__(self, videoLink: str):
        super().__init__()
        self.responseSource = None
        self.videoLink = videoLink

    def prepare_continuation_request(self):
        self.data = {
            "context": {"client": {"clientName": "WEB", "clientVersion": "2.20210820.01.00"}},
            "videoId": getVideoId(self.videoLink)
        }
        self.url = f"https://www.youtube.com/youtubei/v1/next?key={searchKey}"

    def prepare_comments_request(self):
        self.data = {
            "context": {"client": {"clientName": "WEB", "clientVersion": "2.20210820.01.00"}},
            "continuation": self.continuationKey
        }

    def parse_source(self):
        self.responseSource = getValue(self.response.json(), [
            "onResponseReceivedEndpoints",
            0 if self.isNextRequest else 1,
            "appendContinuationItemsAction" if self.isNextRequest else "reloadContinuationItemsCommand",
            "continuationItems",
        ])

    def parse_continuation_source(self):
        self.continuationKey = getValue(
            self.response.json(),
            [
                "contents",
                "twoColumnWatchNextResults",
                "results",
                "results",
                "contents",
                -1,
                "itemSectionRenderer",
                "contents",
                0,
                "continuationItemRenderer",
                "continuationEndpoint",
                "continuationCommand",
                "token",
            ]
        )

    def sync_make_comment_request(self):
        self.prepare_comments_request()
        self.response = self.syncPostRequest()
        if self.response.status_code == 200:
            self.parse_source()

    def sync_make_continuation_request(self):
        self.prepare_continuation_request()
        self.response = self.syncPostRequest()
        if self.response.status_code == 200:
            self.parse_continuation_source()
            if not self.continuationKey:
                raise Exception("Could not retrieve continuation token")
        else:
            raise Exception("Status code is not 200")

    async def async_make_comment_request(self):
        self.prepare_comments_request()
        self.response = await self.asyncPostRequest()
        if self.response.status_code == 200:
            self.parse_source()

    async def async_make_continuation_request(self):
        self.prepare_continuation_request()
        self.response = await self.asyncPostRequest()
        if self.response.status_code == 200:
            self.parse_continuation_source()
            if not self.continuationKey:
                raise Exception("Could not retrieve continuation token")
        else:
            raise Exception("Status code is not 200")

    def sync_create(self):
        self.sync_make_continuation_request()
        self.sync_make_comment_request()
        self.__getComponents()

    def sync_create_next(self):
        self.isNextRequest = True
        self.sync_make_comment_request()
        self.__getComponents()

    async def async_create(self):
        await self.async_make_continuation_request()
        await self.async_make_comment_request()
        self.__getComponents()

    async def async_create_next(self):
        self.isNextRequest = True
        await self.async_make_comment_request()
        self.__getComponents()

    def __getComponents(self) -> None:
        comments = []
        for comment in self.responseSource:
            comment = getValue(comment, ["commentThreadRenderer", "comment", "commentRenderer"])
            #print(json.dumps(comment, indent=4))
            try:
                j = {
                    "id": self.__getValue(comment, ["commentId"]),
                    "author": {
                        "id": self.__getValue(comment, ["authorEndpoint", "browseEndpoint", "browseId"]),
                        "name": self.__getValue(comment, ["authorText", "simpleText"]),
                        "thumbnails": self.__getValue(comment, ["authorThumbnail", "thumbnails"])
                    },
                    "content": self.__getValue(comment, ["contentText", "runs", 0, "text"]),
                    "published": self.__getValue(comment, ["publishedTimeText", "runs", 0, "text"]),
                    "isLiked": self.__getValue(comment, ["isLiked"]),
                    "authorIsChannelOwner": self.__getValue(comment, ["authorIsChannelOwner"]),
                    "voteStatus": self.__getValue(comment, ["voteStatus"]),
                    "votes": {
                        "simpleText": self.__getValue(comment, ["voteCount", "simpleText"]),
                        "label": self.__getValue(comment, ["voteCount", "accessibility", "accessibilityData", "label"])
                    },
                    "replyCount": self.__getValue(comment, ["replyCount"]),
                }
                comments.append(j)
            except:
                pass

        self.commentsComponent["result"].extend(comments)
        self.continuationKey = self.__getValue(self.responseSource, [-1, "continuationItemRenderer", "continuationEndpoint", "continuationCommand", "token"])

    def __result(self, mode: int) -> Union[dict, str]:
        if mode == ResultMode.dict:
            return self.commentsComponent
        elif mode == ResultMode.json:
            return json.dumps(self.commentsComponent, indent=4)

    def __getValue(self, source: dict, path: Iterable[str]) -> Union[str, int, dict, None]:
        value = source
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = None
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = None
                    break
        return value

    def __getAllWithKey(self, source: Iterable[Mapping[K, T]], key: K) -> Iterable[T]:
        for item in source:
            if key in item:
                yield item[key]

    def __getValueEx(self, source: dict, path: List[str]) -> Iterable[Union[str, int, dict, None]]:
        if len(path) <= 0:
            yield source
            return
        key = path[0]
        upcoming = path[1:]
        if key is None:
            following_key = upcoming[0]
            upcoming = upcoming[1:]
            if following_key is None:
                raise Exception("Cannot search for a key twice consecutive or at the end with no key given")
            values = self.__getAllWithKey(source, following_key)
            for val in values:
                yield from self.__getValueEx(val, path=upcoming)
        else:
            val = self.__getValue(source, path=[key])
            yield from self.__getValueEx(val, path=upcoming)

    def __getFirstValue(self, source: dict, path: Iterable[str]) -> Union[str, int, dict, None]:
        values = self.__getValueEx(source, list(path))
        for val in values:
            if val is not None:
                return val
        return None
