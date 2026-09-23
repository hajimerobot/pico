import network
import socket
import time
import rp2

rp2.country("JP")

# あなたのネットワーク環境
ssid = ""
password = ""

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
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

    print(connection)

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
            print("------------------------------")
            print(request)

            html = webpage()
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
            client.send(response.encode())
        except:
            pass
        finally:
            client.close()

try:
    ip = connect()
    print("ip address = ", ip)
    connection = open_socket()
    serve(connection)
except:
    try:
        connection.close()
    except:
        pass
