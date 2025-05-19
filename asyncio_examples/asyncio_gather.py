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

    
# main function (run all functions concurrently)
async def main():
    # run all functions concurrently
    await asyncio.gather(fun1(), fun2(), fun3())

# run the main function
if __name__ == "__main__":
    asyncio.run(main())
