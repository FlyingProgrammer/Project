import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8886))  #连接元组

client.send(b' world')

buff = []

while True:
    s = client.recv(1024)
    if s:
        buff.append(s)
    else:
        break
    data = b''.join(buff)
    print(data)


