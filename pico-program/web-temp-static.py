import network
import socket
import time
from machine import Pin
import rp2
import dht

rp2.country("JP")

led = Pin("LED", Pin.OUT)
dht_sensor = dht.DHT11(Pin(16, Pin.IN, Pin.PULL_UP))

# あなたのネットワーク環境
ssid = ""
password = ""

IP_ADDRESS = ""
SUBNET_MASK = ""
GATEWAY = ""
DNS = ""

def connect_static():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.ifconfig((IP_ADDRESS, SUBNET_MASK, GATEWAY, DNS))
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print("Waiting for connection...")
        time.sleep(1)

    ip = wlan.ifconfig()

#    print("ip address = ", ip[0])
#    print("netmask = ", ip[1])
#    print("gateway = ", ip[2])
#    print("dns = ", ip[3])

    return ip[0]

def open_socket():
    address = socket.getaddrinfo("0.0.0.0", 80)[0][-1]

    connection = socket.socket()
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    connection.bind(address)
    connection.listen(1)

#    print(connection)

    return connection

def webpage(temperature, humidity):
    html = f"""<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <meta http-equiv="refresh" content="5">
    </head>
    <body>
        <p style="font-size: 2em;">温度は{temperature}℃、湿度は{humidity}％</p>
    </body>
</html>
"""
    return html

def serve(connection):
    temperature = 0
    humidity = 0

    while True:
        client = connection.accept()[0]

        try:
            request = client.recv(1024).decode()
#            print("------------------------------")
#            print(request)
            request_line = request.split()[1]

            if request_line.startswith("/favicon.ico"):
                client.send("HTTP/1.1 204 No Content\r\n\r\n".encode())
                continue

            led.toggle()

            dht_sensor.measure()
            temperature = dht_sensor.temperature()
            humidity = dht_sensor.humidity()

            html = webpage(temperature, humidity)
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
            client.send(response.encode())
        except:
            pass
        finally:
            client.close()

try:
    ip = connect_static()
    print("ip address = ", ip)
    connection = open_socket()
    serve(connection)
except:
    led.off()
    try:
        connection.close()
    except:
        pass
