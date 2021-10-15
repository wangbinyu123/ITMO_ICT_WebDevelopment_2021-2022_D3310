#Server.py
import socket

sock = socket.socket(socket.AF_INET)
sock.bind(('localhost',9090))
sock.listen(1)
while True:
    connection, addr = sock.accept()
    pack = connection.recv(1024)
    pack = pack.decode()
    pack = pack.split()
    data = pack[1:]
    data = list(map(float, data))
    print(data)
    if pack[0] == "a":
        msg = data[0]**2 + data[1]**2
    elif pack[0] == "b":
        func = (-data[1]+(data[1]**2 - 4*data[0]*data[2])**0.5)/data[0]*2
        msg = [func, -func]
    elif pack[0] == "c":
        msg = ((data[0] + data[1])*data[2])/2
    elif pack[0] == "d":
        msg = data[0] * data[1]

    msg = str(msg)
    connection.send(msg.encode('utf-8'))
connection.close()
