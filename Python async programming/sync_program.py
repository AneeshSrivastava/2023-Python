import random
from time import sleep
from time import perf_counter, sleep

def get_vertical_id_sync():
    print(f"Fetching vertical id..")
    vertical_id = random.randint(50,2000)
    sleep(3) # heavy request
    print(f"Got vertical id as '{vertical_id}'!")
    
    return vertical_id

def get_asset_details_sync(vertical_id):
    print(f"Getting data for vertical ID: {vertical_id}...")
    asset_id = random.randint(50,2000+1)
    sleep(1)
    print(f"Got response for vertical ID: {vertical_id}!")
    return {'asset_id': asset_id, 'vertical_id': vertical_id, 'asset_data': f'data {asset_id}'}

def non_async_function():
    start_time = perf_counter()
    all_details = []
    for i in range(1, 3+1):
        print("-"*60)
        print(f'Working on {i}th task..')
        vertical_id = get_vertical_id_sync()
        asset_details = get_asset_details_sync(vertical_id)
        all_details.append(asset_details)
    end_time = perf_counter()
    total_time = round(end_time - start_time, 2)
    print('Sync Time', total_time, 'seconds')
    return all_details