from machine import Pin, PWM
import time

led = PWM(Pin(15), freq=10)

led.duty_u16(32768)  # 50%
# led.duty_u16(6554)  # 10%
#led.duty_u16(58982)  # 90%
time.sleep(3)

led.duty_u16(0)  # 0%
time.sleep(1)

led.deinit()
