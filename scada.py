import asyncio
from pyee import EventEmitter

import canreader
import dbwriter

ee = EventEmitter()

dbwriter.setup("mydb.db", ee, 'data_new')

if __name__ == "__main__":
    asyncio.run(canreader.start(ee, 125000))
