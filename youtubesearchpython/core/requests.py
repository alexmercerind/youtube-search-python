import httpx

from youtubesearchpython.core.constants import userAgent

class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2

    def syncPostRequest(self) -> httpx.Response:
        print(self.data)
        return httpx.post(self.url, headers={"User-Agent": userAgent}, data=self.data, timeout=self.timeout)

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            r = await client.post(self.url, headers={"User-Agent": userAgent}, data=self.data, timeout=self.timeout)
            return r

    def syncGetRequest(self) -> httpx.Response:
        return httpx.get(self.url, headers={"User-Agent": userAgent}, timeout=self.timeout)

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url, headers={"User-Agent": userAgent}, timeout=self.timeout)
            return r