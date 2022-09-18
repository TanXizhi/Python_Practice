"""
Echo服务器：非常有用的用于调试和检测的服务器，协议的作用是对方给我发送了什么我原样发回

"""
from socket import *
#创建一个socket对象
udpSock = socket(AF_INET, SOCK_DGRAM)
#绑定一个端口，不使用随机分配的端口
udpSock.bind(('',56565))
#以下是用Echo模拟一个半双工聊天室，半双工聊天室即在发送数据的时候不能接收，在接收的时候不能发送；
#全双工聊天室是在数据接收的时候同时可以发送，可以通过多线程实现
while True:
    reData = udpSock.recvfrom(1024)
    print(reData[0].decode())
    data = input('请输入：')
    udpSock.sendto(data.encode(),reData[1])

udpSock.close()
