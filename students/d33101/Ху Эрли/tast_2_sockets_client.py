# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 6666))
a = input("Введите длину первого катета: ")
b = input("Введите длину второго катета: ")
conn.send(a.encode())
conn.send(b.encode())
c_bin = conn.recv(1024)
c = c_bin.decode('utf-8')
print('Гипотенуза треугольника равна: ', c)
conn.close()