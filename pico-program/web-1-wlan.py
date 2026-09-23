import network
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

ip = connect()
print("ip address = ", ip)
