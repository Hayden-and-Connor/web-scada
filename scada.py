import asyncio
from pyee import EventEmitter

import canreader
import dbwriter

ee = EventEmitter()

dbwriter.setup("mydatabase.db", ee)

if __name__ == "__main__":
    asyncio.run(canreader.start(ee, 125000))
