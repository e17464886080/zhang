from socket import socket

address=('127.0.0.1',8888)
client=socket()
client.connect(address)
client.send('uo aer ic'.encode())
while True:
    data=client.recv(1024).decode()
    if not data:
        print('bira')
        break
    print(data)