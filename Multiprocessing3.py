"""
多进程
    1、调用是无序的
    2、当创建了多个进程的时候，它们会在CPU里频繁地做切换，谁先进入到CPU里执行是不确定的，它是由系统调度机制来决定的
    3、另外，当有多个进程时，子进程1执行多久切换到子进程2也是不确定的，进程之间切换是由操作系统决定的。
    4、在多个进程之间，它们的数据是不共享的，它们有各自独立的内存空间，子进程创建的时候会导入父进程里的所有东西，
       父进程、各子进程相互独立互不影响。

"""

from multiprocessing import Process
num = 1
def run():
    global num
    num += 5
    print('在子进程1中num = %d'%(num))
def run1():
    global num
    num += 10
    print('在子进程2中num = %d'%(num))

if __name__ == "__main__":
    print('父进程启动！')
    p1 = Process(target=run)
    p2 = Process(target=run1)
    #两个子进程都开始运行，但是p1和p2到底谁先执行说不准。
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    #如果一定要p1执行完了再执行p2,可以如下操作
    #p1.start()
    #p1.join()
    #p2.start()
    #p2.join()
    print(num)

"""
打印结果如下:
父进程启动！
在子进程1中num = 6
在子进程2中num = 11

你可能会想，按照逻辑子进程2中num应该是16，但是因为在多个进程之间，它们的数据是不共享的，它们有各自独立的内存空间，
子进程创建的时候会导入父进程里的所有东西，会将num=1都导入到子进程中。
"""

