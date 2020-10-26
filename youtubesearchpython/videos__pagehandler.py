import sys

if sys.version_info[0] == 2:
    import HTMLParser
else:
    import html


class PageHandler:
    def pageResponseHandler(self):
        self.links = []
        self.ids = []
        self.titles = []
        self.channels = []
        self.channelIds = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        self.pageSource = self.page.split()

        if sys.version_info < (2, 8):
            html = HTMLParser.HTMLParser()

        for index in range(0, len(self.pageSource) - 1, 1):

            element = self.pageSource[index]
            elementNext = self.pageSource[index+1]
            elementPrev = self.pageSource[index-1]

            ''' Setting Video View Counts. '''

            if element == "views</li></ul></div><div":
                viewCount = 0
                for character in elementPrev:
                    if character.isnumeric():
                        viewCount = viewCount * 10 + int(character)
                self.views+=[viewCount]
                ''' Unimplemented as this response is not recieved now '''
                self.channelIds+=[""]         

            ''' Setting Video Links, IDs And Thumbnails. '''

            if element[0:15] == 'href="/watch?v=' and len('www.youtube.com'+element[6:len(element)-1]) == 35:
                thumbnailbuffer = []
                modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                if element[15:len(element) - 1] not in self.ids:
                    self.links+=['https://www.youtube.com'+element[6:len(element)-1]]
                    self.ids+=[element[15:len(element) - 1]]
                    for mode in modes:
                        thumbnailbuffer+=["https://img.youtube.com/vi/" + element[15:len(element) - 1] + "/" + mode + ".jpg"]
                    self.thumbnails+=[thumbnailbuffer]

            ''' Setting Video Channels. '''

            if (element[-15:] == '</a>&nbsp;<span' and self.pageSource[index+1] == 'title="Verified"') or (element[-14:] == '</a></div><div' and self.pageSource[index+1] == 'class="yt-lockup-meta'):
                channelBuffer = ""
                channelText = ""
                for channelIndex in range(0, 10):
                    if self.pageSource[index - channelIndex][0] == ">":
                        channelText = self.pageSource[index - channelIndex] + " " + channelText
                        break
                    else:
                        channelText = self.pageSource[index - channelIndex] + " " + channelText
                channelText = channelText[1:]
                for index in range(0, len(channelText)):
                    if channelText[index] == "<":
                        break
                    else:
                        channelBuffer+=channelText[index]
                self.channels+= [channelBuffer]

            ''' Setting Video Durations. '''

            if element[0:19] == 'aria-hidden="true">' and element[19].isnumeric():
                buffer = ""
                bufferBool = False
                for character in  element:
                    if character == ">":
                        bufferBool = True
                    if bufferBool and character!= "<":
                        buffer+=character
                    if character == "<":
                        break
                self.durations+=[buffer[1::]]

            ''' Setting Video Titles. '''

            if (element[0:23] == 'data-sessionlink="itct=') and (elementNext[0:7] == 'title="'):
                buffer = ""
                init = self.pageSource[index+1]
                buffer+=init
                subIndex = index+2
                end = index+22
                while subIndex<end:
                    this_element = self.pageSource[subIndex]
                    next_element = self.pageSource[subIndex+1]
                    if (this_element[len(this_element)-1])== '"':
                        if next_element == 'rel="spf-prefetch"':
                            buffer+=(" "+this_element)
                            self.titles+=[html.unescape(buffer[7:-1])]
                            break
                    else:
                        buffer+=(" "+this_element)
                    subIndex+=1

            if len(self.titles) + 1 > self.max_results:
                break
