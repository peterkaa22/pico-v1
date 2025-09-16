from machine import Pin
from time import sleep

# Nastavení pinů jako výstupy
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)
led5 = Pin(5, Pin.OUT)

# Interval (ms)
delay = 0.5   # půl sekundy

while True:
    led2.value(1); sleep(delay); led2.value(0)
    led3.value(1); sleep(delay); led3.value(0)
    led4.value(1); sleep(delay); led4.value(0)
    led5.value(1); sleep(delay); led5.value(0)
