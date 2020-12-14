from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json


class RequestHandler:
    def __request(self) -> None:
        try:
            query = {
                'search_query': self.query,
                'page': self.page,
                'sp': self.searchPreferences,
                'persist_gl': 1,
                'gl': self.region
            } if self.searchPreferences is not None else {
                'search_query': self.query,
                'page': self.page,
                'persist_gl': 1,
                'gl': self.region
            }
            request = Request(
                'https://www.youtube.com/results' + '?' + urlencode(query),
                headers = {'Accept-Language': self.language + ',en;q=0.9'}
            )
            self.response = urlopen(request).read().decode('utf_8')
        except:
            self.networkError = True

    def __makeSource(self) -> None:
        start = True
        for index in range(self.response.index('ytInitialData'), len(self.response)):
            if self.response[index] == '{' and start:
                startIndex = index
                start = False
            elif self.response[index: index + 9] == '</script>' and not start:
                endIndex = index - 1
                break
        self.responseSource = json.loads(self.response[startIndex: endIndex])['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
