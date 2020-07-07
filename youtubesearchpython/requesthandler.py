#########v1.2.1#########

import urllib.request

class requesthandler:

    def request(self):
        
        try:
            request = "https://www.youtube.com/results?search_query=%s&page=%d" %(self.keyword, self.offset)
            
            #########Making Network Request#########

            self.page = urllib.request.urlopen(request).read().decode('utf_8')

            #########Identifying the type of response returned.#########

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except: 
            self.networkError = False