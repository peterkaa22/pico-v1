import serial

picoA = serial.Serial('/dev/ttyAMA0', 115200)
picoB = serial.Serial('/dev/ttyAMA1', 115200)

picoA.write(b'1')  # LED ON
picoA.write(b'0')  # LED OFF

if picoB.in_waiting:
    print(picoB.readline())