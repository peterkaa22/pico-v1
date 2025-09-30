from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():  # tlačítko stisknuté (GND, tedy LOW)
        uart.write(b'1')  # pošli znak '1'
        print("Tlačítko zmáčknuto, odesílám '1'")
        time.sleep(0.3)  # debounce + pauza, aby se neposílalo pořád
    time.sleep(0.05)
