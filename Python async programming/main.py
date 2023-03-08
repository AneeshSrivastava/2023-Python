import asyncio
import async_program as async_module
import sync_program as sync_module

def main():
    print("-"*60)
    all_responses = asyncio.run(async_module.async_function())
    print('async_responses: ', all_responses)
    print("-"*60)
    resp = sync_module.non_async_function()
    print('sync_response: ', resp)
    print("-"*60)



if __name__ == '__main__':
    main()

