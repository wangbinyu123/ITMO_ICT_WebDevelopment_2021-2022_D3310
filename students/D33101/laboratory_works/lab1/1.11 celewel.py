import socket
# 创建服务端套接字
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定服务端IP地址和端口
sc.bind(("127.0.0.1", 14900))
# 开始监听
sc.listen(10)
# 等待连接
print("服务端程序启动完成，等待连接中...")
conn, addr = sc.accept()
print("客户端%s连接成功" % str(addr))
print("Hello, client")
# 向客户端发送消息

conn.sendall("Hello, client".encode("utf-8"))
# 关闭和这个客户端的套接字
conn.close()