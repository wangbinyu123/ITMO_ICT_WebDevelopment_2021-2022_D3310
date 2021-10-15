import socket
import time
import random
server = socket.socket()
host = '127.0.0.1'
port = 1234
server.bind((host, port))
print("starting server on", host, port)
print("the web server URL for the would be http://%s:%d" % (host, port))
server.listen(5)
print("entering infinite loop: hit CTRL-C to exit")
while True:
    client, (client_host, client_port) = server.accept() # 获得服务器ip和端口
    print("got connection from", client_host, client_port)
    client.recv(1024)
    response_type = 'HTTP/1.0 200 ok\n'
    headers = 'content-type: text/html\n\n'
    body = """
    <html>
    <body>
    <h1>Hello World</h1>!
    </body>
    </html>
    """
    response = response_type + headers + body
    client.send(response.encode('utf-8'))
    client.close()