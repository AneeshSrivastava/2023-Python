import asyncio
import random
from time import perf_counter

async def get_vertical_id():
    print(f"Fetching vertical id..")
    vertical_id = random.randint(50,2000)
    await asyncio.sleep(3) # heavy request
    print(f"Got vertical id as '{vertical_id}'!")
    return vertical_id

async def get_asset_details(vertical_id):
    print(f"Getting data for vertical ID: {vertical_id}...")
    asset_id = random.randint(50,2000+1)
    await asyncio.sleep(1)
    print(f"Got response for vertical ID: {vertical_id}!")
    return {'asset_id': asset_id, 'vertical_id': vertical_id, 'asset_data': f'data {asset_id}'}

async def async_function():
    start_time = perf_counter()
    tasks = []
    all_vert_tasks = []
    for i in range(1, 3+1):
        print(f'Working on {i}th task..')
        vertical_task = asyncio.create_task(get_vertical_id())
        all_vert_tasks.append(vertical_task)
    all_verticals =await asyncio.gather(*all_vert_tasks)
    print("")
    for vertical_id in all_verticals:
        task = asyncio.create_task(get_asset_details(vertical_id))
        tasks.append(task)
    final_resp = await asyncio.gather(*tasks)
    end_time = perf_counter()
    total_time = round(end_time - start_time, 2)
    print("")
    print('Async Time', total_time, 'seconds')
    return final_resp