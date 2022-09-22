"""
编写一个简单的TCP客户端

"""

from socket import *
from xmlrpc import client
#创建一个socket对象clientSock, 可以通过clientSock进行网络的数据收发
#第一个参数是AF_INET代表的是IPV4协议；第二个参数是SOCK_STREAM或者SOCK_DGRAM分别代表UDP和TCP两种协议
clientSock = socket(AF_INET, SOCK_STREAM)
#客户端可以不用绑定一个固定端口号，因为客户端一般为主动建立连接的那一方，服务器在accept()之后会获取客户端的地址
#通过客户端与服务器进行连接,括号里的参数为服务器的IP地址和端口号组成的一个元组，三次握手的过程就是在这个时候进行的
clientSock.connect(('192.168.2.101', 7788))
#发送数据
clientSock.send(b'Hello')
#接收数据
data = clientSock.recv(1024)
print(data)
clientSock.close()



