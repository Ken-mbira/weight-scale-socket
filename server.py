#!/usr/bin/env python

import asyncio
import websockets

async def echo(websocket):
    print("I have been initiated")
    async for message in websocket:
        print(f"I have been called and the message that i got is {message}")
        await websocket.send(message)

async def main():
    async with websockets.serve(echo,"localhost",8765):
        await asyncio.Future()

asyncio.run(main())