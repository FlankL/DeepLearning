#  @Function:  UDP通信协议的Client端
#　＠Time:2020/5/21 上午11:22
#  @Author:Flank

import  socket

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in ['Tom', 'Jary', 'Mary']:
    # 发送数据:
    s.sendto(data.encode(), ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()