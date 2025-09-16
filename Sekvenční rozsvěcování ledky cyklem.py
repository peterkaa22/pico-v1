from machine import Pin
from time import sleep


led_pins = [2, 3, 4, 5]
leds = [Pin(p, Pin.OUT) for p in led_pins]


delay = 0.5

while True:
    for led in leds:
        led.value(1)
        sleep(delay)
        led.value(0)
