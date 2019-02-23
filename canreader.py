import can
from pyee import EventEmitter

async def start(event_emitter, bitrate=125000):
    print("canreader started")
    ee = event_emitter
    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=bitrate)
    print("canbus opened")
    for msg in bus:
        print(msg)
        # decode message
        # return list of new data
        # for each new data create new data event
        ee.emit('data_new', 'mysensor', '10', '5.02')
