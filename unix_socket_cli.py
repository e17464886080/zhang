# unix_socket_cli.py
# 本地套接字客户端
from socket import *
sock_file = "/home/tarena/ppe/b"
# 创建客户端
client = socket(AF_UNIX, SOCK_STREAM)
client.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
client.connect(sock_file)

while True:
    msg = input("请输入要发送的消息:")
    if not msg:
        continue
    if msg == "q" or msg == "Q":
        break
    else:
        client.send(msg.encode())
client.close()
