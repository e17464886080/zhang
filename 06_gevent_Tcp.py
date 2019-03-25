import gevent 

from gevent import monkey
#修改脚本，修改阻塞行为
monkey.patch_socket()
from socket import  *

def server():
    server=socket()
    ADDRESS=('0.0.0.0',8888)

    server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    server.bind(ADDRESS)
    server.listen(10)
    print('wiatt.........')
    while True:
        client,addr=server.accept()
        print(addr,'lianjie')
        #处理客户端请求的函数
        handler(client)
        # gevent.spawn(handler,client)
        print(1)

def handler(client):
    while True:
        data=client.recv(1024)
        print(data.decode())
        if not data:
            break
        client.send('server shoudao'.encode())
    client.close()

if __name__ == '__main__':
    server()
