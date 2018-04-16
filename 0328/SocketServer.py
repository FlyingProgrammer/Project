import socket
import threading
def ProcesingRequest(sock,addr):
    print('客户端:' , addr[0] , '.' , addr[1])
    sock.send(b'Welcome!')
    buff=[]
    while True:
        s=sock.recv(1024)
        if s:
            buff.append(s.decode('utf-8'))
        else:
            break
        print('hello %s!' % buff)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8886))   # 绑定元组
server.listen(5)
print('正在监听...')
while True:
    sock,addr=server.accept()
    t=threading.Thread(target=ProcesingRequest,args=(sock,addr))
    t.start()

server.close()



