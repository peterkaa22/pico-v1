from machine import Pin
import time
import random


led_pins = [2, 3, 4, 5, 6, 7, 8, 9]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]


button = Pin(10, Pin.IN, Pin.PULL_UP)

mode = 0  

def clear_leds():
    for led in leds:
        led.value(0)

while True:
   
    if button.value() == 0:
        time.sleep(0.2)  
        mode += 1
        if mode > 2:
            mode = 0

    clear_leds()

    
    if mode == 0:
        index = random.randint(0, len(leds)-1)
        leds[index].value(1)
        time.sleep(0.5)

    
    elif mode == 1:
        
        pocet = random.randint(1, len(leds))
        vybrane = random.sample(leds, pocet)  
        for led in vybrane:
            led.value(1)
        time.sleep(0.7)

    
    elif mode == 2:
        index = random.randint(0, len(leds)-1)
        leds[index].value(1)
        time.sleep(0.2)
