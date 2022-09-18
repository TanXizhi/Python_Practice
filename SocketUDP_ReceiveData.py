"""
如何用socket-UDP协议接收数据
这里我借助了一个socket调试工具Packet Sender, 也可以借助其他的工具
网络通信的步骤如下：
    发送数据
    1、先倒入一个包---from socket import *
    2、创建一个socket对象--- s = socket(AF_INET, SOCK_DGRAM)
    3、准备接收方的地址--- addr = ("192.168.0.104",61330)
    4、以及要发送的内容--- data = input("请输入需要发送的内容：")
    5、然后通过sendto发送给对方，同时要使用encode将数据转成字节流--- s.sendto(data.encode(), addr)
    如果要接受数据的话
    6、使用recvfrom接收数据，recvfrom是同属于s这个套接字对象里的方法，然后保存在一个对象里--- redata = s.recvfrom(2048)
    7、然后打印获得对方发送的数据--- print(redata[0].decode())
    8、关闭对象，接收数据收发--- s.close()
上面这种情况是先给对方发送数据接着做接收，所以接收方可以知道发送方的IP地址和端口号

如果自己写的程序只做接收的话，发送方是不知道IP地址和端口号的，那么就需要绑定一个IP地址和端口号

总结：
作为数据发送方的时候，并不一定要绑定端口，但是一旦作为接收方的话就要绑定端口
从客户端和服务器的角度看，客户端多数情况下是主动跟服务器建立连接的（或者说是第一条数据的发送方）所以一般是不会绑定端口的，
而服务器一般是等着别人来与它建立连接所以作为数据接收方多数情况下是需要绑定端口的

"""

"""
from socket import *
#创建一个socket对象s, 可以通过s进行网络的数据收发
#第一个参数是AF_INET代表的是IPV4协议；第二个参数是SOCK_STREAM或者SOCK_DGRAM分别代表UDP和TCP两种协议
s = socket(AF_INET, SOCK_DGRAM)
#第一个参数为要发送的数据（需要将字符串转换成Ascii字节流）, 第二个参数是一个元组，其中第一个为IP地址，第二个为接收方分配的端口号
#如果接收方接收的数据是乱码则是字符集的问题，需要在encode()里注明接收方用的字符集类型
#s.sendto("Don't Panic".encode(), ("192.168.0.104",61330))

#数据发送还可以写成如下形式
addr = ("192.168.0.104",61330)
data = input("请输入需要发送的内容：")
s.sendto(data.encode(), addr)


#数据接收：程序到这时会阻塞，也就是说会卡在这一行等着接收别人给它发送的数据
#第一个参数为本次能接收的最大字节数
redata = s.recvfrom(2048)
#如果直接print(redata)发现结果是一个元组，元组里的第一个元素是接收到的字节流数据，第二个元素是一个元组，包含发送方的IP地址和端口号
#如果只想获得对方发送的数据时应该如下打印，用decode()将字节流转换成字符串。如果接收到的数据是乱码则是字符集的问题，需要在decode()里注明接收方用的字符集类型，
print(redata[0].decode())
s.close()
"""



#如果只做接收，那就一定要绑定端口
from socket import *

s = socket(AF_INET, SOCK_DGRAM)
#绑定IP和端口，包含一个参数，参数为元组，元组的第一个元素为IP地址（如果为本机IP则不写),第二个元素为端口号
s.bind(('',55539))
s.sendto("Hello, I'm Xizhi".encode(), ("192.168.0.104", 56565))
redata = s.recvfrom(2048)
print(redata[0].decode())



