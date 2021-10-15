import socket
import struct

a = int(input("введите сторону a:"))
h = int(input("введите сторону h:"))

lst = [1, a, h]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1522))
s.send(bytearray(lst))
data = s.recv(1024)
updata = struct.unpack('!f', data)
print(updata)
s.close()