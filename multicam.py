import serial

ser = serial.Serial('/dev/ttymxc0', 115200) # replace ttyS1 with the appropriate serial port
message = ''


def send_data(cor):
    package = b''

    for i in cor:
        package += struct.pack('!i', i)
        print(package)

    # Sent string value,but if tests shows us it is wrong turn it on btye
    ser.write(package.encode('utf-8'))

    # Do nothing for 500 milliseconds (0.5 seconds)
    time.sleep(0.5)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
