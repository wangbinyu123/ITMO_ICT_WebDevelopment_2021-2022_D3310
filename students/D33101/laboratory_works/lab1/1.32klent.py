import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 1234))
headers = [
    'get / HTTP/1.1',
    'host: 127.0.0.1',
    'connection: keep-alive',
    'accept: text/html',
    '\n'
]
content = '\n'.join(headers)
print(content)
c.send(content.encode())
result = c.recv(1024)
print(result.decode())