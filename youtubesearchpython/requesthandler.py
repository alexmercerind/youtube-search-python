#########v1.2.1#########

import urllib.request

class requesthandler:

    def request(self):
        
        try:
            #########Network request is packed in try: except: for network related error handling.#########

            #########Second string is search filter for video only results.#########
            request = "https://www.youtube.com/results?search_query=%s&page=%d" %(self.keyword, self.offset)
            
            #########Making Network Request#########

            self.page = str(urllib.request.urlopen(request).read())

            #########Identifying the type of response returned.#########

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except:
            
            self.networkError = False