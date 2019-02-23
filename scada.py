import asyncio
from pyee import EventEmitter

import canreader
import dbwriter

ee = EventEmitter()

ee.on('data_new')(dbwriter.write_data)

if __name__ == "__main__":
    asyncio.run(canreader.start(ee, 125000))
