class scripthandler:

    def scriptResponseHandler(self):
        
        #########playlistHandler PROPERTY#########

        #########This property is later called in the another property exec() of the class.   #########

        temp = 0

        #########Defining Result Arrays.#########

        self.links = []
        self.ids = []
        self.titles = []

        #########Transversing Through Network Request Array.#########

        self.pageSource = self.page.split('":"')

        for index in range(0, len(self.pageSource) - 1, 1):
            
            #########Setting Playlist ID and link.#########

            if self.pageSource[index][-10:] == 'playlistId':
                if self.pageSource[index+1].split('"')[0] not in self.ids:
                    if self.pageSource[index+1].split('"')[0] == "WL":
                        pass
                    else:
                        self.ids+=[self.pageSource[index+1].split('"')[0]]
                        self.links+=["https://www.youtube.com/playlist?list=" + self.pageSource[index+1].split('"')[0]]

            #########Setting Playlist Title.#########

            if self.pageSource[index][-20:] == '"title":{"simpleText' and self.pageSource[index+1][-3:] == 'url':
                self.titles+=[self.pageSource[index+1].split('"},"')[0].replace("\\u0026", "&")]

            if len(self.titles) > self.max_results and len(self.ids) > self.max_results:
                max_results = min(len(self.titles), len(self.ids))
                self.titles = self.titles[0:max_results]
                self.ids = self.ids[0:max_results]
                self.links = self.links[0:max_results]
                break
                