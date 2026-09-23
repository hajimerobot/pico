from machine import Pin
import time

led = Pin("LED", Pin.OUT)
# led = Pin(25, Pin.OUT)

for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
