from urllib import request
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import pkg_resources
import json
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from youtubesearchpython.internal.constants import *


class RequestHandler(ComponentHandler):
    def __makeRequest(self) -> None:
        with open(pkg_resources.resource_filename('youtubesearchpython', 'requestPayload.json'), 'r', encoding = 'utf_8') as file:
            requestPayload = json.loads(file.read())
            requestPayload['query'] = self.query
            requestPayload['client'] = {
                'hl': self.language,
                'gl': self.region,
            }
            if self.searchPreferences:
                requestPayload['params'] = self.searchPreferences
            if self.continuationKey:
                requestPayload['continuation'] = self.continuationKey
            requestPayloadBytes = json.dumps(requestPayload).encode('utf_8')
            request = Request(
                'https://www.youtube.com/youtubei/v1/search' + '?' + urlencode({
                    'key': searchKey,
                }),
                data = requestPayloadBytes,
                headers = {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Content-Length': len(requestPayloadBytes),
                }
            )
            try:
                self.response = urlopen(request).read().decode('utf_8')
            except:
                raise Exception('ERROR: Could not make request.')

    def __parseSource(self) -> None:
        try:
            if not self.continuationKey:
                responseContent = self._ComponentHandler__getValue(json.loads(self.response), contentPath)
            else:
                responseContent = self._ComponentHandler__getValue(json.loads(self.response), continuationContentPath)
            
            for element in responseContent:
                if itemSectionKey in element.keys():
                    self.responseSource = self._ComponentHandler__getValue(element, [itemSectionKey, 'contents'])
                if continuationItemKey in element.keys():
                    self.continuationKey = self._ComponentHandler__getValue(element, [continuationItemKey, 'continuationEndpoint', 'continuationCommand', 'token'])
        except:
            raise Exception('ERROR: Could not parse YouTube response.')