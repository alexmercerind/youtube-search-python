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
        '''Fetches only information  for the given video link or ID.
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
