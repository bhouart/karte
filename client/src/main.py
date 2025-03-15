import asyncio
import websockets
from dotenv import load_dotenv
import os


async def read_input(prompt="Enter message: "):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, prompt)

async def send_message(websocket):
    while True:
        message = await read_input()
        await websocket.send(message)

async def receive_message(websocket):
    while True:
        response = await websocket.recv()
        print(f"Received: {response}")

async def chat(ip, port):
    async with websockets.connect(f'ws://{ip}:{port}') as websocket:
        # Run sending and receiving concurrently
        await asyncio.gather(send_message(websocket), receive_message(websocket))

if __name__ == "__main__":
    load_dotenv()
    ip = os.getenv("IP")
    port = os.getenv("PORT")
    asyncio.run(chat(ip, port))