#Client.py
import socket

sock = socket.socket(socket.AF_INET)
sock.connect(('localhost',9090))
msg = input()

sock.send(msg.encode('utf-8'))
data = sock.recv(1024)
print(data.decode())

sock.close()
