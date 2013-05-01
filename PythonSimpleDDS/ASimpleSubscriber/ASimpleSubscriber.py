import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5555
MESSAGE = "subscribe, hello"
a = bytes(MESSAGE, 'UTF-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:

    sock.sendto(a, (UDP_IP, UDP_PORT))
    time.sleep(1)
     