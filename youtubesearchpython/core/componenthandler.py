import json
from typing import Union, List


class ComponentCore:
    def __getValue(self, source: dict, path: List[str]) -> Union[str, int, dict, None]:
        value = source
        for key in path:
            if type(key) is str:
                if key in value.keys():
                    value = value[key]
                else:
                    value = None
                    break
            elif type(key) is int:
                if len(value) != 0:
                    value = value[key]
                else:
                    value = None
                    break
        return value

    def __getVideoId(self, videoLink: str) -> str:
        if 'youtu.be' in videoLink:
            if videoLink[-1] == '/':
                return videoLink.split('/')[-2]
            return videoLink.split('/')[-1]
        elif 'youtube.com' in videoLink:
            if '&' not in videoLink:
                return videoLink[videoLink.index('v=') + 2:]
            return videoLink[videoLink.index('v=') + 2: videoLink.index('&')]
        else:
            return videoLink

    def __parseSource(self) -> None:
        try:
            self.responseSource = json.loads(self.response)
        except Exception as e:
            raise Exception('ERROR: Could not parse YouTube response.')