import dht
from machine import Pin
import time

dht_sensor = dht.DHT11(Pin(16, Pin.IN, Pin.PULL_UP))

while True:
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    print(f"温度は{temperature}℃、湿度は{humidity}％")

    time.sleep(2)
