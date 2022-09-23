"""
编写一个多进程TCP服务器,即并发服务器

"""
from socket import *
from multiprocessing import *
from time import sleep
# 处理客户端的请求并为其服务
def dealWithClinet(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('recv{0}: {1}'.format(str(destAddr), recvData))
        else:
            print('{}客户端已经关闭'.format(str(destAddr)))
            break
    newSocket.close()

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    #默认情况下套接字对象不允许被重复使用端口，为了能接收多个连接请求，需要重新修改socket对象的设置，以下为固定写法
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    #加了一个try-finally异常机制是为了保证不管在创建进程过程中有没有出问题，最终作为监听的套接字对象都能正常关闭
    #不加try-finally也能正常运行，加了更保险
    try:
        #循环接收客户端连接请求
        while True:
            print('------主进程...等待新客户端的到来------')
            newSocket, destAddr = serSocket.accept()
            print('------主进程...接下来创建一个新的进程负责数据处理------')
            client = Process(target=dealWithClinet, args=(newSocket, destAddr))
            client.start()
            #子进程start之后主进程会继续往下走，同时因为已经向子进程中copy了一份了，并且父进程中这个套接字也没有用处了，所以关闭(关闭这个对子进程无影响)
            newSocket.close()
    finally:
        #当为所有的客户端服务完之后再进行关闭，表示不再接受新的客户端的连接
        serSocket.close()

if __name__ == '__main__':
    main()



        

