import asyncio

def kk():
    async def watch_serials():
        while True:
            await asyncio.sleep(10)
            print('10 second')

    async def shop_bread():
        while True:
            await asyncio.sleep(10)
            for i in range(10):
                print(i)

    async def cooking_soup():
        task1 = asyncio.create_task(watch_serials())
        task2 = asyncio.create_task(shop_bread())

        await task1
        await task2


    asyncio.run(cooking_soup())
    

