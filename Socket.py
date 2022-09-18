"""
1、网络基础

2、Socket编程（套接字）
    Socket:通过网络完成进程间通信的方式，它是应用层和传输层之间的桥梁
    Socket本质是编程接口（API): Socket是对TCP/IP协议的封装
    Socket之间的连接过程可以分为三个步骤：服务器监听，客户端请求，连接确认
    
    SOCK_STREAM是有保障的(即能保证数据正确传送到对方)面向连接的SOCKET，多用于资料(如文件)传送。
    SOCK_DGRAM是无保障的面向消息的socket, 主要用于在网络上发广播信息。
    SOCK_STREAM是基于TCP的，数据传输比较有保障，但是速度会慢一些（当保密性要求高速度要求较低时使用）
    SOCK_DGRAM是基于UDP的，通信速度快一些但有可能丢数据，容易被黑客攻击，专门用于局域网（当速度要求较高安全性要求并不高时使用）
    基于广播SOCK_STREAM是数据流,一般是tcp/ip协议的编程,SOCK_DGRAM是数据报,是udp协议网络编程
            
    socket-udp
    UDP: User Data Protocol, 用户数据报协议
        发送数据的时候并没有在服务器和客户之间建立连接所以并不能保证对方一定能收得到，并且没有超时重发等机制所以UDP的传输速度很快
        一般用于多点通信或者实时的数据业务，比如语音广播、视频、QQ聊天等这类情况，有时做简单文件传送的时候也会用到UDP
        UDP的过程可以理解为生活中的寄信,也就是说只要知道对方的地址（即对方的IP和端口号）就可以给对方发数据，但是对方能不能收到发送方是没法确定的
    
    socket-tcp
    TCP: Transmission Control Protocol, 传输控制协议
        它是一个基于连接的的协议，也就是说在收发数据之前，TCP必须要先和对方建立一个可靠的连接，
        一个TCP连接要经过三次对话才能建立。简单描述一下对话的过：
            有一台主机A和一台主机B，主机A先发送一个数据连接请求的数据包给主机B，主机B再向主机A发送一个同意的连接，
            主机A在收到这个数据包之后还要向主机B发送一个数据包来确认主机B的要求。只有当三次对话完成后才能正式地进行数据收发。
        TCP的过程可以理解为打电话，在跟对方正式开始聊天之前要有一个寒暄的过程，比方说问候你好啊、确认对方身份、告知对方我的身份。在几次寒暄后才正式进行数据收发。

    UDP和TCP的区别
        1、TCP是基于连接（要先建立完整的连接后才进行数据收发），UDP是无连接（不需要预先建立连接）
        2、在对系统资源的要求上，TCP所占用的系统资源较多，相对的UDP会少一些，UDP程序的结构也会相对简单些
        3、模式上，TCP是流模式，UDP数据报模式
        4、TCP在传输过程中可以保证数据的正确性，UDP则可能会丢包
        5、TCP在传输的时候可以保证数据传输的顺序（即可以保证对方先收到哪条后收到哪条），而UDP则无法保证

    协议的选择：
        在进行安全性要求较高的操作时选择TCP，比如转账等，安全性比速度更重要。
        在进行重要性并不是很高但是需要实时快速地收到数据时选择UDP
        在实际开发过程中，TCP虽然比UDP慢，但是慢的不明显，建立连接的时间也是极短的几乎可以忽略不计；UDP虽然可能会丢包但是丢包的概率也不大
    
    在通信过程中创建socket的时候必须指明是用的TCP还是UDP协议，因为发送方用的是什么协议接收方也必须用这种协议接收，
    也就是说发送方如果用UDP发送数据对方就一定要用UDP协议来接收，如果接收方用的是TCP协议则接收不到数据

3、并发网络服务器

问题：
    1、如何在网络中唯一地标识一台计算机？或者说在进行数据收发时怎么才能确定数据的接收方和发送方究竟是谁？
        通过IP地址实现标识，IP地址可以理解为在网络中用来标记一台计算机的一串数字
        
    2、在同一台计算机上运行多个程序如果做到共用网络而不发生冲突？
    3、不同的计算机在通信的时候怎么才能相互理解

"""

import socket
#创建一个socket对象s, 可以通过s进行网络的数据收发
#第一个参数是AF_INET代表的是IPV4协议；第二个参数是SOCK_STREAM或者SOCK_DGRAM分别代表UDP和TCP两种协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
