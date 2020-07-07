#########v1.2.2#########

class scripthandler:

    def scriptResponseHandler(self):

        #########scriptResponseHandler PROPERTY#########

        #########This property is later called in the another property exec() of the class.   #########

        temp = 0

        #########Defining Result Arrays.#########

        self.links = []
        self.ids = []
        self.titles = []
        self.channels = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        #########Transversing Through Network Request Array.#########

        self.pageSource = self.page.split('":"')

        for index in range(0, len(self.pageSource) - 1, 1):
            
            #########Setting Video Durations And View Counts.#########

            if self.pageSource[index][-14:] == '}},"simpleText' and self.pageSource[index+1][-28:] == '"viewCountText":{"simpleText':
                durationBuffer = ""
                viewCountBuffer = 0
                for character in self.pageSource[index+1]:
                    if character!= '"':
                        durationBuffer+=character
                    else:
                        break
                for character in self.pageSource[index+2].split()[0]:
                    if character.isnumeric():
                        viewCountBuffer = viewCountBuffer * 10 + int(character)
                self.durations[-1] = durationBuffer
                self.views[-1] = viewCountBuffer

            #########Setting Video Links, IDs And Thumbnails.#########

            if self.pageSource[index][-98:] == '"commandMetadata":{"webCommandMetadata":{}},"addToPlaylistCommand":{"openMiniplayer":true,"videoId':
                temp+=1
                if temp % 2 == 0:
                    id = self.pageSource[index+1][0:11]
                    thumbnailbuffer = []
                    modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                    self.ids+=[id]
                    self.links+=['https://www.youtube.com/watch?v='+ id]
                    for mode in modes:
                        thumbnailbuffer+=["https://img.youtube.com/vi/" + id + "/" + mode + ".jpg"]
                    self.thumbnails+=[thumbnailbuffer]
            
            #########Setting Video Titles.#########

            if self.pageSource[index][-23:] == '"title":{"runs":[{"text' and self.pageSource[index+1][-44:] == '"accessibility":{"accessibilityData":{"label':
                titleBuffer = ""
                for character in self.pageSource[index+1]:
                    if character!= '"':
                        titleBuffer+=character
                    else:
                        break
                self.titles+=[titleBuffer.replace("\\u0026", "&")]
                self.views+=["LIVE"]
                self.durations+=["LIVE"]
                self.channels+= [""]

            #########Setting Video Channels.#########

            if self.pageSource[index][-32:] == '"longBylineText":{"runs":[{"text' and self.pageSource[index+1][-42:] == '"navigationEndpoint":{"clickTrackingParams':
                channelBuffer = ""
                for character in self.pageSource[index+1]:
                    if character!= '"':
                        channelBuffer+=character
                    else:
                        break
                try:
                    self.channels[-1] = channelBuffer.replace("\\u0026", "&")
                except:
                    pass

            if len(self.ids) + 1 > self.max_results:
                break