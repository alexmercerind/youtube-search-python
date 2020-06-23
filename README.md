# youtube-search-python


**Return video links and titles by searching in YouTube without using YouTube Data API v3.**


(Made from scratch without using YouTube Data API v3 and any other third party library!)


A small python script that will return URLs and title names of videos when entering a keyword to search in youtube.
Feel free to use. 
Made from scratch.


Working as of June, 2020.


## :arrow_down: Install


```pip3 install youtube-search-python```


## :triangular_ruler: Usage


```python

from youtubesearchpython.searchyoutube import searchyoutube
result = searchyoutube("ENTER-YOUR-SEARCH-KEYWORD-HERE", "ENTER-SEARCH-OFFSET-HERE (default is 1)")

print(result[0]) #gives video links
print(result[1]) #gives video titles




##########Returns a array having two sub-arrays with video titles and links##########
##########Returns string "Network Error!" in case a network error is encountered##########

```


## :heart: Like the module?


Consider starring the repo. Feel free to use.


## :camera: Screenshot


![Image description](https://github.com/HiteshKumarSaini/youtube-search-python/blob/master/youtube-search-python.PNG)

