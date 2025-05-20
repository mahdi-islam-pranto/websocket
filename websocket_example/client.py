from websockets.sync.client import connect

def send_hello():
     # WebSocket server URL 
    uri = "ws://localhost:8765"

    # Create a connection to the WebSocket server
    # The 'with' statement ensures the connection is properly closed after use
    with connect(uri) as websocket:
        name = input("What's your name? ")

        # Send the name to the server
        websocket.send(name)
        print(f">>> {name}")

        # Receive the greeting from the server
        greeting = websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    send_hello()