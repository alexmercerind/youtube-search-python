import urllib.parse
import urllib.request
import json
import html

class searchYoutube:

    #########https://github.com/alexmercerind/youtube-search-python#########

    __networkError = False
    __validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json"):

        #########CLASS CONSTRUCTOR#########

        #########Setting Feilds#########

        self.__keyword = urllib.parse.quote(keyword)
        self.__offset = offset
        self.__mode = mode

        #########Executing Entry Point Of Class#########

        self.__exec()

    def __request(self):

        try:

            #########Network request is packed in try: except: for network related error handling.#########

            request = "https://www.youtube.com/results?search_query=%s&page=%d" %(self.__keyword, self.__offset)

            #########Making Network Request#########

            self.__page = urllib.request.urlopen(request).read().decode('utf-8')

            #########Identifying the type of response returned.#########

            if self.__page[0:29] == '  <!DOCTYPE html><html lang="':
                self.__validResponse = True

        except:

            #########Setting Network Error In Case Of Network Related Errors.#########

            self.__networkError = True

    def __scriptResponseHandler(self):

        #########MAIN PROPERTY#########

        #########This property is later called in the another property exec() of the class.   #########

        temp = 0

        #########Defining Result Arrays.#########

        self.__links = []
        self.__ids = []
        self.__titles = []
        self.__channels = []
        self.__views = []
        self.__durations = []
        self.__thumbnails = []

        #########Transversing Through Network Request Array.#########

        self.__pageSource = self.__page.split('":"')

        for index in range(0, len(self.__pageSource)-1, 1):

            #########Setting Video Links, IDs And Thumbnails.#########
            if self.__pageSource[index][-98:] == '"commandMetadata":{"webCommandMetadata":{}},"addToPlaylistCommand":{"openMiniplayer":true,"videoId':
                temp+=1
                if temp % 2 == 0:
                    id = self.__pageSource[index+1][0:11]
                    thumbnailbuffer = []
                    modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                    self.__ids+=[id]
                    self.__links+=['https://www.youtube.com/watch?v='+ id]
                    for mode in modes:
                        thumbnailbuffer+=["https://img.youtube.com/vi/" + id + "/" + mode + ".jpg"]
                    self.__thumbnails+=[thumbnailbuffer]
            
            #########Setting Video Channels, Titles, Views And Durations#########

            if self.__pageSource[index][-44:] == '"accessibility":{"accessibilityData":{"label' and self.__pageSource[index+1][-36:] == '"descriptionSnippet":{"runs":[{"text':
                infoString = '"' + self.__pageSource[index+1].split("}}}")[0]
                titleBuffer = ""
                channelBuffer = ""
                durationBuffer = ""
                durationBool = False
                viewBuffer = 0
                channelBool = True
                separators = ["second", "hour", "day", "month", "year", "seconds", "hours", "days", "months", "years"]
                timeBool = True
                for element in infoString.split()[-2]:
                    if element.isnumeric():
                        viewBuffer = viewBuffer * 10 + int(element)
                for index in range(len(infoString.split())):
                    element = infoString.split()[index]
                    if element != "by" and channelBool:
                        titleBuffer+=element+" "
                    if element == "by":
                        channelBool = False
                    if element != "by" and not channelBool and index < len(infoString.split())-1:
                        if infoString.split()[index+1] in separators:
                            timeBool = False
                        else:
                            if timeBool:
                                channelBuffer+=element+" "
                            else:
                                break
                for index in range(len(infoString.split())):
                    if infoString.split()[index] == "ago":
                        durationBool = True
                        continue
                    if durationBool:
                        if index <= len(infoString.split())-3:
                            durationBuffer += infoString.split()[index] + " "
                        else:
                            break
                self.__channels+=[channelBuffer.rstrip().encode('utf-8').decode('unicode_escape')]
                self.__titles+=[titleBuffer.rstrip()[1:].encode('utf-8').decode('unicode_escape')]
                self.__views+=[viewBuffer]
                self.__durations+=[durationBuffer.rstrip()]

    def __pageResponseHandler(self):

        #########MAIN PROPERTY#########

        #########This property is later called in the another property exec() of the class.   #########

        temp = 0

        #########Defining Result Arrays.#########

        self.__links = []
        self.__ids = []
        self.__titles = []
        self.__views = []
        self.__durations = []
        self.__thumbnails = []

        #########Transversing Through Network Request Array.#########

        self.__pageSource = self.__page.split()

        for index in range(0, len(self.__pageSource)-1, 1):

            element = self.__pageSource[index]
            elementNext = self.__pageSource[index+1]
            elementPrev = self.__pageSource[index-1]

            #########Setting Video View Counts.#########

            if element == "views</li></ul></div><div":
                viewCount = 0
                for character in elementPrev:
                    if character.isnumeric():
                        viewCount = viewCount * 10 + int(character)
                self.__views+=[viewCount]            

            #########Setting Video Links, IDs And Thumbnails.#########

            if element[0:15] == 'href="/watch?v=' and len('www.youtube.com'+element[6:len(element)-1]) == 35:
                thumbnailbuffer = []
                modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                temp+=1
                if temp%2 ==0:
                    self.__links+=['https://www.youtube.com'+element[6:len(element)-1]]
                    self.__ids+=[element[15:len(element) - 1]]
                    for mode in modes:
                        thumbnailbuffer+=["https://img.youtube.com/vi/" + element[15:len(element) - 1] + "/" + mode + ".jpg"]
                    self.__thumbnails+=[thumbnailbuffer]

            #########Setting Video Durations.#########

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
                self.__durations+=[buffer[1::]]

            #########Setting Video Titles.#########

            if (element[0:23] == 'data-sessionlink="itct=') and (elementNext[0:7] == 'title="'):
                buffer = ""
                init = self.__pageSource[index+1]
                buffer+=init
                subIndex = index+2
                end = index+22
                while subIndex<end:
                    this_element = self.__pageSource[subIndex]
                    next_element = self.__pageSource[subIndex+1]
                    if (this_element[len(this_element)-1])== '"':
                        if next_element == 'rel="spf-prefetch"':
                            buffer+=(" "+this_element)
                            self.__titles+=[html.unescape(buffer[7:-1])]
                            break
                    else:
                        buffer+=(" "+this_element)
                    subIndex+=1

    def __exec(self):
        
        #########EXEC PROPERTY#########
        
        #########We are calling main property within this exec property because, YouTube randomly returns two types of#########
        #########responses, one having content as HTML and another as script, and this algorithm is designed to work  #########
        #########with both of them. So, we have no choice but to just look if the script response is recieved i.e     #########
        #########self.validResponse = False then we execute self.scriptResponseHandler() instead of                   #########
        #########self.pageResponseHandler(), finally, we call self.main() and return result to the user.              #########     

        #########We will seek potential fixes in future.#########

        #########Calling the main property.#########

        self.__request()

        if self.__networkError:
            self.__networkError = True

        else:

            if not self.__validResponse:
                self.__scriptResponseHandler()
            
            if self.__validResponse:
                self.__pageResponseHandler()

    def result(self):

        #########RESULT PROPERTY#########

        #########Checking for network error and returning None to the user in case of it.#########

        if self.__networkError:
            return None
        
        #########Returning Result.#########

        else:

            result = []
            
            #########JSON Result Handling.#########

            if self.__mode == "json":

                for index in range(len(self.__titles) - 1):
                    if not self.__validResponse:
                        thisResult = {
                        "index": index,
                        "id": self.__ids[index],
                        "link": self.__links[index],
                        "title": self.__titles[index],
                        "channel": self.__channels[index],
                        "duration": self.__durations[index],
                        "views": self.__views[index],
                        "thumbnails": self.__thumbnails[index]
                    }
                    else:
                        thisResult = {
                        "index": index,
                        "id": self.__ids[index],
                        "link": self.__links[index],
                        "title": self.__titles[index],
                        "duration": self.__durations[index],
                        "views": self.__views[index],
                        "thumbnails": self.__thumbnails[index]
                        }
                    result+=[thisResult]

                return json.dumps({"search_result": result}, indent=4)
            
            #########List Result Handling.#########

            elif self.__mode == "list":
                
                for index in range(len(self.__titles) - 1):
                    if not self.__validResponse:
                        thisResult=[
                            index,
                            self.__ids[index],
                            self.__links[index],
                            self.__titles[index],
                            self.__channels[index],
                            self.__durations[index],
                            self.__titles[index],
                            self.__thumbnails[index]
                        ]
                    else:
                        thisResult=[
                            index,
                            self.__ids[index],
                            self.__links[index],
                            self.__titles[index],
                            self.__durations[index],
                            self.__titles[index],
                            self.__thumbnails[index]
                        ]

                    result+=[thisResult]
                
                return result