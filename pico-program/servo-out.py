from machine import Pin, PWM
import time

pwm = PWM(Pin(15), freq=50)

angle_0 = int(1.45e6)
angle_p90 = int(2.4e6)
angle_m90 = int(0.5e6)

pwm.duty_ns(angle_0)
time.sleep(3)

pwm.duty_ns(angle_p90)
time.sleep(3)

pwm.duty_ns(angle_m90)
time.sleep(3)

pwm.duty_ns(angle_0)
time.sleep(3)

pwm.duty_ns(0)
time.sleep(1)

pwm.deinit()
