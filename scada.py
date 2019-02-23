import asyncio
from pyee import EventEmitter

import canreader

ee = EventEmitter()

if __name__ == "__main__":
    asyncio.run(canreader.start(ee, 125000))