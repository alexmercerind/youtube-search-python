from youtubesearchpython.base.constants import *
from youtubesearchpython.handlers.requesthandler import RequestHandler
from youtubesearchpython.handlers.componenthandler import ComponentHandler
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
        self._RequestHandler__request()
        self._RequestHandler__makeSource()

    def result(self, mode: str = ResultMode.json) -> [str, dict, None]:
        if self.exception or len(self.resultComponents) == 0:
            return None
        else:
            if mode == ResultMode.json:
                return json.dumps({'result': self.resultComponents}, indent = 4)
            elif mode == ResultMode.dict:
                return {'result': self.resultComponents}
        