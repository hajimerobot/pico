from machine import Pin, PWM
import time

pwm1 = PWM(Pin(14), freq=500)
pwm2 = PWM(Pin(15), freq=500)

pwm1_duty = int(0.4 * 65535)
pwm2_duty = 0

pwm1.duty_u16(pwm1_duty)
pwm2.duty_u16(pwm2_duty)

time.sleep(1)

pwm1.duty_u16(0)
pwm2.duty_u16(0)

time.sleep(1)

pwm1.deinit()
pwm2.deinit()
