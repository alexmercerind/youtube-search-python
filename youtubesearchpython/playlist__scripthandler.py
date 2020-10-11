class ScriptHandler:
    def scriptResponseHandler(self):     
        self.links = []
        self.ids = []
        self.titles = []
        self.thumbnails = []
        self.count = []
        self.channel = []

        self.pageSource = self.page.split('":"')

        for index in range(0, len(self.pageSource) - 1, 1):
            
            ''' Setting Playlist ID and link. '''

            if self.pageSource[index][-10:] == 'playlistId':

                if self.pageSource[index+1].split('"')[0] not in self.ids:
                    if self.pageSource[index+1].split('"')[0] == "WL":
                        pass
                    else:
                        self.ids+=[self.pageSource[index+1].split('"')[0]]
                        self.links+=["https://www.youtube.com/playlist?list=" + self.pageSource[index+1].split('"')[0]]

            ''' Setting Playlist Title. '''

            if self.pageSource[index][-20:] == '"title":{"simpleText' and self.pageSource[index+1][-3:] == 'url':
                self.titles+=[self.pageSource[index+1].split('"},"')[0].replace("\\u0026", "&")]

                        
            self.thumb=[]
            if self.pageSource[index][-34:] == '"thumbnails":[{"thumbnails":[{"url':
                temp=index
                while self.pageSource[temp][-10:] != 'videoCount':
                    if 'https://i.ytimg.com' in self.pageSource[temp]:
                        self.thumb.append(self.pageSource[temp].split('","')[0].replace("\\u0026", "&"))
                    temp=temp+1
                if self.pageSource[temp+1][-41:] == 'navigationEndpoint":{"clickTrackingParams':
                    self.count.append(self.pageSource[temp+1].split('","')[0])
                self.thumbnails.append(self.thumb)

                self.thumb=[]

                        
            if self.pageSource[index][-33:]=='"shortBylineText":{"runs":[{"text':
                self.channel.append(self.pageSource[index+1].split('","')[0])


            if len(self.titles) > self.max_results and len(self.ids) > self.max_results:
                max_results = min(len(self.titles), len(self.ids))
                self.titles = self.titles[0:max_results]
                self.ids = self.ids[0:max_results]
                self.links = self.links[0:max_results]
                self.thumbnails = self.thumbnails[0:max_results]
                self.count = self.count[0:max_results]
                self.channel = self.channel[0:max_results]
                break
