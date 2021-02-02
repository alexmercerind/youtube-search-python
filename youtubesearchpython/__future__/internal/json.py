import json
import asyncio

async def dumps(content: dict) -> str:
    loop = asyncio.get_running_loop()
    json = await loop.run_in_executor(None, json.dumps, content)
    return json

async def loads(content: str) -> dict:
    loop = asyncio.get_running_loop()
    dictionary = await loop.run_in_executor(None, json.loads, content)
    return dictionary
