import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

import aiohttp

from penalty import calculate_penalty_for_json
from unmarshaller import unmarshall_to_financial_instruments

async def main_networking():
    async with aiohttp.ClientSession(headers={'Authorization': 'Basic YTph'}) as session:
        async with session.get('http://10.1.7.22:10009/v1/securities') as response:
            print(response.status)
            json: str = await response.text()
            penalty: float = calculate_penalty_for_json(json)
            print(penalty)
            await session.close()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.set_debug(True)
# loop.set_default_executor(ThreadPoolExecutor(os.cpu_count() * 2))
# loop.run_until_complete(main())

asyncio.run(main_networking())