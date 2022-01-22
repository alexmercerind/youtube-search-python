from typing import Union
from youtubesearchpython.core.streamurlfetcher import StreamURLFetcherCore


class StreamURLFetcher(StreamURLFetcherCore):
    '''Gets direct stream URLs for a YouTube video fetched using `Video.get` or `Video.getFormats`.

    This class can fetch direct video URLs without any additional network requests (that's really fast).

    Call `get` or `getAll` method of this class & pass response returned by `Video.get` or `Video.getFormats` as parameter to fetch direct URLs.
    Getting URLs or downloading streams using youtube-dl or PyTube is can be a slow, because of the fact that they make requests to fetch the same content, which one might have already recieved at the time of showing it to the user etc.
    This class makes use of PyTube (if installed) & makes some slight improvements to functioning of PyTube.
    Avoid instantiating this class more than once, it will be slow (making global object of the class will be a recommended solution).

    Raises:
        Exception: "ERROR: PyTube is not installed. To use this functionality of youtube-search-python, PyTube must be installed."

    Examples:
        Returns direct stream URL.

        >>> from youtubesearchpython import *
        >>> fetcher = StreamURLFetcher()
        >>> video = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
        >>> url = fetcher.get(video, 251)
        >>> print(url)
        "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=251&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=audio%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=10210834&dur=634.601&lmt=1544629945422176&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5511222&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgKKIEiwQTgXsdKPEyOckgVPs_LMH6KJoeaYmZic_lelECIHXHs1ZnSP5mgtpffNlIMJM3DhxcvDbA-4udFFE6AmVP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D"
    '''
    def __init__(self):
        super().__init__()
        #self._getJS()

    def get(self, videoFormats: dict, itag: int) -> Union[str, None]:
        '''Gets direct stream URL for a YouTube video fetched using `Video.get` or `Video.getFormats`.

        Args:
            videoFormats (dict): Dictionary returned by `Video.get` or `Video.getFormats`.
            itag (int): Itag of the required stream.

        Returns:
            Union[str, None]: Returns stream URL as string. None, if no stream is present for that itag.

        Examples:
            Returns direct stream URL.

            >>> from youtubesearchpython import *
            >>> fetcher = StreamURLFetcher()
            >>> video = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
            >>> url = fetcher.get(video, 251)
            >>> print(url)
            "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=251&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=audio%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=10210834&dur=634.601&lmt=1544629945422176&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5511222&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgKKIEiwQTgXsdKPEyOckgVPs_LMH6KJoeaYmZic_lelECIHXHs1ZnSP5mgtpffNlIMJM3DhxcvDbA-4udFFE6AmVP&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D"
        '''
        self._getDecipheredURLs(videoFormats, itag)
        if len(self._streams) == 1:
            return self._streams[0]["url"]
        return None

    def getAll(self, videoFormats: dict) -> Union[dict, None]:
        '''Gets all stream URLs for a YouTube video fetched using `Video.get` or `Video.getFormats`.

        Args:
            videoFormats (dict): Dictionary returned by `Video.get` or `Video.getFormats`.

        Returns:
            Union[dict, None]: Returns stream URLs in a dictionary.
        
        Examples:
            Returns direct stream URLs in a dictionary.

            >>> from youtubesearchpython import *
            >>> fetcher = StreamURLFetcher()
            >>> video = Video.get("https://www.youtube.com/watch?v=aqz-KE-bpKQ")
            >>> allUrls = fetcher.getAll(video)
            >>> print(allUrls)
            {
                "streams": [
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=18&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=video%2Fmp4&ns=AAHB1CvhVqlATtzQj67WHI8F&gir=yes&clen=47526444&ratebypass=yes&dur=634.624&lmt=1544610273905877&mt=1610776131&fvip=6&c=WEB&txp=5531432&n=Laycu1cJ2fCN_K&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgdjTwmtEc3MpmRxH27ZvTgktL-d2by5HXXGFwo3EGR4MCIQDi0oiI8mshGssiOFu1XzQCqljZuNLhA6z19S8Ig0CRTQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "video/mp4; codecs=\"avc1.42001E, mp4a.40.2\"",
                        "quality": "medium",
                        "itag": 18,
                        "bitrate": 599167,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=22&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=video%2Fmp4&ns=AAHB1CvhVqlATtzQj67WHI8F&ratebypass=yes&dur=634.624&lmt=1544610886483826&mt=1610776131&fvip=6&c=WEB&txp=5532432&n=Laycu1cJ2fCN_K&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALaSHkcx0m9rfqJKoiJT1dY7spIKf-zDfq12SOdN7Ej5AiBCgvcUvLUGqGoMBnc0NIQtDeNM8ETJD2lTt9Bi7T186g%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "video/mp4; codecs=\"avc1.64001F, mp4a.40.2\"",
                        "quality": "hd720",
                        "itag": 22,
                        "bitrate": 1340380,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=315&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=video%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=1648069666&dur=634.566&lmt=1544611995945231&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5532432&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgGaJmx70EkBCsfAYOI1lI695hXnFSEn-ZAfRiqWrnt9ACIQClBT5YZlou5ttgFzKnLZkUKxjZznxMJGPTNvtXCAlebw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "video/webm; codecs=\"vp9\"",
                        "quality": "hd2160",
                        "itag": 315,
                        "bitrate": 26416339,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=308&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=video%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=627075264&dur=634.566&lmt=1544611159960793&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5532432&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALl1_ksmnpBhD49Hgjdg-z-Y4H2AL8hBx63ephvsvhbCAiAFrqyy65MimA4mCXYQBopP67G9dtwH9xyjHS_0hZ-rJA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "video/webm; codecs=\"vp9\"",
                        "quality": "hd1440",
                        "itag": 308,
                        "bitrate": 13381315,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=134&aitags=133%2C134%2C135%2C136%2C160%2C242%2C243%2C244%2C247%2C278%2C298%2C299%2C302%2C303%2C308%2C315%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=video%2Fmp4&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=26072934&dur=634.566&lmt=1544609325917976&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5532432&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAKT9N5EmUz3OQOc9IA8P1CuYgzPStz4ulJvCkA8Y1Cf4AiEAwwC2mCjOFWD5jFhAu8g0O6EF5fYJ7HmwskN1sjqTHlA%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "video/mp4; codecs=\"avc1.4d401e\"",
                        "quality": "medium",
                        "itag": 134,
                        "bitrate": 723888,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=249&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=audio%2Fwebm&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=3936299&dur=634.601&lmt=1544629945028066&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5511222&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAJ_UffgeslE26GFwlMZHBsW-zYLcnanMqrvESdjWoupYAiAH7KlvQlYsokTVCCcD7jflD21Fjiim28qNzhOKZ88D3Q%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "audio/webm; codecs=\"opus\"",
                        "quality": "tiny",
                        "itag": 249,
                        "bitrate": 57976,
                        "is_otf": false
                    },
                    {
                        "url": "https://r6---sn-gwpa-5bgk.googlevideo.com/videoplayback?expire=1610798125&ei=zX8CYITXEIGKz7sP9MWL0AE&ip=2409%3A4053%3A803%3A2b22%3Adc68%3Adfb9%3Aa676%3A26a3&id=o-APBakKSE2_eMDMegtCmeWXfuhhUfAzJTmOCWj4lkEjAM&itag=258&source=youtube&requiressl=yes&mh=aP&mm=31%2C29&mn=sn-gwpa-5bgk%2Csn-gwpa-qxad&ms=au%2Crdu&mv=m&mvi=6&pl=36&initcwndbps=146250&vprv=1&mime=audio%2Fmp4&ns=ULL4mkMO31KDtEhOjkOrmpkF&gir=yes&clen=30769612&dur=634.666&lmt=1544629837561969&mt=1610776131&fvip=6&keepalive=yes&c=WEB&txp=5511222&n=uEjSqtzBZaJyVn&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAP6XrnFm3AHxyk8xjU6mJLdVN-uWLl1ItHk5_ONUiRuPAiEAlEYQBsOoEraFemkJIL7OMyHL9aszxW4CbDlxro-AY3Q%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPmhL745RYeL_ffgUJk_xJLC-8riXKMylLTLA_pITYWWAiB2qUIXur8ThW7cLfQ73mIVK61mMZc2ncK6FZWjUHGcUw%3D%3D",
                        "type": "audio/mp4; codecs=\"mp4a.40.2\"",
                        "quality": "tiny",
                        "itag": 258,
                        "bitrate": 390017,
                        "is_otf": false
                    }
                ]
            }
        '''
        self._getDecipheredURLs(videoFormats)
        return {"streams": self._streams}
