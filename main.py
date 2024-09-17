import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

import aiohttp

from unmarshaller import unmarshall_to_financial_instruments

async def main():
    async with aiohttp.ClientSession(headers={'Authorization': 'Basic YTph'}) as session:
        async with session.get(f"http://10.1.7.22:{10009}/v1/securities") as response:
            text_ = await response.text()
            print(text_)
            # objects = parse_json_to_objects(text_)
            # print(objects)
            # print(type(objects))

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.set_debug(True)
# loop.set_default_executor(ThreadPoolExecutor(os.cpu_count() * 2))
loop.run_until_complete(main())

# asyncio.run(main())