from youtubesearchpython.base.constants import *
from youtubesearchpython.handlers.requesthandler import RequestHandler
from youtubesearchpython.handlers.componenthandler import ComponentHandler
from typing import Union
import json


class BaseSearch(RequestHandler, ComponentHandler):
    def __init__(self, query: str, page: int = 1, limit: int = 20, language: str = 'en-US', region: str = 'US', searchPreferences: str = None):
        self.page = page
        self.query = query
        self.limit = limit
        self.language = language
        self.region = region
        self.searchPreferences = searchPreferences
        self.exception = False
        self.resultComponents = []
        self.responseSource = []
        self._RequestHandler__request()
        self._RequestHandler__makeSource()
    def result(self, mode: str = ResultMode.json) -> Union[str, dict, None]:
        '''
        Returns the result from YouTube.
        Parameters
        ----------
        mode : str, optional
            Used to switch between JSON & dictionary result. Defaults to ResultMode.json, can be ResultMode.dict as well.
        Returns
        -------
        str, dict, None
            The result returned by this method is cached at the time of instantiating the object. Thus, no new network requests are made.
        '''
        if self.exception or len(self.resultComponents) == 0:
            return None
        else:
            if mode == ResultMode.json:
                return json.dumps({'result': self.resultComponents}, indent = 4)
            elif mode == ResultMode.dict:
                return {'result': self.resultComponents}
        