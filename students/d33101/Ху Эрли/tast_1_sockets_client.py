# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 5555))
conn.send(b"Hello, server! \n")
data = conn.recv(1024)
udata = data.decode('utf-8')
print(udata)
conn.close()