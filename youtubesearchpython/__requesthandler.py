import urllib


class requesthandler:

    def request(self):
        
        try:
            query = urllib.urlencode({
                "search_query": self.keyword,
                "page": self.offset,
                "sp": self.searchPreferences
            })
            request = "https://www.youtube.com/results" + "?" + query

            #########Making Network Request#########

            response = urllib.urlopen(request).read()

            self.page = response.decode('utf_8')

            #########Identifying the type of response returned.#########

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except: 
            self.networkError = True