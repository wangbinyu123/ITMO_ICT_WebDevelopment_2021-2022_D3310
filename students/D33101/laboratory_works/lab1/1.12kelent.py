import socket

sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sc.connect(("127.0.0.1", 14900))

msg= sc.recv(1024)

print("接收到服务器的欢迎消息:Hello, server")

sc.close()