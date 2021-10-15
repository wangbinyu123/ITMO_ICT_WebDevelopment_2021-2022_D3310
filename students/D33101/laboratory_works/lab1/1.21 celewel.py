import socket
import struct
import math
from math import *

def k(a,h):
    return a*h

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1522))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    data = clientsocket.recv(1024)
    udata = list(data)
    if 1 in udata:
        result = k(udata[1], udata[2])
        a = struct.pack('!f', result)
        clientsocket.send(a)
    else:
        clientsocket.close()