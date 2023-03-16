import serial
ser = serial.Serial('/dev/ttymxc0', 115200) # replace ttyS1 with the appropriate serial port
while True:

  ser.write(b'Hello Raspberry Pi!\n')
  response = ser.readline()
  
