
import serial

ser = serial.Serial('/dev/ttyS0', 115200) # replace ttyAMA0 with the appropriate serial port
	
while True:
	response = ser.readline().decode('utf-8').rstrip()
	print(response)
	
