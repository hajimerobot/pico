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

try:
    ip = connect()
    print("ip address = ", ip)
    connection = open_socket()
except:
    try:
        connection.close()
    except:
        pass
