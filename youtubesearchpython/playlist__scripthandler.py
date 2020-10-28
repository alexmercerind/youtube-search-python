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

            ''' Setting Playlist Thumbnail. '''
                        
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

            ''' Setting Playlist Channel. '''
                        
            if self.pageSource[index][-33:]=='"shortBylineText":{"runs":[{"text':
                self.channel.append(self.pageSource[index+1].split('","')[0])


            if min(len(self.links), len(self.ids), len(self.titles), len(self.thumbnails), len(self.count), len(self.channel)) + 1 > self.max_results:
                break
