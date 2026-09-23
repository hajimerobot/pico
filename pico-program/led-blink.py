from machine import Pin
import time

# led = Pin("LED", Pin.OUT)
led = Pin(15, Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
