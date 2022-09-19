"""
TFTP: Trivial File Transfer  Protocol, 简单文件传输协议 （如果要做文件传输/下载的话要用到这个协议）
    1、它是在TCP/IP协议簇中用来在客户端与服务器之间进行简单文件传输的协议
    2、使用这个协议，就可以实现简单文件的下载， tftp端口号为69
    3、这个协议比较简单，它在运行的时候占用的空间较小，比较适合传递小文件
    4、比较适合在局域网中传递
    5、是基于UDP协议来实现的

    实现TFTP下载器
        下载：从服务器上将一个文件复制到本机上
        下载的过程：
            1、在本地创建一个空文件夹（要与下载的文件同名）
            2、向里面写数据（接收到一点就向空文件里写一点）
            3、关闭（接收完所有数据关闭文件）

......更多TFTP相关知识可见同名PPT文档

"""
#假设要从TFTP服务器上下载一个文件名为dog.jpg的照片
from socket import *
import struct
filename = 'dog.jpg'
server_ip = '192.168.0.105'
#构建下载请求
send_data = struct.pack("!H%dsb5sb"%len(filename),1,filename.encode(),0,'octet'.encode(),0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(send_data, (server_ip, 69))
#创建一个与下载文件同名的空文件，“ab"表示的是打开模式，其中a代表用追加模式打卡，b是二进制的形式打开
f = open(filename, 'ab')
#直到接收到的数据长度小于516字节就跳出循环结束程序
while True:
    recv_data = s.recvfrom(1024)  #接收数据
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][0:4])  #获取数据块编号，前两个字节为操作码后两个字节是块编号，跟在后面的才是具体要写入的512字节的数据
    rand_port = recv_data[1][1]  #获取服务器的随机端口
    if int(caozuoma) == 5:
        print('文件不存在...')
        break
    print('操作码: %d, ACK: %d, 服务器随机端口: %d, 数据长度: %d'%(caozuoma, ack_num, rand_port, len(recv_data))) #如果只是要下载这行可省略
    f.write(recv_data[0][4:]) #将数据写入
    if len(recv_data[0]) < 516:
        break
    ack_data = struct.pack("!HH", 4, ack_num) #确认包的操作码是4
    s.sendto(ack_data, (server_ip, rand_port)) #回复ACK确认包
    