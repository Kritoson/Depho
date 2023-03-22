import serial
import time
import struct


ser = serial.Serial('/dev/ttyS0', 115200, timeout=None) # replace ttyAMA0 with the appropriate serial port


while True:
	#ser.flush()
	response = ser.read(8)
	#data_left = ser.inWaiting()  # Get the number of characters ready to be read
	#response += ser.read(data_left)
	#print(response)
	#time.sleep(1)
	data = struct.unpack('ii', response)
	print("aaa")
	print(data)
	
	
