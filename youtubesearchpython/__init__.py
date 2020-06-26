import urllib.parse
import urllib.request
import json
import html


class searchYoutube:

    #########https://github.com/alexmercerind/youtube-search-python#########

    networkError = False
    validResponse = False

    def __init__(self, keyword, offset = 1, mode = "json"):

        #########CLASS CONSTRUCTOR#########
        #########https://github.com/alexmercerind/youtube-search-python#########

        #########Setting Feilds#########

        self.keyword = urllib.parse.quote(keyword)
        self.offset = offset
        self.mode = mode

        #########Executing Entry Point Of Class#########
        self.exec()

    def request(self):

        try:

            #########Network request is packed in try: except: for network related error handling.#########

            request = "https://www.youtube.com/results?search_query=%s&page=%d" %(self.keyword, self.offset)

            #########Making Network Request And Splitting It Into An Array.#########

            self.page = urllib.request.urlopen(request).read().decode('utf-8')
            self.pageSource = self.page.split()

            #########Checking If The Valid Response Is Returned.#########

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except:

            #########Setting Network Error In Case Of Network Related Errors.#########

            self.networkError = True

    def main(self):

        #########MAIN PROPERTY#########
        #########https://github.com/alexmercerind/youtube-search-python#########

        #########This property is later called in the another property exec() of the class.   #########

        temp = 0

        #########Defining Result Arrays.#########

        self.links = []
        self.ids = []
        self.titles = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        #########Transversing Through Network Request Array.#########

        for index in range(0, len(self.pageSource)-1, 1):

            element = self.pageSource[index]
            elementNext = self.pageSource[index+1]
            elementPrev = self.pageSource[index-1]

            #########Setting Video View Counts.#########

            if element == "views</li></ul></div><div":
                viewCount = 0
                for character in elementPrev:
                    if character.isnumeric():
                        viewCount = viewCount * 10 + int(character)
                self.views+=[viewCount]            

            #########Setting Video Links, IDs And Thumbnails.#########

            if element[0:15] == 'href="/watch?v=' and len('www.youtube.com'+element[6:len(element)-1]) == 35:
                thumbnailbuffer = []
                modes = ["default", "hqdefault", "mqdefault", "sddefault", "maxresdefault"]
                temp+=1
                if temp%2 ==0:
                    self.links+=['www.youtube.com'+element[6:len(element)-1]]
                    self.ids+=[element[15:len(element) - 1]]
                    for mode in modes:
                        thumbnailbuffer+=["https://img.youtube.com/vi/" + element[15:len(element) - 1] + "/" + mode + ".jpg"]
                    self.thumbnails+=[thumbnailbuffer]

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
                self.durations+=[buffer[1::]]

            #########Setting Video Titles.#########

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

    def exec(self):
        
        #########EXEC PROPERTY#########
        #########https://github.com/alexmercerind/youtube-search-python#########
        
        #########We are calling main property within this exec property because, YouTube randomly returns two types of#########
        #########responses, one having content as HTML and another as script, and this algorithm is designed to work  #########
        #########with only HTML one. So, we have no choice but to just look if the algorithm failed i.e               #########
        #########self.validResponse = False then again make the request and see the output, if we get valid response, #########
        #########we call self.main() and return result to the user, instead of making request again.                  #########     

        #########This causes heavy performance expenses but we have no choice at the point.#########
        #########We will seek potential fixes in future.#########

        #########Calling the main property.#########

        self.request()

        #########Checking for netWork error.#########

        if self.networkError:

            self.networkError = True

        else:
            
            #########Checking if we got bad response from YouTube.#########

            if not self.validResponse:

                #########Again called exec() in case of invalid response.#########

                self.exec()
            
            if self.validResponse:
                
                #########Calling main() in case of a valid response.#########

                self.main()

    def result(self):

        #########RESULT PROPERTY#########
        #########https://github.com/alexmercerind/youtube-search-python#########

        #########Checking for network error and returning None to the user in case of it.#########

        if self.networkError:
            return None
        
        #########Returning Result.#########

        else:

            result = []

            #########JSON Result Handling.#########

            if self.mode == "json":

                for index in range(len(self.links) - 1):
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

                return json.dumps({"search_result": result}, indent=4)
            
            #########List Result Handling.#########

            elif self.mode == "list":
                
                for index in range(len(self.links) - 1):
                    thisResult=[
                        index,
                        self.ids[index],
                        self.links[index],
                        self.titles[index],
                        self.durations[index],
                        self.titles[index],
                        self.thumbnails[index]
                    ]
                    result+=[thisResult]
                
                return result
