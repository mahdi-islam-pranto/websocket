#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import broadcast, serve 

# Set to store all connected clients
CONNECTIONS = set()

async def handle_connection(websocket):
    try:
        # Add new client to connections set
        CONNECTIONS.add(websocket)
        print(f"New client connected. Total clients: {len(CONNECTIONS)}")

        # receive message from client
        async for message in websocket:
            print(f'Received message: {message}')
            # Broadcast this message to all clients
            if len(CONNECTIONS) > 0:
                # Create a copy of connections to avoid modification during iteration
                clients = CONNECTIONS.copy()
                try:
                     if clients:
                        await broadcast(clients, message)
                        print(f"Message broadcast to {len(clients)} clients")
                except Exception as broadcast_error:
                    print(f"Broadcast error: {broadcast_error}")
                    
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        # Remove client from connections when they disconnect
        if websocket in CONNECTIONS:
            CONNECTIONS.remove(websocket)
            print(f"Client disconnected. Remaining clients: {len(CONNECTIONS)}")

async def main():
    async with serve(handle_connection, "localhost", 5000) as server:
        print("Server started on ws://localhost:5000")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())