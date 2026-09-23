from machine import Pin, ADC
import time

adc = ADC(Pin(26))

while True:
    ad_data = adc.read_u16()
    ad_percent = ad_data * 100 / 65535
    ad_volt = ad_data * 3.3 / 65535

    print("percent=", ad_percent, "volt=", ad_volt)

    time.sleep(1)
