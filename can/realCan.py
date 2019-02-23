import can

bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=125000)

for msg in bus:
    print(msg)
