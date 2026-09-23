from machine import Pin
import time

led = Pin(15, Pin.OUT)

button = Pin(14, Pin.IN, Pin.PULL_UP)
# button = Pin(14, Pin.IN)

while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()

    time.sleep(0.01)
