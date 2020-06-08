#  @Function:  ＴCP传输协议的服务端
#　＠Time:2020/5/20 下午3:42
#  @Author:Flank

#导入socket库
from socket import *

#1. 定义参数
IP='127.0.0.1'
PORT=50000
BUFLEN=512 #一次从socket缓存区最多读入512个字节数据
# 2.实例化一个socket对象,并绑定IP和端口
#AF_INET:表示该Socket网络层使用IP协议
#SOCK_STREAM:表示Socket传输层使用TCP协议
socket=socket(AF_INET,SOCK_STREAM)#TCP/IP
socket.bind((IP,PORT))

# 3.使SOcket处于监听状态,等待客户端的连接请求
socket.listen(5)#5表示对多接受5个客户端
print(f'服务端启动成功,在{PORT}端口等待连接...')

#返回一个新的socket,用来传输数据的
dataSocket,addr=socket.accept()
print('接受一个客户端连接',addr)
while True:
    recved=dataSocket.recv(BUFLEN)
    if not recved: break
    # 读取的字节是bytes类型,需要解码为字符串
    info=recved.decode()
    print("收到对方的消息: ",info )
    dataSocket.send(f'服务端收到了消息:{info}'.encode())
dataSocket.close()
socket.close()






