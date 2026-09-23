from machine import Pin
import time

led = Pin("LED", Pin.OUT)

try:
    while True:
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
except KeyboardInterrupt:
#    print("kkkkk")
#    pass
    led.off()
