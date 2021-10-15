#Client.py
import socket

sock = socket.socket(socket.AF_INET)
sock.connect(('localhost',9090))

sock.sendall(bytes(f'.', 'utf-8'))
data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()
