from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        uart.write(b'1')
        print("Tlačítko zmáčknuto, posílám '1'")
        time.sleep(0.5)  # debounce
    time.sleep(0.05)
