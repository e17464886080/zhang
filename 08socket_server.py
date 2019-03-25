from SocketServer import *



class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    #重写handle方法
    def handle(self):
        #client_address:客户端地址
        print(self.client_address,'链接')
        while True:
            #属性:self.request  客户端套芥子
            data=self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send('服务器收到'.encode())

#创建服务器对象
server=Server(('0.0.0.0',8888))
#启动
server.server_forever()

