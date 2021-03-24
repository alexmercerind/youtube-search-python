import copy
from youtubesearchpython.internal.extras import *
from youtubesearchpython.internal.constants import *

class Video(VideoInternal):
    @staticmethod
    def get(videoLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches information and formats  for the given video link or ID.
        Returns None if video is unavailable.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.get("E07s5ZYygMg", mode = ResultMode.dict)
            >>> print(video)
            {
                "id": "E07s5ZYygMg",
                "title": "Harry Styles - Watermelon Sugar (Official Video)",
                "viewCount": {
                    "text": "170389228"
                },
                "thumbnails": [
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCT6nkbmYf-zbqAFgzF0D9PUhtsOQ",
                        "width": 168,
                        "height": 94
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA-JdoctyNp4aaj9dVtR0c6l5RDVw",
                        "width": 196,
                        "height": 110
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBquHs9OWY5Dy1nE_syglwKP6-pMw",
                        "width": 246,
                        "height": 138
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDSjHwdHxt9aU8NTojucGLp4PurTA",
                        "width": 336,
                        "height": 188
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/maxresdefault.jpg?v=5ebedc0c",
                        "width": 1920,
                        "height": 1080
                    }
                ],
                "description": "This video is dedicated to touching. Listen to Harry Styles\u2019 new album \u2018Fine Line\u2019 now: https://HStyles.lnk.to/FineLineAY   Follow Harry Styles: Facebook: https://HarryStyles.lnk.to/followFI Instagram: https://HarryStyles.lnk.to/followII Twitter: https://HarryStyles.lnk.to/followTI Website: https://HarryStyles.lnk.to/followWI Spotify: https://HarryStyles.lnk.to/followSI YouTube: https://HarryStyles.lnk.to/subscribeYD  Lyrics:   Tastes like strawberries On a summer evening And it sounds just like a song I want more berries And that summer feeling It\u2019s so wonderful and warm Breathe me in Breathe me out I don\u2019t know if I could ever go without I\u2019m just thinking out loud I don\u2019t know if I could ever go without   Watermelon sugar high Watermelon sugar high Watermelon sugar high Watermelon sugar high Watermelon sugar   Strawberries On a summer evening Baby, you\u2019re the end of June I want your belly And that summer feeling Getting washed away in you Breathe me in Breathe me out I don\u2019t know if I could ever go without   Watermelon sugar high   I just wanna taste it I just wanna taste it Watermelon sugar high   Tastes like strawberries On a summer evening And it sounds just like a song I want your belly And that summer feeling I don\u2019t know if I could ever go without   Watermelon sugar high   I just wanna taste it I just wanna taste it Watermelon sugar high I just wanna taste it I just wanna taste it Watermelon sugar high   Watermelon Sugar  #HarryStyles #WatermelonSugar #FineLine",
                "channel": {
                    "name": "HarryStylesVEVO",
                    "id": "UCbOCbp5gXL8jigIBZLqMPrw",
                    "link": "https://www.youtube.com/channel/UCbOCbp5gXL8jigIBZLqMPrw"
                },
                "averageRating": 4.9043722,
                "keywords": [
                    "Fine Line",
                    "Harry Styles Fine Line",
                    "New Harry Styles",
                    "Harry Styles Album",
                    "HS2",
                    "One Direction",
                    "Eroda",
                    "HStyles",
                    "HarryStyles",
                    "New HS",
                    "Watermelon",
                    "Sugar",
                    "Watermlon Sugar",
                    "Harry Styles Watermelon Sugar",
                    "Fine Line Watermelon Sugar",
                    "Watermelon Sugar Fine Line",
                    "Harry Styles Watermelon Sguar Official Audio",
                    "Harry Styles Watermelon Sugar Song",
                    "HS Watermelon Sugar",
                    "Harry Styles Watermelon Sugar Video",
                    "Harry Styles Watermelon Sugar Official Video",
                    "Harry"
                ],
                "publishDate": "2020-05-18",
                "uploadDate": "2020-05-18",
                "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
                "streamingData": {
                    "expiresInSeconds": "21540",
                    "formats": [
                        {
                            "itag": 18,
                            "mimeType": "video/mp4; codecs=\"avc1.42001E, mp4a.40.2\"",
                            "bitrate": 635291,
                            "width": 640,
                            "height": 360,
                            "lastModified": "1594495537943093",
                            "contentLength": "14993923",
                            "quality": "medium",
                            "fps": 24,
                            "qualityLabel": "360p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 635096,
                            "audioQuality": "AUDIO_QUALITY_LOW",
                            "approxDurationMs": "188871",
                            "audioSampleRate": "44100",
                            "audioChannels": 2,
                            "signatureCipher": "s=%3D%3D%3D%3DQodOF5O8RrqTn2rAkcM8v_YNimZ3DfiiO8ZPw9KyyeSBiASFkFP5N0jiMesLzywq2YSWUDXD5Z6lrU9gubyH9Go_MAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DVfvQKqQ_NZHn6Dor7spmHhEF%26gir%3Dyes%26clen%3D14993923%26ratebypass%3Dyes%26dur%3D188.871%26lmt%3D1594495537943093%26mt%3D1610773720%26fvip%3D7%26beids%3D23886208%26c%3DWEB%26txp%3D5531432%26n%3DWJb1Ck1hxc089s%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgMhVOt4fvPig34e70PugZ4fF9_eaMIxFjkxoViFq_o7QCIHOuwB1qTokkaSC_SRacI2M1ThRYliS_9grHyI5qyZMS"
                        }
                    ],
                    "adaptiveFormats": [
                        {
                            "itag": 396,
                            "mimeType": "video/mp4; codecs=\"av01.0.01M.08\"",
                            "bitrate": 382566,
                            "width": 640,
                            "height": 360,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609487253789141",
                            "contentLength": "6728270",
                            "quality": "medium",
                            "fps": 24,
                            "qualityLabel": "360p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 285076,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3Dk%3DkdR4btYwFQpMSXtob0p2mPKAXiWMK-RwiWxxIt5LWu2AEiAL2zMdQnSgnygDbjo9yzBHDJxs-xM8C6T3kjsh6awJQOAhIgAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D396%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D6728270%26dur%3D188.813%26lmt%3D1609487253789141%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhANojIwQjR-uyA0up-8AVzVVmluYtBAUv7-xfcVLx78VWAiEA70Nv2CCMerX-aagqEvaYtfvWlJnxfIrXbrNh6-9Jlqw%253D"
                        },
                        {
                            "itag": 133,
                            "mimeType": "video/mp4; codecs=\"avc1.4d4015\"",
                            "bitrate": 305779,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "738"
                            },
                            "indexRange": {
                                "start": "739",
                                "end": "1226"
                            },
                            "lastModified": "1601811623766061",
                            "contentLength": "4866855",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 206208,
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3Dws707EGUqrkpRbQj1iDJx96vnuQ3Pdpyw_htdH4w4QvBiAn-2tm8pntaCUkaYr9xiHrb4lmcGfYyhtAebKdghPsGIAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D133%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D4866855%26dur%3D188.813%26lmt%3D1601811623766061%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5535432%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgb0GIgg73jyyDh_JXbJEHYHpNgLpeGa92-oy7wr-WoLcCIQDjOTwDMClu68TTAo5e09v-6mGnnk-g3XypBrPbPHmiLA%253D%253D"
                        },
                        {
                            "itag": 242,
                            "mimeType": "video/webm; codecs=\"vp9\"",
                            "bitrate": 227782,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "218"
                            },
                            "indexRange": {
                                "start": "219",
                                "end": "837"
                            },
                            "lastModified": "1594499983390711",
                            "contentLength": "4309129",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 182577,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3Dg%3Dgwb9JzjrAAoXMNBLNQ5qD2iPHnJ4YzENIdt3mbm44OyAEiAzwBK8Zyqox-LOCWIQYKqubPgZxkUzUWZplemU0D6-QPAhIgAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D242%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D4309129%26dur%3D188.813%26lmt%3D1594499983390711%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5535432%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAKi5zlxKb1XGoMRCFAqs3dS9YUzyLPOHyWxDvZD0tHNRAiEAhE-TFI9B_K_oL0ButpdTjJyx01WaC4axvEGcnAL8SaI%253D"
                        },
                        {
                            "itag": 395,
                            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
                            "bitrate": 182316,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609496650516481",
                            "contentLength": "3387984",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 143548,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3DQ7tMYTeWztx_qFnE9iEOGgHx3wUENk2RY17qdu8FlWVDQICEBt2q4X76zIMwAwS3rCLv4Tvh7rzvEmhokR3o1siuLBgIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D395%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D3387984%26dur%3D188.813%26lmt%3D1609496650516481%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgflPTDLTISSYw4YCfRfUC9QIXUHap_ozlFzKQY2Bw_C0CIQC5ew2MDaI5VmSLOKWu3DgwLLMOXEvVrDWML-NeSicHuw%253D%253D"
                        }
                        {
                            "itag": 394,
                            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
                            "bitrate": 82683,
                            "width": 256,
                            "height": 144,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609493305821258",
                            "contentLength": "1659821",
                            "quality": "tiny",
                            "fps": 24,
                            "qualityLabel": "144p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 70326,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3DACyTUDBvASFI8Ffxayro2mbZkq635OC5aYXXRc2kRfoAiAfc3-OE7SvRgrsjDiCcCriEaeEsaS1NMDNr5M2b_8PHIAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D394%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D1659821%26dur%3D188.813%26lmt%3D1609493305821258%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhALudpHTWdYjzD8IWi9i3ksOL4Ks41vD4P3fQJy42gvU_AiEA5einGPLuqholaqIuBiyFH292aMcRL6bZTeqxEed6So8%253D"
                        }
                    ]
                }
        '''
        return Video(videoLink, None, mode).result
    
    @staticmethod
    def getInfo(videoLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches only information for the given video link or ID.
        Returns None if video is unavailable.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.getInfo("E07s5ZYygMg")
            >>> print(video)
            {
                "id": "E07s5ZYygMg",
                "title": "Harry Styles - Watermelon Sugar (Official Video)",
                "viewCount": {
                    "text": "170389228"
                },
                "thumbnails": [
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCT6nkbmYf-zbqAFgzF0D9PUhtsOQ",
                        "width": 168,
                        "height": 94
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA-JdoctyNp4aaj9dVtR0c6l5RDVw",
                        "width": 196,
                        "height": 110
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBquHs9OWY5Dy1nE_syglwKP6-pMw",
                        "width": 246,
                        "height": 138
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDSjHwdHxt9aU8NTojucGLp4PurTA",
                        "width": 336,
                        "height": 188
                    },
                    {
                        "url": "https://i.ytimg.com/vi/E07s5ZYygMg/maxresdefault.jpg?v=5ebedc0c",
                        "width": 1920,
                        "height": 1080
                    }
                ],
                "description": "This video is dedicated to touching. Listen to Harry Styles\u2019 new album \u2018Fine Line\u2019 now: https://HStyles.lnk.to/FineLineAY   Follow Harry Styles: Facebook: https://HarryStyles.lnk.to/followFI Instagram: https://HarryStyles.lnk.to/followII Twitter: https://HarryStyles.lnk.to/followTI Website: https://HarryStyles.lnk.to/followWI Spotify: https://HarryStyles.lnk.to/followSI YouTube: https://HarryStyles.lnk.to/subscribeYD  Lyrics:   Tastes like strawberries On a summer evening And it sounds just like a song I want more berries And that summer feeling It\u2019s so wonderful and warm Breathe me in Breathe me out I don\u2019t know if I could ever go without I\u2019m just thinking out loud I don\u2019t know if I could ever go without   Watermelon sugar high Watermelon sugar high Watermelon sugar high Watermelon sugar high Watermelon sugar   Strawberries On a summer evening Baby, you\u2019re the end of June I want your belly And that summer feeling Getting washed away in you Breathe me in Breathe me out I don\u2019t know if I could ever go without   Watermelon sugar high   I just wanna taste it I just wanna taste it Watermelon sugar high   Tastes like strawberries On a summer evening And it sounds just like a song I want your belly And that summer feeling I don\u2019t know if I could ever go without   Watermelon sugar high   I just wanna taste it I just wanna taste it Watermelon sugar high I just wanna taste it I just wanna taste it Watermelon sugar high   Watermelon Sugar  #HarryStyles #WatermelonSugar #FineLine",
                "channel": {
                    "name": "HarryStylesVEVO",
                    "id": "UCbOCbp5gXL8jigIBZLqMPrw",
                    "link": "https://www.youtube.com/channel/UCbOCbp5gXL8jigIBZLqMPrw"
                },
                "averageRating": 4.9043722,
                "keywords": [
                    "Fine Line",
                    "Harry Styles Fine Line",
                    "New Harry Styles",
                    "Harry Styles Album",
                    "HS2",
                    "One Direction",
                    "Eroda",
                    "HStyles",
                    "HarryStyles",
                    "New HS",
                    "Watermelon",
                    "Sugar",
                    "Watermlon Sugar",
                    "Harry Styles Watermelon Sugar",
                    "Fine Line Watermelon Sugar",
                    "Watermelon Sugar Fine Line",
                    "Harry Styles Watermelon Sguar Official Audio",
                    "Harry Styles Watermelon Sugar Song",
                    "HS Watermelon Sugar",
                    "Harry Styles Watermelon Sugar Video",
                    "Harry Styles Watermelon Sugar Official Video",
                    "Harry"
                ],
                "publishDate": "2020-05-18",
                "uploadDate": "2020-05-18",
                "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
            }
        '''
        return Video(videoLink, "getInfo", mode).result

    @staticmethod
    def getFormats(videoLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches formats  for the given video link or ID.
        Returns None if video is unavailable.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.getFormats("E07s5ZYygMg", mode = ResultMode.dict)
            >>> print(video)
            {
                "streamingData": {
                    "expiresInSeconds": "21540",
                    "formats": [
                        {
                            "itag": 18,
                            "mimeType": "video/mp4; codecs=\"avc1.42001E, mp4a.40.2\"",
                            "bitrate": 635291,
                            "width": 640,
                            "height": 360,
                            "lastModified": "1594495537943093",
                            "contentLength": "14993923",
                            "quality": "medium",
                            "fps": 24,
                            "qualityLabel": "360p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 635096,
                            "audioQuality": "AUDIO_QUALITY_LOW",
                            "approxDurationMs": "188871",
                            "audioSampleRate": "44100",
                            "audioChannels": 2,
                            "signatureCipher": "s=%3D%3D%3D%3DQodOF5O8RrqTn2rAkcM8v_YNimZ3DfiiO8ZPw9KyyeSBiASFkFP5N0jiMesLzywq2YSWUDXD5Z6lrU9gubyH9Go_MAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DVfvQKqQ_NZHn6Dor7spmHhEF%26gir%3Dyes%26clen%3D14993923%26ratebypass%3Dyes%26dur%3D188.871%26lmt%3D1594495537943093%26mt%3D1610773720%26fvip%3D7%26beids%3D23886208%26c%3DWEB%26txp%3D5531432%26n%3DWJb1Ck1hxc089s%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgMhVOt4fvPig34e70PugZ4fF9_eaMIxFjkxoViFq_o7QCIHOuwB1qTokkaSC_SRacI2M1ThRYliS_9grHyI5qyZMS"
                        }
                    ],
                    "adaptiveFormats": [
                        {
                            "itag": 396,
                            "mimeType": "video/mp4; codecs=\"av01.0.01M.08\"",
                            "bitrate": 382566,
                            "width": 640,
                            "height": 360,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609487253789141",
                            "contentLength": "6728270",
                            "quality": "medium",
                            "fps": 24,
                            "qualityLabel": "360p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 285076,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3Dk%3DkdR4btYwFQpMSXtob0p2mPKAXiWMK-RwiWxxIt5LWu2AEiAL2zMdQnSgnygDbjo9yzBHDJxs-xM8C6T3kjsh6awJQOAhIgAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D396%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D6728270%26dur%3D188.813%26lmt%3D1609487253789141%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhANojIwQjR-uyA0up-8AVzVVmluYtBAUv7-xfcVLx78VWAiEA70Nv2CCMerX-aagqEvaYtfvWlJnxfIrXbrNh6-9Jlqw%253D"
                        },
                        {
                            "itag": 133,
                            "mimeType": "video/mp4; codecs=\"avc1.4d4015\"",
                            "bitrate": 305779,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "738"
                            },
                            "indexRange": {
                                "start": "739",
                                "end": "1226"
                            },
                            "lastModified": "1601811623766061",
                            "contentLength": "4866855",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 206208,
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3Dws707EGUqrkpRbQj1iDJx96vnuQ3Pdpyw_htdH4w4QvBiAn-2tm8pntaCUkaYr9xiHrb4lmcGfYyhtAebKdghPsGIAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D133%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D4866855%26dur%3D188.813%26lmt%3D1601811623766061%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5535432%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgb0GIgg73jyyDh_JXbJEHYHpNgLpeGa92-oy7wr-WoLcCIQDjOTwDMClu68TTAo5e09v-6mGnnk-g3XypBrPbPHmiLA%253D%253D"
                        },
                        {
                            "itag": 242,
                            "mimeType": "video/webm; codecs=\"vp9\"",
                            "bitrate": 227782,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "218"
                            },
                            "indexRange": {
                                "start": "219",
                                "end": "837"
                            },
                            "lastModified": "1594499983390711",
                            "contentLength": "4309129",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 182577,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3Dg%3Dgwb9JzjrAAoXMNBLNQ5qD2iPHnJ4YzENIdt3mbm44OyAEiAzwBK8Zyqox-LOCWIQYKqubPgZxkUzUWZplemU0D6-QPAhIgAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D242%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D4309129%26dur%3D188.813%26lmt%3D1594499983390711%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5535432%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAKi5zlxKb1XGoMRCFAqs3dS9YUzyLPOHyWxDvZD0tHNRAiEAhE-TFI9B_K_oL0ButpdTjJyx01WaC4axvEGcnAL8SaI%253D"
                        },
                        {
                            "itag": 395,
                            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
                            "bitrate": 182316,
                            "width": 426,
                            "height": 240,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609496650516481",
                            "contentLength": "3387984",
                            "quality": "small",
                            "fps": 24,
                            "qualityLabel": "240p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 143548,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3DQ7tMYTeWztx_qFnE9iEOGgHx3wUENk2RY17qdu8FlWVDQICEBt2q4X76zIMwAwS3rCLv4Tvh7rzvEmhokR3o1siuLBgIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D395%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D3387984%26dur%3D188.813%26lmt%3D1609496650516481%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgflPTDLTISSYw4YCfRfUC9QIXUHap_ozlFzKQY2Bw_C0CIQC5ew2MDaI5VmSLOKWu3DgwLLMOXEvVrDWML-NeSicHuw%253D%253D"
                        }
                        {
                            "itag": 394,
                            "mimeType": "video/mp4; codecs=\"av01.0.00M.08\"",
                            "bitrate": 82683,
                            "width": 256,
                            "height": 144,
                            "initRange": {
                                "start": "0",
                                "end": "699"
                            },
                            "indexRange": {
                                "start": "700",
                                "end": "1187"
                            },
                            "lastModified": "1609493305821258",
                            "contentLength": "1659821",
                            "quality": "tiny",
                            "fps": 24,
                            "qualityLabel": "144p",
                            "projectionType": "RECTANGULAR",
                            "averageBitrate": 70326,
                            "colorInfo": {
                                "primaries": "COLOR_PRIMARIES_BT709",
                                "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                                "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                            },
                            "approxDurationMs": "188813",
                            "signatureCipher": "s=%3D%3D%3D%3DACyTUDBvASFI8Ffxayro2mbZkq635OC5aYXXRc2kRfoAiAfc3-OE7SvRgrsjDiCcCriEaeEsaS1NMDNr5M2b_8PHIAhIQAw8JQ0qRORO&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1610795853%26ei%3D7XYCYPjqL86L3LUPsuqOwAw%26ip%3D2409%253A4053%253A803%253A2b22%253Adc68%253Adfb9%253Aa676%253A26a3%26id%3Do-AABrI6NBWfT4rkPYNA8z0KQ_le3lQiAHSFem5FtT8eBq%26itag%3D394%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pl%3D36%26gcr%3Din%26initcwndbps%3D151250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dm85HcnnYCRMEVrPeHkFE5QgF%26gir%3Dyes%26clen%3D1659821%26dur%3D188.813%26lmt%3D1609493305821258%26mt%3D1610773720%26fvip%3D7%26keepalive%3Dyes%26beids%3D23886208%26c%3DWEB%26txp%3D5532434%26n%3Dfg3i3LCZK719E3%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhALudpHTWdYjzD8IWi9i3ksOL4Ks41vD4P3fQJy42gvU_AiEA5einGPLuqholaqIuBiyFH292aMcRL6bZTeqxEed6So8%253D"
                        }
                    ]
                }
            }
        '''
        return Video(videoLink, "getFormats", mode).result



class Playlist:
    '''Fetches information and videos for the given playlist link.
    Returns None if playlist is unavailable.

    The information of the playlist can be accessed in the `info` field of the class.
    And the retrieved videos of the playlist are present inside the `videos` field of the class, as a list.

    Due to limit of being able to retrieve only 100 videos at a time, call `getNextVideos` method to get more videos of the playlist,
    which will be appended to the `videos` list.

    `hasMoreVideos` stores boolean to indicate whether more videos are present in the playlist.
    If this field is True, then you can call `getNextVideos` method again to get more videos of the playlist.

    Args:
        playlistLink (str): link of the playlist on YouTube.
    '''
    __playlist = None
    videos = []
    info = None
    hasMoreVideos = False

    def __init__(self, playlistLink: str):
        self.__playlist = PlaylistInternal(playlistLink, None, ResultMode.dict)
        self.info = copy.deepcopy(self.__playlist.playlistComponent)
        self.videos = self.__playlist.playlistComponent['videos']
        self.hasMoreVideos = self.__playlist.continuationKey != None
        self.info.pop('videos')

    '''Fetches more susequent videos of the playlist, and appends to the `videos` list.
    `hasMoreVideos` bool indicates whether more videos can be fetched or not.
    '''
    def getNextVideos(self) -> None:
        self.__playlist.next()
        self.videos = self.__playlist.playlistComponent['videos']
        self.hasMoreVideos = self.__playlist.continuationKey != None

    @staticmethod
    def get(playlistLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches information and videos for the given playlist link.
        Returns None if playlist is unavailable.

        Args:
            playlistLink (str): link of the playlist on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> playlist = Playlist.get("https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK", mode = ResultMode.dict)
            >>> print(playlist)
            {
                "id": "PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
                "title": "🔥 NCS: House",
                "videoCount": "209",
                "viewCount": "155,772,054 views",
                "thumbnails": {
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDHZYoB-WNHmvT3CZy6SpdqygsO4A",
                            "width": 168,
                            "height": 94
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLACCxCIRvCn65_OS1z_4tLAq5Jb8Q",
                            "width": 196,
                            "height": 110
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBt00cYTIVBdrnHsSNLinhq7meCpQ",
                            "width": 246,
                            "height": 138
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBFaqqO6kCAuqya1SIJo5Cf45Ndxg",
                            "width": 336,
                            "height": 188
                        }
                    ]
                },
                "link": "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
                "channel": {
                    "name": "NoCopyrightSounds",
                    "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                    "thumbnails": [
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s48-c-k-c0x00ffffff-no-rj",
                            "width": 48,
                            "height": 48
                        },
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s88-c-k-c0x00ffffff-no-rj",
                            "width": 88,
                            "height": 88
                        },
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s176-c-k-c0x00ffffff-no-rj",
                            "width": 176,
                            "height": 176
                        }
                    ],
                    "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                },
                "videos": [
                    {
                        "id": "0oq2Ej36nlY",
                        "title": "Axol - Mars [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLAYA8xOuVJyq4ZdmdZEy3128mkHSg",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBVen9Zle-8QDR10u73EEHbHc_MAQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBFv2xNC53WtsAQahBV1kRW2knJ2w",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBMkco75LBzq-XCblRqQZkcFbDf4w",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:56",
                        "accessibility": {
                            "title": "Axol - Mars [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 56 seconds",
                            "duration": "2 minutes, 56 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=0oq2Ej36nlY"
                    },
                    {
                        "id": "iv7ZJecuu_o",
                        "title": "NIVIRO - The Floor Is Lava [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCkw6PB0tE3tROCegrF7uPK0tHM4w",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDxeEJ7qhh1Du1V2GiStjP0XGTniQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLB_0R_xsvuIqYr30BgvOdcHsSCoUQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCcr_u0591ANz4Mes7MCECuvRikUA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:16",
                        "accessibility": {
                            "title": "NIVIRO - The Floor Is Lava [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 16 seconds",
                            "duration": "3 minutes, 16 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=iv7ZJecuu_o"
                    },
                    {
                        "id": "cmVdgWL5548",
                        "title": "Raven & Kreyn - So Happy [NCS Official Video]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBa3HKnW5uNkAP25X5668d5Yxx_GQ",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBghyhFRtdIWD4AT3BZBuOhlzB4JA",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDgYP3wdhqlhDEMPuAW6vMt415fIQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD94rVwtv3iglKBdtQ_oKtxZT1iJA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:41",
                        "accessibility": {
                            "title": "Raven & Kreyn - So Happy [NCS Official Video] by NoCopyrightSounds 3 years ago 2 minutes, 41 seconds",
                            "duration": "2 minutes, 41 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=cmVdgWL5548"
                    },
                    {
                        "id": "ldDCHrBeOlg",
                        "title": "Phantom Sage - Kingdom (feat. Miss Lina) [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDFrVolfV84PcVgXzpjZNaxJqqTyw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDEOg15NmmhCRL9_lQQmK-6axAqyw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDt3q3px1x8SQ8flQYJebkg9fef5g",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBB0B2f0D7RuCc420npQdZpYGb7QQ",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "4:39",
                        "accessibility": {
                            "title": "Phantom Sage - Kingdom (feat. Miss Lina) [NCS Release] by NoCopyrightSounds 3 years ago 4 minutes, 39 seconds",
                            "duration": "4 minutes, 39 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=ldDCHrBeOlg"
                    },
                    {
                        "id": "PhzDIABahyc",
                        "title": "Jensation - Delicious [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBwntSl_7Buk4Udzrvko_zJ4nQf8Q",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCUyQIjjZ0eA5ZgHfBXZOYdDtfHGQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBQKS12wSDYhcIBYFeBjiT1VQLSxQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAE72b5ac2xa9x1ccrKiXsFQwsACA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:49",
                        "accessibility": {
                            "title": "Jensation - Delicious [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 49 seconds",
                            "duration": "2 minutes, 49 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=PhzDIABahyc"
                    },
                    {
                        "id": "Y5TnYaZ31b0",
                        "title": "Waysons - Running [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLAEY6qDwWgh6QjKsRN_hB92IiZlMw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLATd9F2LOxmWU7cirUbLqwTfq75xg",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCBDUIuqcX7vg17NY21ykR8JNyd3A",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCBXImJda2jfUE9_L10N5KJLsQTuA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:08",
                        "accessibility": {
                            "title": "Waysons - Running [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 8 seconds",
                            "duration": "3 minutes, 8 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=Y5TnYaZ31b0"
                    },
                    {
                        "id": "2Nv5juZKhKo",
                        "title": "NIVIRO - You [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCBLGyqDfAqaZ3nTk15H4k7EhAaxg",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCoyqiY8380ua84NIqVNaDDn6zecg",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCxW4Qnr1k3EE5MWbuJlThIm02oYg",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBDOvAvcUtCAVB519ww32RtplBkNw",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:50",
                        "accessibility": {
                            "title": "NIVIRO - You [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 50 seconds",
                            "duration": "3 minutes, 50 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=2Nv5juZKhKo"
                    },
                    {
                        "id": "odThebFOFVg",
                        "title": "Elektronomia - The Other Side [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDhut1THu5o6SRzgEfCmEURV3ob7Q",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBkgcLev1knPC0x_aWkEjsKj8HMpA",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDhHu2Y4U_b05FEskx70NHqnReNFw",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD1FR4CWnJbkrWD_QsVWEpjq_CzjQ",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "4:11",
                        "accessibility": {
                            "title": "Elektronomia - The Other Side [NCS Release] by NoCopyrightSounds 3 years ago 4 minutes, 11 seconds",
                            "duration": "4 minutes, 11 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=odThebFOFVg"
                    },
                    {
                        "id": "9phWj3Iygq8",
                        "title": "Raven & Kreyn - Get This Party [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBxD8ouCe61I6X4oiHQhPjmu7G8rw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDRVh4TEJG0WTAWz-LnFPjQQxhQaw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLARKdRufUYSduQ3IPGO831vvoQ_8w",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAuGbI8xMrYBZ46shlinaj7Na9chg",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:39",
                        "accessibility": {
                            "title": "Raven & Kreyn - Get This Party [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 39 seconds",
                            "duration": "2 minutes, 39 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=9phWj3Iygq8"
                    },
                    {
                        "id": "dM2hrLwdaoU",
                        "title": "Distrion & Alex Skrindo - Lightning [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDuprc64g80t_DXa9UE5SrzLEkAdw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA3bgMR8b2UKtbCpbYzSmsLhgTK7g",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLB3LNf1rjgiGHtMa7UH9cQ9B29-yQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBXvevJvz3sTF4ZjpunveJF8Z-gSg",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:27",
                        "accessibility": {
                            "title": "Distrion & Alex Skrindo - Lightning [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 27 seconds",
                            "duration": "3 minutes, 27 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=dM2hrLwdaoU"
                    },
                    {
                        "id": "vKAHowm3Ry0",
                        "title": "Kontinuum - Lost (feat. Savoi) [Sunroof Remix] | NCS Release",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC4BvoPiuOIA_mTbacI2BobXfm8gA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDOmyUcbQL2EffQm7T19yI9FIe89w",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBsI7UIpQCI3Ty6CJxL1R4wRF2EqQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBJivP3UVcYXjkKjdTYLKJO7L329g",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:02",
                        "accessibility": {
                            "title": "Kontinuum - Lost (feat. Savoi) [Sunroof Remix] | NCS Release by NoCopyrightSounds 3 years ago 3 minutes, 2 seconds",
                            "duration": "3 minutes, 2 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=vKAHowm3Ry0"
                    },
                    {
                        "id": "FseAiTb8Se0",
                        "title": "Kovan & Electro-Light - Skyline [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBQ5gJjpS6VprS0z0SxgZxEVxGaJA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC5oJlZLpCbxAxQHUceUuVIvUKNSw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDyWw_4fzlujqrtOT90Ya6_cpLeFg",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBytsYOYycFUOdBrF47tyEUjnC_-A",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:50",
                        "accessibility": {
                            "title": "Kovan & Electro-Light - Skyline [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 50 seconds",
                            "duration": "3 minutes, 50 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=FseAiTb8Se0"
                    },
                    {
                        "id": "BoI6g46zuU4",
                        "title": "RetroVision & Domastic - SICC [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC-hfMNYvUViQKf8jD1d1XwQDtfNA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDlXueYSIv8fVNN0k4s7CLlJBUw8w",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD2PqxAsUQcuqNP_uxtZDeMaWd5sA",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCNtEtObJdzEJykxkMqkcR6qYin0w",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:46",
                        "accessibility": {
                            "title": "RetroVision & Domastic - SICC [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 46 seconds",
                            "duration": "2 minutes, 46 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=BoI6g46zuU4"
                    }
                ]
            }
        '''
        return Playlist(playlistLink, None, mode).result
    
    @staticmethod
    def getInfo(playlistLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches only information for the given playlist link.
        Returns None if playlist is unavailable.

        Args:
            playlistLink (str): link of the playlist on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> playlist = Playlist.getInfo("https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK", mode = ResultMode.dict)
            >>> print(playlist)
            {
                "id": "PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
                "title": "🔥 NCS: House",
                "videoCount": "209",
                "viewCount": "155,772,054 views",
                "thumbnails": {
                    "thumbnails": [
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCKgBEF5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLDHZYoB-WNHmvT3CZy6SpdqygsO4A",
                            "width": 168,
                            "height": 94
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEWCMQBEG5IWvKriqkDCQgBFQAAiEIYAQ==&rs=AOn4CLACCxCIRvCn65_OS1z_4tLAq5Jb8Q",
                            "width": 196,
                            "height": 110
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBt00cYTIVBdrnHsSNLinhq7meCpQ",
                            "width": 246,
                            "height": 138
                        },
                        {
                            "url": "https://i.ytimg.com/vi/LIvSF0fQPJc/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBFaqqO6kCAuqya1SIJo5Cf45Ndxg",
                            "width": 336,
                            "height": 188
                        }
                    ]
                },
                "link": "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK",
                "channel": {
                    "name": "NoCopyrightSounds",
                    "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                    "thumbnails": [
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s48-c-k-c0x00ffffff-no-rj",
                            "width": 48,
                            "height": 48
                        },
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s88-c-k-c0x00ffffff-no-rj",
                            "width": 88,
                            "height": 88
                        },
                        {
                            "url": "https://yt3.ggpht.com/ytc/AAUvwnhwQpPaPL_w-2bQM3TXQN0bdsQQSeEW74TDNXDfHQ=s176-c-k-c0x00ffffff-no-rj",
                            "width": 176,
                            "height": 176
                        }
                    ],
                    "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                }
            }
        '''
        return Playlist(playlistLink, 'getInfo', mode).result

    @staticmethod
    def getVideos(playlistLink: str, mode: int = ResultMode.dict) -> Union[dict, str, None]:
        '''Fetches only videos in the given playlist from link.
        Returns None if playlist is unavailable.

        Args:
            playlistLink (str): link of the playlist on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> playlist = Playlist.getInfo("https://www.youtube.com/playlist?list=PLRBp0Fe2GpgmsW46rJyudVFlY6IYjFBIK", mode = ResultMode.dict)
            >>> print(playlist)
            {
                "videos": [
                    {
                        "id": "0oq2Ej36nlY",
                        "title": "Axol - Mars [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLAYA8xOuVJyq4ZdmdZEy3128mkHSg",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBVen9Zle-8QDR10u73EEHbHc_MAQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBFv2xNC53WtsAQahBV1kRW2knJ2w",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/0oq2Ej36nlY/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBMkco75LBzq-XCblRqQZkcFbDf4w",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:56",
                        "accessibility": {
                            "title": "Axol - Mars [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 56 seconds",
                            "duration": "2 minutes, 56 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=0oq2Ej36nlY"
                    },
                    {
                        "id": "iv7ZJecuu_o",
                        "title": "NIVIRO - The Floor Is Lava [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCkw6PB0tE3tROCegrF7uPK0tHM4w",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDxeEJ7qhh1Du1V2GiStjP0XGTniQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLB_0R_xsvuIqYr30BgvOdcHsSCoUQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/iv7ZJecuu_o/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCcr_u0591ANz4Mes7MCECuvRikUA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:16",
                        "accessibility": {
                            "title": "NIVIRO - The Floor Is Lava [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 16 seconds",
                            "duration": "3 minutes, 16 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=iv7ZJecuu_o"
                    },
                    {
                        "id": "cmVdgWL5548",
                        "title": "Raven & Kreyn - So Happy [NCS Official Video]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBa3HKnW5uNkAP25X5668d5Yxx_GQ",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBghyhFRtdIWD4AT3BZBuOhlzB4JA",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDgYP3wdhqlhDEMPuAW6vMt415fIQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/cmVdgWL5548/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD94rVwtv3iglKBdtQ_oKtxZT1iJA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:41",
                        "accessibility": {
                            "title": "Raven & Kreyn - So Happy [NCS Official Video] by NoCopyrightSounds 3 years ago 2 minutes, 41 seconds",
                            "duration": "2 minutes, 41 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=cmVdgWL5548"
                    },
                    {
                        "id": "ldDCHrBeOlg",
                        "title": "Phantom Sage - Kingdom (feat. Miss Lina) [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDFrVolfV84PcVgXzpjZNaxJqqTyw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDEOg15NmmhCRL9_lQQmK-6axAqyw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDt3q3px1x8SQ8flQYJebkg9fef5g",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/ldDCHrBeOlg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBB0B2f0D7RuCc420npQdZpYGb7QQ",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "4:39",
                        "accessibility": {
                            "title": "Phantom Sage - Kingdom (feat. Miss Lina) [NCS Release] by NoCopyrightSounds 3 years ago 4 minutes, 39 seconds",
                            "duration": "4 minutes, 39 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=ldDCHrBeOlg"
                    },
                    {
                        "id": "PhzDIABahyc",
                        "title": "Jensation - Delicious [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBwntSl_7Buk4Udzrvko_zJ4nQf8Q",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCUyQIjjZ0eA5ZgHfBXZOYdDtfHGQ",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBQKS12wSDYhcIBYFeBjiT1VQLSxQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/PhzDIABahyc/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAE72b5ac2xa9x1ccrKiXsFQwsACA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:49",
                        "accessibility": {
                            "title": "Jensation - Delicious [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 49 seconds",
                            "duration": "2 minutes, 49 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=PhzDIABahyc"
                    },
                    {
                        "id": "Y5TnYaZ31b0",
                        "title": "Waysons - Running [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLAEY6qDwWgh6QjKsRN_hB92IiZlMw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLATd9F2LOxmWU7cirUbLqwTfq75xg",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCBDUIuqcX7vg17NY21ykR8JNyd3A",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/Y5TnYaZ31b0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCBXImJda2jfUE9_L10N5KJLsQTuA",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:08",
                        "accessibility": {
                            "title": "Waysons - Running [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 8 seconds",
                            "duration": "3 minutes, 8 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=Y5TnYaZ31b0"
                    },
                    {
                        "id": "2Nv5juZKhKo",
                        "title": "NIVIRO - You [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCBLGyqDfAqaZ3nTk15H4k7EhAaxg",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCoyqiY8380ua84NIqVNaDDn6zecg",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCxW4Qnr1k3EE5MWbuJlThIm02oYg",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/2Nv5juZKhKo/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBDOvAvcUtCAVB519ww32RtplBkNw",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:50",
                        "accessibility": {
                            "title": "NIVIRO - You [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 50 seconds",
                            "duration": "3 minutes, 50 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=2Nv5juZKhKo"
                    },
                    {
                        "id": "odThebFOFVg",
                        "title": "Elektronomia - The Other Side [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDhut1THu5o6SRzgEfCmEURV3ob7Q",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBkgcLev1knPC0x_aWkEjsKj8HMpA",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDhHu2Y4U_b05FEskx70NHqnReNFw",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/odThebFOFVg/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD1FR4CWnJbkrWD_QsVWEpjq_CzjQ",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "4:11",
                        "accessibility": {
                            "title": "Elektronomia - The Other Side [NCS Release] by NoCopyrightSounds 3 years ago 4 minutes, 11 seconds",
                            "duration": "4 minutes, 11 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=odThebFOFVg"
                    },
                    {
                        "id": "9phWj3Iygq8",
                        "title": "Raven & Kreyn - Get This Party [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBxD8ouCe61I6X4oiHQhPjmu7G8rw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDRVh4TEJG0WTAWz-LnFPjQQxhQaw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLARKdRufUYSduQ3IPGO831vvoQ_8w",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/9phWj3Iygq8/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAuGbI8xMrYBZ46shlinaj7Na9chg",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:39",
                        "accessibility": {
                            "title": "Raven & Kreyn - Get This Party [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 39 seconds",
                            "duration": "2 minutes, 39 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=9phWj3Iygq8"
                    },
                    {
                        "id": "dM2hrLwdaoU",
                        "title": "Distrion & Alex Skrindo - Lightning [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDuprc64g80t_DXa9UE5SrzLEkAdw",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLA3bgMR8b2UKtbCpbYzSmsLhgTK7g",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLB3LNf1rjgiGHtMa7UH9cQ9B29-yQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/dM2hrLwdaoU/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBXvevJvz3sTF4ZjpunveJF8Z-gSg",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:27",
                        "accessibility": {
                            "title": "Distrion & Alex Skrindo - Lightning [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 27 seconds",
                            "duration": "3 minutes, 27 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=dM2hrLwdaoU"
                    },
                    {
                        "id": "vKAHowm3Ry0",
                        "title": "Kontinuum - Lost (feat. Savoi) [Sunroof Remix] | NCS Release",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC4BvoPiuOIA_mTbacI2BobXfm8gA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDOmyUcbQL2EffQm7T19yI9FIe89w",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBsI7UIpQCI3Ty6CJxL1R4wRF2EqQ",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/vKAHowm3Ry0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBJivP3UVcYXjkKjdTYLKJO7L329g",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:02",
                        "accessibility": {
                            "title": "Kontinuum - Lost (feat. Savoi) [Sunroof Remix] | NCS Release by NoCopyrightSounds 3 years ago 3 minutes, 2 seconds",
                            "duration": "3 minutes, 2 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=vKAHowm3Ry0"
                    },
                    {
                        "id": "FseAiTb8Se0",
                        "title": "Kovan & Electro-Light - Skyline [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLBQ5gJjpS6VprS0z0SxgZxEVxGaJA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC5oJlZLpCbxAxQHUceUuVIvUKNSw",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLDyWw_4fzlujqrtOT90Ya6_cpLeFg",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/FseAiTb8Se0/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBytsYOYycFUOdBrF47tyEUjnC_-A",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "3:50",
                        "accessibility": {
                            "title": "Kovan & Electro-Light - Skyline [NCS Release] by NoCopyrightSounds 3 years ago 3 minutes, 50 seconds",
                            "duration": "3 minutes, 50 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=FseAiTb8Se0"
                    },
                    {
                        "id": "BoI6g46zuU4",
                        "title": "RetroVision & Domastic - SICC [NCS Release]",
                        "thumbnails": [
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLC-hfMNYvUViQKf8jD1d1XwQDtfNA",
                                "width": 168,
                                "height": 94
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEiCMQBEG5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLDlXueYSIv8fVNN0k4s7CLlJBUw8w",
                                "width": 196,
                                "height": 110
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLD2PqxAsUQcuqNP_uxtZDeMaWd5sA",
                                "width": 246,
                                "height": 138
                            },
                            {
                                "url": "https://i.ytimg.com/vi/BoI6g46zuU4/hqdefault.jpg?sqp=-oaymwEjCNACELwBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCNtEtObJdzEJykxkMqkcR6qYin0w",
                                "width": 336,
                                "height": 188
                            }
                        ],
                        "channel": {
                            "name": "NoCopyrightSounds",
                            "id": "UC_aEa8K-EOJ3D6gOs7HcyNg",
                            "link": "https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg"
                        },
                        "duration": "2:46",
                        "accessibility": {
                            "title": "RetroVision & Domastic - SICC [NCS Release] by NoCopyrightSounds 3 years ago 2 minutes, 46 seconds",
                            "duration": "2 minutes, 46 seconds"
                        },
                        "link": "https://www.youtube.com/watch?v=BoI6g46zuU4"
                    }
                ]
            }
        '''
        return Playlist(playlistLink, 'getVideos', mode).result
