#!/usr/bin/env python

import asyncio
import websockets

async def echo(websockets):
    async for message in websockets:
        await websockets.send(message)

async def main():
    async with websockets.serve(echo,"localhost",8765):
        await asyncio.Future()

asyncio.run(main())