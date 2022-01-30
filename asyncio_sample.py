import asyncio
import time

async def main():
    print("bro came and it is working coroutine main output")
    task = asyncio.create_task(foo("murugaraju"))
    task2 = asyncio.create_task(sample())
    task3 = asyncio.create_task(sample2())
    
  
    await asyncio.sleep(2)
    print("after task3")

    await task2
    print(await task, await task3)

    
async def foo(d):
    for i in range(1000):
        print("print foo --->",i)
        await asyncio.sleep(4)


async def sample():
    for i in range(100):
        print("print sample2 --->",i)
        await asyncio.sleep(2)


async def sample2():
    for i in list(range(100))[::-1]:
        print("print sample --->",i)
        await asyncio.sleep(1)
        





loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()