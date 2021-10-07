#Server.py
import socket

sock = socket.socket(socket.AF_INET)
sock.bind(('localhost',9090))
sock.listen(1)
while True:
    connection, addr = sock.accept()
    pack = connection.recv(1024)
    connection.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n"
     + open("index.html", "rb").read())
    connection.close()

