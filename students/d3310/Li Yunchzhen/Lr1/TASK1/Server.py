#Server.py
import socket

msg = 'Hello, Client'

sock = socket.socket(socket.AF_INET)
sock.bind(('localhost',9090))
sock.listen(1)
while True:
    connection, addr = sock.accept()
    data = connection.recv(1024)
    print(data.decode())
    connection.send(msg.encode('utf-8'))
    connection.close()
