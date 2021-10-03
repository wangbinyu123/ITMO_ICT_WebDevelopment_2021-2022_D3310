# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 7777))
result = conn.recv(10240)
print(result.decode())
conn.close()