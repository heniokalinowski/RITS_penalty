# import requests
#
# from ritApi import trader_get
#
# API_KEY = {'X-API-key': "F2P6KDRK"}
#
# with requests.Session() as ses:
#     ses.headers.update(API_KEY)
#
#     print(trader_get(ses))
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

import aiohttp

from async_client import AsyncClient


async def main2():
    async with aiohttp.ClientSession(headers={'Authorization': 'Basic YTph'}) as session:
        async with session.get(f"http://10.1.7.22:{10009}/v1/limits") as resp:
            print(resp.status)
            print(await resp.text())
            print()

###

async def main3():
    async with aiohttp.ClientSession(headers={'Authorization': 'Basic YTph'}) as session:
        async with session.get(f"http://10.1.7.22:{10009}/v1/securities") as resp:
            print(resp.status)
            print(await resp.text())
            print()

# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# loop.set_debug(True)
# loop.set_default_executor(ThreadPoolExecutor(os.cpu_count() * 2))
# loop.run_until_complete(main2())

asyncio.run(main3())