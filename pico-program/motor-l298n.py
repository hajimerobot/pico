from machine import Pin, PWM
import time

pwm = PWM(Pin(13), freq=500)
in1 = Pin(14, Pin.OUT)
in2 = Pin(15, Pin.OUT)

pwm_duty = int(0.2 * 65535)

pwm.duty_u16(pwm_duty)
in1.on()
in2.off()

time.sleep(1)

pwm.duty_u16(0)
in1.off()
in2.off()

time.sleep(1)

pwm.deinit()
