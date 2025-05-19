import asyncio

async def critical_section(lock, data):
    # Using 'async with' to automatically acquire and release the lock
    async with lock:
        # Print when a coroutine acquires the lock
        print(f"Coroutine {data['id']} acquired lock")
        
        # Increment the shared value
        data['value'] += 1
        
        # Simulate some time-consuming work (1 second)
        await asyncio.sleep(1)
        
        # Print when the coroutine releases the lock
        print(f"Coroutine {data['id']} released lock")

async def main():
    # Create a lock object to synchronize access to shared resources
    lock = asyncio.Lock()
    
    # Initialize shared data that will be accessed by multiple coroutines
    shared_data = {'value': 0}
    
    # Create three tasks that will run concurrently
    # Each task runs the critical_section function with a unique ID
    tasks = [
        asyncio.create_task(critical_section(lock, {'id': 1, 'value': shared_data['value']})),
        asyncio.create_task(critical_section(lock, {'id': 2, 'value': shared_data['value']})),
        asyncio.create_task(critical_section(lock, {'id': 3, 'value': shared_data['value']}))
    ]
    
    # Wait for all tasks to complete
    await asyncio.gather(*tasks)
    
    # Print the final value after all coroutines have finished
    print(f"Final value: {shared_data['value']}")

# Entry point of the script
if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())


# This code demonstrates:
# 1. Use of asyncio.Lock() for synchronization
# 2. How to protect critical sections in async code
# 3. Running multiple coroutines concurrently
# 4. Working with shared data in an async environment

# When you run this code, it will:
# - Create 3 coroutines that try to access a shared resource
# - Each coroutine will wait for the lock before proceeding
# - Only one coroutine can execute the critical section at a time
# - Each operation takes 1 second (simulated work)
# - The lock ensures there are no race conditions when accessing shared data
