# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7777
server.bind((host, port))
server.listen(1)


conn, addr = server.accept()

page = open('index.html')
content = page.read()
page.close()

response = 'HTTP/1.0 200 OK\n\n' + content
conn.sendall(response.encode())
conn.close()
