# unix_socket_svr.py
# 本地套接字示例
from socket import *
import os
# 套接字文件
sock_file = "/home/tarena/ppe/a"
if os.path.exists(sock_file):
    os.remove(sock_file)#删除套接字文件
# 创建套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
sockfd.bind(sock_file)#绑定地址
sockfd.listen(3)
while True:
    client, addr = sockfd.accept()
    while True:
        data = client.recv(1024)
        print(data.decode())
sockfd.close()
