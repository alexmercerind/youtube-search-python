import sys

if sys.version_info[0] == 2:
    from urllib import urlencode, urlopen, Request
else:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode


class RequestHandler:
    def request(self):
        try:
            query = urlencode({
                "search_query": self.keyword,
                "page": self.offset,
                "sp": self.searchPreferences,
                "persist_gl": 1,
                "gl": self.region
            })
            request = Request(
                "https://www.youtube.com/results" + "?" + query,
                headers = {"Accept-Language": f"{self.language},en;q=0.9"}
            )
            response = urlopen(request).read()
            self.page = response.decode('utf_8')

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except: 
            self.networkError = True
