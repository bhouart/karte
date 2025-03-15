import asyncio
from websockets.asyncio.server import serve
from dotenv import load_dotenv
import os

# A set to store all connected clients
connected_clients = set()

async def broadcast(websocket, message):
    # Broadcast the message to every connected client
    for client in connected_clients:
        # Optionally, you can skip sending to the sender if desired
        await client.send(message)

async def echo(websocket):
    # Add new client connection to the set
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # For example, if you want a special response for "wesh"
            if message == "wesh":
                response = "pêlo"
            else:
                response = message
            # Broadcast the response to all connected clients
            await broadcast(websocket, response)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Remove the client connection when it disconnects
        connected_clients.remove(websocket)

async def main():
    load_dotenv()
    port = os.getenv("PORT")
    
    async with serve(echo, "0.0.0.0", port):
        # Keep the server running indefinitely
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())