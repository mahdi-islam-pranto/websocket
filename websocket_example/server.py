import asyncio
from websockets.asyncio.server import serve

# This function handles each individual WebSocket connection
async def HandleConnection(websocket):
    # Print client connection info
    print(f"New client connected from {websocket.remote_address}")
    name = await websocket.recv()
    print(f"<<< {name}")

    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")

async def main():
    print("Starting server...")
    # Start server
    async with serve(HandleConnection, "localhost", 8765) as server:
        print("Server is running on ws://localhost:8765")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())

