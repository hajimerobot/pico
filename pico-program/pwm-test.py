from machine import Pin, PWM

pwm = PWM(Pin(13), freq=500)

pwm_duty = int(0.5 * 65535)
pwm.duty_u16(pwm_duty)

# pwm.duty_u16(0)
# pwm.deinit()
