class ScriptHandler:
    def scriptResponseHandler(self):
        self.links = []
        self.ids = []
        self.titles = []
        self.channels = []
        self.channelIds = []
        self.publishTime = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        indexValue = 0

        self.pageSource = self.page.split('":"')

        for index in range(0, len(self.pageSource) - 1, 1):
            
            ''' Setting Video Durations And View Counts. '''

            if self.pageSource[index][-14:] == '}},"simpleText' and self.pageSource[index+1][-28:] == '"viewCountText":{"simpleText':
                durationBuffer = ""
                viewCountBuffer = 0
                for character in self.pageSource[index+1]:
                    if character!= '"':
                        durationBuffer+=character
                    else:
                        break
                for character in self.pageSource[index+2]:
                    if character.isnumeric():
                        viewCountBuffer = viewCountBuffer * 10 + int(character)
                    elif character == '"':
                        break
                self.durations[-1] = durationBuffer
                self.views[-1] = viewCountBuffer

            ''' Setting Video Links, IDs And Thumbnails. '''

            if self.pageSource[index][0:9] == '/watch?v=':
                id = self.pageSource[index][9:20]
                modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                self.ids+=[id]
                self.links+=['https://www.youtube.com/watch?v='+ id]
                thumbnailbuffer = []
                for mode in modes:
                    thumbnailbuffer+=["https://img.youtube.com/vi/" + id + "/" + mode + ".jpg"]
                self.thumbnails+=[thumbnailbuffer]
            
            ''' Setting Video Titles. '''

            if self.pageSource[index][-23:] == '"title":{"runs":[{"text' and self.pageSource[index+1][-44:] == '"accessibility":{"accessibilityData":{"label':
                titleBuffer = ""
                for subIndex in range(len(self.pageSource[index+1])):
                    if self.pageSource[index+1][subIndex: subIndex+2] != '}]':
                        ''' For getting rid of " written as \" in JSON '''
                        if self.pageSource[index+1][subIndex] == '"' and self.pageSource[index+1][subIndex+1: subIndex+3] != '}]':
                            titleBuffer = titleBuffer[:-1]
                        titleBuffer+=self.pageSource[index+1][subIndex]
                    else:
                        titleBuffer = titleBuffer[:-1]
                        break
                self.titles+=[titleBuffer.replace("\\u0026", "&")]

                self.views+=["LIVE"]
                self.durations+=["LIVE"]
                self.publishTime+=["LIVE"]
                self.channels+= [""]
                self.channelIds+=[""]

            ''' Setting Video Channels. '''

            if self.pageSource[index][-32:] == '"longBylineText":{"runs":[{"text' and self.pageSource[index+1][-42:] == '"navigationEndpoint":{"clickTrackingParams':
                channelBuffer = ""
                for character in self.pageSource[index+1]:
                    if character!= '"':
                        channelBuffer+=character
                    else:
                        break
                try:
                    self.channels[-1] = channelBuffer.replace("\\u0026", "&")
                    self.channelIds[-1] = self.pageSource[index+5].split('"')[0]
                except:
                    pass
            
            ''' Setting Video Published Time Text. '''

            if self.pageSource[index][-31:] == 'publishedTimeText":{"simpleText':
                self.publishTime[-1] = self.pageSource[index+1].split('"},"')[0]

            if min(len(self.links), len(self.ids), len(self.titles), len(self.channels), len(self.channelIds), len(self.publishTime), len(self.views), len(self.durations), len(self.thumbnails)) + 1 > self.max_results:
                break
