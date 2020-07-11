import urllib.request
from urllib.request import Request


class requesthandler:

    def request(self):
        
        try:
            query = urllib.parse.urlencode({
                "search_query": self.keyword,
                "page": self.offset,
                "sp": self.searchPreferences
            })
            request = Request(
                url = "https://www.youtube.com/results" + "?" + query,
                data = None
            )

            #########Making Network Request#########

            response = urllib.request.urlopen(request).read()

            self.page = response.decode('utf_8')

            #########Identifying the type of response returned.#########

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except: 
            self.networkError = True