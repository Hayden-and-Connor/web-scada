import can

scada_bus = can.interface.Bus('test', bustype='virtual')
mc_bus = 	can.interface.Bus('test', bustype='virtual')
sync_bus = 	can.interface.Bus('test', bustype='virtual')

# # set up SCADA CAN listener
# class ScadaCAN(can.Listener):

# 	def on_message_received(self, msg):
# 		if msg.arbitration_id == 0x181:
# 			# decode PDO1

# 			# save to db




# make Listener subclass that looks for sync signal and responds with PDO1
PDO1 = can.Message(arbitration_id=0x181, data=[0xFE, 0xDC, 0xBA, 0x98, 0x76, 0x54, 0x32, 0x10])

class MotorController(can.Listener):
	"""
	Listens for sync messages. Responds with PDOs.
	
	"""
	#TODO add full motorcontroller response to CANbus messages
	# add ability to reconfigure motorcontroller simulator
	def __init__(self, bus):
		self.bus = bus

	def on_message_received(self, msg):
		if msg.arbitration_id == 0x80 and msg.data == 0x00:
			#TODO add more PDOs
			#TODO add feature to count syncs before sending PDO
			self.bus.send(PDO1)
		# Add more CANopen responses here

mc = MotorController()
notifier = can.Notifier(mc_bus, [mc])		

sync = can.Message(arbitration_id=0x80, data=0x00)
sync_bus.send_periodic(sync, 1)

for msg in scada_bus:
	print(msg)

