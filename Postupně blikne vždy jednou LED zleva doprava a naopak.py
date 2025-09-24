from machine import Pin
import time


led_pins = [2, 3, 4, 5, 6, 7, 8, 9]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]


button = Pin(10, Pin.IN, Pin.PULL_UP)


direction = 1
index = 0

def clear_leds():
    for led in leds:
        led.value(0)

while True:
    
    if button.value() == 0:
        time.sleep(0.2)  
        direction *= -1  

    
    clear_leds()
    leds[index].value(1)
    time.sleep(0.2)

    
    clear_leds()
    time.sleep(0.2)

    
    index += direction

    
    if index >= len(leds) - 1:
        direction = -1
    elif index <= 0:
        direction = 1
