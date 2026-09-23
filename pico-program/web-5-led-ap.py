import network
import socket
import time
from machine import Pin
import rp2

rp2.country("JP")

led = Pin("LED", Pin.OUT)

ssid = "pico-w-AP"
password = "12345678"

def connect_ap():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == False:
        time.sleep(0.1)

    ip = ap.ifconfig()

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

def webpage():
    html = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
    </head>
    <body>
        <p>LEDを操作します</p>
        <form action="/ledon">
            <input type="submit" value="LED点灯"/>
        </form>
        <p></p>
        <form action="/ledoff">
            <input type="submit" value="LED消灯"/>
        </form>
</body>
</html>
"""
    return html

def serve(connection):
    while True:
        client = connection.accept()[0]

        try:
            request = client.recv(1024).decode()
#            print("------------------------------")
#            print(request)
            request_line = request.split()[1]

            if request_line.startswith("/ledon"):
                led.on()
            elif request_line.startswith("/ledoff"):
                led.off()

            if request_line.startswith("/favicon.ico"):
                client.send("HTTP/1.1 204 No Content\r\n\r\n".encode())
                continue

            html = webpage()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
            client.send(response.encode())
        except:
            pass
        finally:
            client.close()

try:
    ip = connect_ap()
    print("ip address = ", ip)
    connection = open_socket()
    serve(connection)
except:
    led.off()
    try:
        connection.close()
    except:
        pass
