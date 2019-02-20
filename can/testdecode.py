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
PDO1 = can.Message(arbitration_id=0x181, data=[0xFEDCBA9876543210])

class MotorController(can.Listener):
	"""
	Listens for sync messages. Responds with PDOs.
	
	"""
	#TODO add full motorcontroller response to CANbus messages
	# add ability to reconfigure motorcontroller simulator
	# def __init__(self):
	# 	return

	def on_message_received(self, msg):
		if msg.arbitration_id == 0x80 and msg.data == 0x00:
			#TODO add more PDOs
			#TODO add feature to count syncs before sending PDO
			self.send(PDO1)
		# Add more CANopen responses here

mc = MotorController()			

sync = can.Message(arbitration_id=0x80, data[0x00])
sync_bus.send_periodic(sync, 0.1)

for msg in scada_bus:
	print(msg.string)

