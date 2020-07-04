#########v1.2.1#########

import urllib.parse
import json

from youtubesearchpython.requesthandler import requesthandler
from youtubesearchpython.pagehandler import pagehandler
from youtubesearchpython.scripthandler import scripthandler

class searchYoutube(requesthandler, pagehandler, scripthandler):

    #########https://github.com/alexmercerind/youtube-search-python#########

    networkError = False
    validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20):

        #########CLASS CONSTRUCTOR#########

        #########Setting Feilds#########

        self.offset = offset
        self.mode = mode
        self.keyword = urllib.parse.quote(keyword)
        self.max_results = max_results

        #########Executing Entry Point Of Class#########

        self.exec()

    def exec(self):
        
        #########EXEC PROPERTY#########
        
        #########We are calling main property within this exec property because, YouTube randomly returns two types of#########
        #########responses, one having content as HTML and another as script, and this algorithm is designed to work  #########
        #########with both of them. So, we have no choice but to just look if the script response is recieved i.e     #########
        #########self.validResponse = False then we execute self.scriptResponseHandler() instead of                   #########
        #########self.pageResponseHandler(), finally, we call self.main() and return result to the user.              #########     

        #########We will seek potential fixes in future.#########

        #########Calling the main property.#########

        self.request()

        if self.networkError:
            self.networkError = True

        else:

            if not self.validResponse:
                self.scriptResponseHandler()
            
            if self.validResponse:
                self.pageResponseHandler()

    def result(self):

        #########RESULT PROPERTY#########

        #########Checking for network error and returning None to the user in case of it.#########

        if self.networkError:
            return None
        
        #########Returning Result.#########

        else:

            result = []
            
            #########JSON Result Handling.#########

            if self.mode in ["json", "dict"]:

                for index in range(len(self.ids)):
                    if not self.validResponse:
                        thisResult = {
                        "index": index,
                        "id": self.ids[index],
                        "link": self.links[index],
                        "title": self.titles[index],
                        "channel": self.channels[index],
                        "duration": self.durations[index],
                        "views": self.views[index],
                        "thumbnails": self.thumbnails[index]
                    }
                    else:
                        thisResult = {
                        "index": index,
                        "id": self.ids[index],
                        "link": self.links[index],
                        "title": self.titles[index],
                        "duration": self.durations[index],
                        "views": self.views[index],
                        "thumbnails": self.thumbnails[index]
                        }
                    result+=[thisResult]

                return json.dumps({"search_result": result}, indent=4) \
                        if self.mode == "json" else {"search_result": result}
            
            #########List Result Handling.#########

            elif self.mode == "list":
                
                for index in range(len(self.ids)):
                    if not self.validResponse:
                        thisResult=[
                            index,
                            self.ids[index],
                            self.links[index],
                            self.titles[index],
                            self.channels[index],
                            self.durations[index],
                            self.views[index],
                            self.thumbnails[index]
                        ]
                    else:
                        thisResult=[
                            index,
                            self.ids[index],
                            self.links[index],
                            self.titles[index],
                            self.durations[index],
                            self.views[index],
                            self.thumbnails[index]
                        ]

                    result+=[thisResult]
                
                return result