#!/usr/bin/env python

import asyncio
import datetime
import random

from websockets.asyncio.server import broadcast, serve 

# Set to store all connected clients
CONNECTIONS = set()

async def show_time(websocket):
    # Add new client to connections set
    CONNECTIONS.add(websocket)
    print("New client connected")

    try:

    # Continuously send timestamps to connected clients
        while True:
            message = datetime.datetime.now(tz=datetime.timezone.utc).isoformat() + " From Pranto"
            # broadcast to all clients
        
            # send message to client
            await websocket.send(message)
            await asyncio.sleep(random.random() * 2 + 1)

    finally:
        #  # Remove client from connections when they disconnect
        CONNECTIONS.remove(websocket)
        print("Client disconnected")

async def main():
    async with serve(show_time, "localhost", 5678) as server:
        print("Server started")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())

