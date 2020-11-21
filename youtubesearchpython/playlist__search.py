import json

from youtubesearchpython.__requesthandler import RequestHandler
from youtubesearchpython.playlist__scripthandler import ScriptHandler

class SearchPlaylists(RequestHandler, ScriptHandler):
    '''
    Search for playlists in YouTube.
    Parameters
    ----------
    keyword : str
        Used as a query to search for playlists in YouTube.
    offset : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    mode : str
        Search result mode. Can be 'json', 'dict' or 'list'.
    max_results : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
        Can be used to get results in particular language. Defaults to 'en-US'
    region: str, optional
        Can be used to get results according to particular region. Defaults to 'US'.
    Methods
    -------
    result()
        Returns the playlists fetched from YouTube.
    '''
    networkError = False
    validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json", max_results = 20, language = "en-US", region = "US"):

        self.offset = offset
        self.mode = mode
        self.keyword = keyword
        self.max_results = max_results
        self.searchPreferences = "EgIQAw%3D%3D"
        self.language = language
        self.region = region
        self.main()

    def main(self):
        self.request()
        if self.networkError:
            self.networkError = True
        else:
            self.scriptResponseHandler()

    def result(self):
        '''
        Returns
        -------
        None, str, dict, list
            Returns playlist results from YouTube. Returns None, if network error occurs.
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
                        "thumbnails": self.thumbnails[index],
                        "count": self.count[index],
                        "channel": self.channel[index],


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
                        self.thumbnails[index],
                        self.count[index],
                        self.channel[index],
                    ]
                    result+=[list_index]
                
                return result
