import  asyncio

async def work():
    print("start")
    await asyncio.sleep(3)
    print("end")

asyncio.run(work())