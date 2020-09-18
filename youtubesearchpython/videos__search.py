import json

from youtubesearchpython.__requesthandler import RequestHandler
from youtubesearchpython.videos__pagehandler import PageHandler
from youtubesearchpython.videos__scripthandler import ScriptHandler


class SearchVideos(RequestHandler, PageHandler, ScriptHandler):
    '''
    Search for videos in YouTube.
    Parameters
    ----------
    keyword : str
        Used as a query to search for videos in YouTube.
    offset : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    mode : str
        Search result mode. Can be 'json', 'dict' or 'list'.
    maxResults : int, optional
        Maximum number of video results. Defaults to 20.
    Methods
    -------
    search()
        Searches for the videos in YouTube
    result()
        Returns the videos fetched from YouTube by search().
    '''
    networkError = False
    validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20):
        self.offset = offset
        self.mode = mode
        self.keyword = keyword
        self.max_results = max_results
        self.searchPreferences = "EgIQAQ%3D%3D"
        self.main()

    def main(self):
        self.request()
        if self.networkError:
            self.networkError = True
        else:

            if not self.validResponse:
                self.scriptResponseHandler()
            
            if self.validResponse:
                self.pageResponseHandler()

    def result(self):
        '''
        Returns
        -------
        None, str, dict, list
            Returns video results from YouTube. Returns None, if network error occurs.
        '''
        if self.networkError:
            return None

        else:

            result = []
            
            if self.mode in ["json", "dict"]:

                for index in range(len(self.ids)):
                    result_index = {
                        "index": index,
                        "id": self.ids[index],
                        "link": self.links[index],
                        "title": self.titles[index],
                        "channel": self.channels[index],
                        "duration": self.durations[index],
                        "views": self.views[index],
                        "thumbnails": self.thumbnails[index],
                        "channelId": self.channelIds[index],
                    }
                    result+=[result_index]

                if self.mode == "json":
                    return json.dumps({"search_result": result}, indent=4)
                else:
                    return {"search_result": result}
                    
            elif self.mode == "list":
                
                for index in range(len(self.ids)):
                    list_index=[
                            index,
                            self.ids[index],
                            self.links[index],
                            self.titles[index],
                            self.channels[index],
                            self.durations[index],
                            self.views[index],
                            self.thumbnails[index],
                            self.channelIds[index],
                    ]
                    result+=[list_index]
                
                return result