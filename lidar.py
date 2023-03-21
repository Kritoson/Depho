import pigpio
import time

RX2 = 23
pigpio.exceptions = False
pi2 = pigpio.pi()
pi2.set_mode(RX2, pigpio.INPUT)
pi2.bb_serial_read_open(RX2, 115200)


def getTFminiData2():
    while True:

        time.sleep(0.1)
        (count, recv) = pi2.bb_serial_read(RX2)

        if count > 8:
            for i in range(0, count - 9):
                if recv[i] == 89 and recv[i + 1] == 89:  # 0x59 is 89
                    checksum = 0
                    for j in range(0, 8):
                        checksum = checksum + recv[i + j]
                    checksum = checksum % 256
                    if checksum == recv[i + 8]:
                        distance = recv[i + 2] + recv[i + 3] * 256
                        strength = recv[i + 4] + recv[i + 5] * 256

                        return distance
            
