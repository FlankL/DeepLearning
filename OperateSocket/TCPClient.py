#  @Function:  ＴCP传输协议的客户端
#　＠Time:2020/5/20 下午4:20
#  @Author:Flank
from socket import *

IP='127.0.0.1'
PORT=50000
BUFLEN=1024
#1.实例化一个socket对象,指明协议
dataSocket=socket(AF_INET,SOCK_STREAM)
#2.连接服务端socket
dataSocket.connect((IP,PORT))
i=0
while i<10:
    #发送消息,编码为bytes
    dataSocket.send('hello,server'.encode())
    #等待接受服务端的消息
    recved=dataSocket.recv(BUFLEN)
    if not recved: break
    print(recved.decode())
    i=i+1
dataSocket.close()


