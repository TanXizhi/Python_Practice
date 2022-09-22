"""
编写一个简单的TCP服务器

"""

from socket import *
#创建一个socket对象tcpSock, 可以通过tcpSock进行网络的数据收发
#第一个参数是AF_INET代表的是IPV4协议；第二个参数是SOCK_STREAM或者SOCK_DGRAM分别代表UDP和TCP两种协议
tcpSock = socket(AF_INET, SOCK_STREAM)
#绑定一个端口，第一个参数元组里的第一个元素为“”时默认为本机IP，第二个元素为要绑定的端口号，在这里假设绑定到7788端口（与广播TFTP的69端口类似只用于接收请求）
tcpSock.bind(('', 7788))
#用listen()方法设置最大连接数，即最多能排队的人数，这里设为5
tcpSock.listen(5)
#用accept()方法等待客户端连接，一旦有客户端连接它，它就会返回两个值
#一个是新的socket对象(数据收发不用7788端口而是会新生成一个端口，只要有客户端来连接都会新生成一个端口，这样就可以把接收请求的socket空出来），另一个是客户端地址
newSock, clientAddr = tcpSock.accept()
#接收数据，在udp里接收数据是recvfrom，在tcp里接收数据是recv
data = newSock.recv(1024)
print(data)
#发送数据，在udp里发送数据是sendto，在tcp里发送数据是send
#在udp里发送数据有两个参数，第一个为要发送的内容，第二个为接收方的ip地址和端口号。
#但是用tcp协议发送数据时不再需要第二个参数，是因为在最初进行三次握手的时候已经建立了稳定的连接
newSock.send(b'thanks')
#在数据收发结束之后就可以关闭socket对象了，先关闭的是新创建的socket对象，一旦新创建的这个套接字对象被关闭后就意味着不再为这个客户端服务了
newSock.close()
#当想要结束的时候还要把作为监听的套接字关闭掉，只要这个负责监听的套接字对象关闭就意味着整个程序都不能再接收新的客户端连接了
tcpSock.close()



