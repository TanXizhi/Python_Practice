"""
如何用socket-UDP协议发送数据
这里我借助了一个socket调试工具Packet Sender, 也可以借助其他的工具
"""
from socket import *
#创建一个socket对象s, 可以通过s进行网络的数据收发
#第一个参数是AF_INET代表的是IPV4协议；第二个参数是SOCK_STREAM或者SOCK_DGRAM分别代表UDP和TCP两种协议
s = socket(AF_INET, SOCK_DGRAM)
#第一个参数为要发送的数据（需要转换为Ascii格式）, 第二个参数是一个元组，其中第一个为IP地址，第二个为接收方分配的端口号
#如果接收到的数据是乱码则是字符集的问题，需要在encode()里注明接收方用的字符集类型
#s.sendto("Don't Panic".encode(), ("192.168.0.104",61330))

#还可以写成如下形式
addr = ("192.168.0.104",61330)
data = input("请输入需要发送的内容：")
s.sendto(data.encode(), addr)

