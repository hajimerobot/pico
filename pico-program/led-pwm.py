from machine import Pin, PWM

led = PWM(Pin(15), freq=100)

led.duty_u16(32768)  # 50%
# led.duty_u16(6554)  # 10%
# led.duty_u16(58982)  # 90%
