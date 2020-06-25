import urllib.parse
import urllib.request
import json
import html


class searchYoutube:

    #########https://github.com/alexmercerind#########

    networkError = False

    def __init__(self, keyword, offset = 1, mode = "json"):

        self.keyword = keyword
        self.offset = offset
        self.mode = mode

        self.exec()

    def main(self):
        try:
            request = "https://www.youtube.com/results?search_query=%s&disable_polymer=1&page=%d" %(urllib.parse.quote(self.keyword), self.offset)
            
            page = urllib.request.urlopen(request).read().decode('utf-8')
            page_source = page.split()

            temp = 0

            self.links = []
            self.titles = []

            for index in range(0, len(page_source)-1, 1):
                element = page_source[index]
                element_next = page_source[index+1]

                if element[0:15] == 'href="/watch?v=' and len('www.youtube.com'+element[6:len(element)-1]) == 35:
                    temp+=1
                    if temp%2 ==0:
                        self.links+=['www.youtube.com'+element[6:len(element)-1]]

                if (element[0:23] == 'data-sessionlink="itct=') and (element_next[0:7] == 'title="'):
                    buffer = ""
                    init = page_source[index+1]
                    buffer+=init
                    sub_index = index+2
                    end = index+22
                    while sub_index<end:
                        this_element = page_source[sub_index]
                        next_element = page_source[sub_index+1]
                        if (this_element[len(this_element)-1])== '"':
                            if next_element == 'rel="spf-prefetch"':
                                buffer+=(" "+this_element)
                                self.titles.append(html.unescape(buffer[7:-1]))
                                break
                        else:
                            buffer+=(" "+this_element)
                        sub_index+=1

        except:

            self.networkError = True

    def exec(self):
        self.main()
        if self.networkError:
            self.networkError = True
        else:
            if len(self.links) == 0:
                self.exec()

    def result(self):
        if self.networkError:
            return None
        else:
            result = []
            if self.mode == "json":
                for index in range(len(self.links) - 1):
                    thisResult = {"index": index, "link": self.links[index], "title": self.titles[index]}
                    result+=[thisResult]
                return json.dumps({"search_result": result}, indent=4)
            elif self.mode == "list":
                for index in range(len(self.links) - 1):
                    thisResult=[index, self.links[index], self.titles[index]]
                    result+=[thisResult]
                return result