from youtubesearchpython.internal.extras import *
from youtubesearchpython.internal.constants import *

class Video(VideoInternal):
    @staticmethod
    def get(videoLink: str, mode: int = ResultMode.dict):
        '''Fetches information and formats  for the given video link or ID.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.get('E07s5ZYygMg', mode = ResultMode.dict)
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
                "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
                "adaptiveFormats": [
                    {
                        "itag": 137,
                        "mimeType": "video/mp4; codecs=\"avc1.640028\"",
                        "bitrate": 4517689,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "740"
                        },
                        "indexRange": {
                            "start": "741",
                            "end": "1228"
                        },
                        "lastModified": "1601811652909447",
                        "contentLength": "75694686",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 3207181,
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=F%3DX%3DgIkn_MWCUvQZ__3tR_7gPNDBeOz8n9M0WGxNtIZ6zwxAiA-VALQ9F5bz%3DW8I_Z8WfXPLHjEGEn_JRVVu7BcNJJfjKAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D137%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D75694686%26dur%3D188.813%26lmt%3D1601811652909447%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgTGJdeFFnVZy97rzAeBnJCSdcY7KWBCa21RQ9ZvkH0KsCIQD1-Vzcj53p39l_DWtK1b69VjQmtBi_SIZOZD0hzXHJNA%253D%253D"
                    },
                    {
                        "itag": 248,
                        "mimeType": "video/webm; codecs=\"vp9\"",
                        "bitrate": 2677426,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "219"
                        },
                        "indexRange": {
                            "start": "220",
                            "end": "861"
                        },
                        "lastModified": "1594499920972798",
                        "contentLength": "54314997",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 2301324,
                        "colorInfo": {
                            "primaries": "COLOR_PRIMARIES_BT709",
                            "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                            "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                        },
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=4WSWyDZ4VUW0FxNi5blaiF4ilQNYR-3uChA822Y034mMGICMPJy_OPOcgmaH7OjHiz7P3SA11EXoi7xWDBddADzQhXgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D248%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D54314997%26dur%3D188.813%26lmt%3D1594499920972798%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAJHI4m9CrBPc-vEl_qXPYvACMjDAgC7dGWk5cZ5yc4DTAiEA36ijZkSFmCngvJZ5ULpRFJLGB3wWohsxABHZJL_q4_c%253D"
                    },
                    {
                        "itag": 399,
                        "mimeType": "video/mp4; codecs=\"av01.0.08M.08\"",
                        "bitrate": 2252425,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "699"
                        },
                        "indexRange": {
                            "start": "700",
                            "end": "1187"
                        },
                        "lastModified": "1602396935824004",
                        "contentLength": "40536309",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 1717521,
                        "colorInfo": {
                            "primaries": "COLOR_PRIMARIES_BT709",
                            "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                            "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                        },
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=ZJwJxM3AbUoW4wiucKj-hgbD-KpvS21BYBD1lsDZa7SPCICMZo9flYaa2ePw-6CdA1a_DwNtjbk4KXaTb0U1btiIfDgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D399%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D40536309%26dur%3D188.813%26lmt%3D1602396935824004%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgB9Jm-n4o3HkYm1cr2pVG9NLb_7Tmp22lXGwKkWSiwZ0CIBKSMK5PqbPHniDqOFCPoqa4eT_Y8hQDSWM7k_V8A99p"
                    },
                    {
                        "itag": 250,
                        "mimeType": "audio/webm; codecs=\"opus\"",
                        "bitrate": 70403,
                        "initRange": {
                            "start": "0",
                            "end": "258"
                        },
                        "indexRange": {
                            "start": "259",
                            "end": "577"
                        },
                        "lastModified": "1594498110473681",
                        "contentLength": "1518207",
                        "quality": "tiny",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 64316,
                        "audioQuality": "AUDIO_QUALITY_LOW",
                        "approxDurationMs": "188841",
                        "audioSampleRate": "48000",
                        "audioChannels": 2,
                        "loudnessDb": 6.1900001,
                        "signatureCipher": "s=O%3Dg%3DQMHtYOQBw_YLTXlJ8W5xY0ZYms3jL4-fEAqDNZ7V7qAAiAe3sv6PQID8%3Dy5pkYzGrgnFEslUXBF7J5E2RFBMg_yJMAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D250%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D1518207%26dur%3D188.841%26lmt%3D1594498110473681%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAMhseOQnTni1bj-5JVVe4mUAM1oNoUtXOQFVzWRU8GHHAiAYsOo3Dv8r6gEWnCJWJ8sdXFRuD78hghT-33x8cRGI2g%253D%253D"
                    },
                    {
                        "itag": 251,
                        "mimeType": "audio/webm; codecs=\"opus\"",
                        "bitrate": 135695,
                        "initRange": {
                            "start": "0",
                            "end": "258"
                        },
                        "indexRange": {
                            "start": "259",
                            "end": "577"
                        },
                        "lastModified": "1594498099017464",
                        "contentLength": "2933357",
                        "quality": "tiny",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 124267,
                        "audioQuality": "AUDIO_QUALITY_MEDIUM",
                        "approxDurationMs": "188841",
                        "audioSampleRate": "48000",
                        "audioChannels": 2,
                        "loudnessDb": 6.1900001,
                        "signatureCipher": "s=iE1Ev7003kBIMkOGrbRjxXqkm4slwC2pqCY5CJuTxaMqHnAEiAZOk6qgeRcc%3DYgm9kcnF17HeiW_Sjsbna-nN1-3h3SIKAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D251%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D2933357%26dur%3D188.841%26lmt%3D1594498099017464%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAP491Wcaof1Bb3XZxhzH8H5SrvAhR5wh5It1_z-03KPHAiAjP4ZU3ND8aOyEKz32HI1iDA9bku4tuxloXZKBE-Bang%253D%253D"
                    }
                ],
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
                        "signatureCipher": "s=AsPsztt4ZltrQC0ijKLX83bx8smNjCLHwb5D-pJLJvDGAmAEiAhvbstJR8js%3D7g7hscPbPtwrjUDtzwb1GgpkTG53d9kMAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dw-Sn-YFRtfT0kLnFKpo3EA4F%26gir%3Dyes%26clen%3D14993923%26ratebypass%3Dyes%26dur%3D188.871%26lmt%3D1594495537943093%26mt%3D1609499069%26fvip%3D7%26c%3DWEB%26txp%3D5531432%26n%3DV2sNxp4tEzNJkZtb%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgbrfk-x_xucwjZedmoR8sR3UQHP4OUd1jDUL_91palCICIQC0w6urClsmCBTpK27I5DIKKED9T_ci6blRj-c8rSD86A%253D%253D"
                    }
                ],
                "expiresInSeconds": "21540"
            }
        '''
        return Video(videoLink, None, mode).result
    
    @staticmethod
    def getInfo(videoLink: str, mode: int = ResultMode.dict):
        '''Fetches only information  for the given video link or ID.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.getInfo('E07s5ZYygMg')
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
                "link": "https://www.youtube.com/watch?v=E07s5ZYygMg",
            }
        '''
        return Video(videoLink, 'getInfo', mode).result

    @staticmethod
    def getFormats(videoLink: str, mode: int = ResultMode.dict):
        '''Fetches formats  for the given video link or ID.

        Args:
            videoLink (str): link or ID of the video on YouTube.
            mode (int, optional): Sets the type of result. Defaults to ResultMode.dict.

        Examples:

            >>> video = Video.getFormats('E07s5ZYygMg', mode = ResultMode.dict)
            >>> print(video)
            {
                "adaptiveFormats": [
                    {
                        "itag": 137,
                        "mimeType": "video/mp4; codecs=\"avc1.640028\"",
                        "bitrate": 4517689,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "740"
                        },
                        "indexRange": {
                            "start": "741",
                            "end": "1228"
                        },
                        "lastModified": "1601811652909447",
                        "contentLength": "75694686",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 3207181,
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=F%3DX%3DgIkn_MWCUvQZ__3tR_7gPNDBeOz8n9M0WGxNtIZ6zwxAiA-VALQ9F5bz%3DW8I_Z8WfXPLHjEGEn_JRVVu7BcNJJfjKAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D137%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D75694686%26dur%3D188.813%26lmt%3D1601811652909447%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgTGJdeFFnVZy97rzAeBnJCSdcY7KWBCa21RQ9ZvkH0KsCIQD1-Vzcj53p39l_DWtK1b69VjQmtBi_SIZOZD0hzXHJNA%253D%253D"
                    },
                    {
                        "itag": 248,
                        "mimeType": "video/webm; codecs=\"vp9\"",
                        "bitrate": 2677426,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "219"
                        },
                        "indexRange": {
                            "start": "220",
                            "end": "861"
                        },
                        "lastModified": "1594499920972798",
                        "contentLength": "54314997",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 2301324,
                        "colorInfo": {
                            "primaries": "COLOR_PRIMARIES_BT709",
                            "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                            "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                        },
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=4WSWyDZ4VUW0FxNi5blaiF4ilQNYR-3uChA822Y034mMGICMPJy_OPOcgmaH7OjHiz7P3SA11EXoi7xWDBddADzQhXgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D248%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D54314997%26dur%3D188.813%26lmt%3D1594499920972798%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5535432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRgIhAJHI4m9CrBPc-vEl_qXPYvACMjDAgC7dGWk5cZ5yc4DTAiEA36ijZkSFmCngvJZ5ULpRFJLGB3wWohsxABHZJL_q4_c%253D"
                    },
                    {
                        "itag": 399,
                        "mimeType": "video/mp4; codecs=\"av01.0.08M.08\"",
                        "bitrate": 2252425,
                        "width": 1920,
                        "height": 1080,
                        "initRange": {
                            "start": "0",
                            "end": "699"
                        },
                        "indexRange": {
                            "start": "700",
                            "end": "1187"
                        },
                        "lastModified": "1602396935824004",
                        "contentLength": "40536309",
                        "quality": "hd1080",
                        "fps": 24,
                        "qualityLabel": "1080p",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 1717521,
                        "colorInfo": {
                            "primaries": "COLOR_PRIMARIES_BT709",
                            "transferCharacteristics": "COLOR_TRANSFER_CHARACTERISTICS_BT709",
                            "matrixCoefficients": "COLOR_MATRIX_COEFFICIENTS_BT709"
                        },
                        "approxDurationMs": "188813",
                        "signatureCipher": "s=ZJwJxM3AbUoW4wiucKj-hgbD-KpvS21BYBD1lsDZa7SPCICMZo9flYaa2ePw-6CdA1a_DwNtjbk4KXaTb0U1btiIfDgIARw8JQ0qOAAOAA&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D399%26aitags%3D133%252C134%252C135%252C136%252C137%252C160%252C242%252C243%252C244%252C247%252C248%252C278%252C394%252C395%252C396%252C397%252C398%252C399%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D40536309%26dur%3D188.813%26lmt%3D1602396935824004%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Caitags%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRAIgB9Jm-n4o3HkYm1cr2pVG9NLb_7Tmp22lXGwKkWSiwZ0CIBKSMK5PqbPHniDqOFCPoqa4eT_Y8hQDSWM7k_V8A99p"
                    },
                    {
                        "itag": 250,
                        "mimeType": "audio/webm; codecs=\"opus\"",
                        "bitrate": 70403,
                        "initRange": {
                            "start": "0",
                            "end": "258"
                        },
                        "indexRange": {
                            "start": "259",
                            "end": "577"
                        },
                        "lastModified": "1594498110473681",
                        "contentLength": "1518207",
                        "quality": "tiny",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 64316,
                        "audioQuality": "AUDIO_QUALITY_LOW",
                        "approxDurationMs": "188841",
                        "audioSampleRate": "48000",
                        "audioChannels": 2,
                        "loudnessDb": 6.1900001,
                        "signatureCipher": "s=O%3Dg%3DQMHtYOQBw_YLTXlJ8W5xY0ZYms3jL4-fEAqDNZ7V7qAAiAe3sv6PQID8%3Dy5pkYzGrgnFEslUXBF7J5E2RFBMg_yJMAhIARw8JQ0qOAAOAQ&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D250%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D1518207%26dur%3D188.841%26lmt%3D1594498110473681%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAMhseOQnTni1bj-5JVVe4mUAM1oNoUtXOQFVzWRU8GHHAiAYsOo3Dv8r6gEWnCJWJ8sdXFRuD78hghT-33x8cRGI2g%253D%253D"
                    },
                    {
                        "itag": 251,
                        "mimeType": "audio/webm; codecs=\"opus\"",
                        "bitrate": 135695,
                        "initRange": {
                            "start": "0",
                            "end": "258"
                        },
                        "indexRange": {
                            "start": "259",
                            "end": "577"
                        },
                        "lastModified": "1594498099017464",
                        "contentLength": "2933357",
                        "quality": "tiny",
                        "projectionType": "RECTANGULAR",
                        "averageBitrate": 124267,
                        "audioQuality": "AUDIO_QUALITY_MEDIUM",
                        "approxDurationMs": "188841",
                        "audioSampleRate": "48000",
                        "audioChannels": 2,
                        "loudnessDb": 6.1900001,
                        "signatureCipher": "s=iE1Ev7003kBIMkOGrbRjxXqkm4slwC2pqCY5CJuTxaMqHnAEiAZOk6qgeRcc%3DYgm9kcnF17HeiW_Sjsbna-nN1-3h3SIKAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D251%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Daudio%252Fwebm%26ns%3DAmm7Bly72tYhQYuUBTu4ougF%26gir%3Dyes%26clen%3D2933357%26dur%3D188.841%26lmt%3D1594498099017464%26mt%3D1609499069%26fvip%3D7%26keepalive%3Dyes%26c%3DWEB%26txp%3D5531432%26n%3DRBQO4tIQGFK2ymlT%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIhAP491Wcaof1Bb3XZxhzH8H5SrvAhR5wh5It1_z-03KPHAiAjP4ZU3ND8aOyEKz32HI1iDA9bku4tuxloXZKBE-Bang%253D%253D"
                    }
                ],
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
                        "signatureCipher": "s=AsPsztt4ZltrQC0ijKLX83bx8smNjCLHwb5D-pJLJvDGAmAEiAhvbstJR8js%3D7g7hscPbPtwrjUDtzwb1GgpkTG53d9kMAhIARw8JQ0qOAAOAg&sp=sig&url=https://r7---sn-gwpa-5bge.googlevideo.com/videoplayback%3Fexpire%3D1609521167%26ei%3DrwPvX6ayN7GImgel4b2YDg%26ip%3D132.154.228.240%26id%3Do-AB56znPv_llgJ0v0XuIn4mf-4F2feyfn78hi9AowVgJP%26itag%3D18%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DCl%26mm%3D31%252C29%26mn%3Dsn-gwpa-5bge%252Csn-gwpa-qxay%26ms%3Dau%252Crdu%26mv%3Dm%26mvi%3D7%26pcm2cms%3Dyes%26pl%3D19%26gcr%3Din%26initcwndbps%3D156250%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3Dw-Sn-YFRtfT0kLnFKpo3EA4F%26gir%3Dyes%26clen%3D14993923%26ratebypass%3Dyes%26dur%3D188.871%26lmt%3D1594495537943093%26mt%3D1609499069%26fvip%3D7%26c%3DWEB%26txp%3D5531432%26n%3DV2sNxp4tEzNJkZtb%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cgcr%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cratebypass%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpcm2cms%252Cpl%252Cinitcwndbps%26lsig%3DAG3C_xAwRQIgbrfk-x_xucwjZedmoR8sR3UQHP4OUd1jDUL_91palCICIQC0w6urClsmCBTpK27I5DIKKED9T_ci6blRj-c8rSD86A%253D%253D"
                    }
                ],
                "expiresInSeconds": "21540"
            }
        '''
        return Video(videoLink, 'getFormats', mode).result
