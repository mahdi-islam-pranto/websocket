import asyncio
from datetime import datetime

# functions
async def fun1():
    print("start running fun1")
    # time consuming task
    await asyncio.sleep(2)  # 2 seconds
    # print start time
    print(datetime.now().strftime("%H:%M:%S"))
    print("------fun1-------")
    
async def fun2():
    print("start running fun2")
    # time consuming task
    await asyncio.sleep(3) # 3 seconds
    print(datetime.now().strftime("%H:%M:%S"))
    print("-------fun2------")

async def fun3():
    print("start running fun3")
    # time consuming task
    await asyncio.sleep(3) # 3 seconds
    print(datetime.now().strftime("%H:%M:%S"))
    print("------fun3------")

# main function

async def main():
    task1 = asyncio.create_task(fun1())
    task2 = asyncio.create_task(fun2())
    task3 = asyncio.create_task(fun3())
    await task1
    await task2
    await task3

if __name__ == "__main__":
    asyncio.run(main())