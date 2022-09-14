"""
多任务处理:使得计算机可以同时处理多个任务, 进程通过轮替占用CPU的运行来实现。(进程即正在执行中的程序)
高并发: 进程数远大于CUP的核数
高并行: CPU的核数多同时进程数就多

多进程：
    程序：是一个指令的集合
    进程：正在执行的程序

    *进程开始运行时，首先会创建一个主进程
    *在主进程（父进程）下，我们可以创建新的进程（子进程），子进程依赖于主进程，如果主进程结束，程序会退出
    *Python提供了非常好用的多进程包multiprocessing,借助这个包可以轻松完成从单进程到并发执行的转换

"""

from multiprocessing import Process
def run(name):
    print('123{}'.format(name))
def run1():
    print('456')

if __name__=="__main__": #指定主方法函数。在脚本执行时开启main函数，但是在其他文件import调用时不会执行。
    p = Process(target=run, args=("test",))   #taget只要写函数名不要加（）; args是位置参数元组,一个元组时后面要加逗号
    p.start()
    p.join()  #作用是让主进程等待子进程结束
    p1 = Process(target=run1)   #target只要写函数名不要加（）
    p1.start()
    p1.join()  #作用是让主进程等待子进程结束