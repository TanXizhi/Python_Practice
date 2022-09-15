"""
多进程
    Process类的常用属性:
        Process(target, name, args)
        参数介绍：
            target---表示调用对象，即子进程要执行的任务(即调用的函数名)
            args---表示调用对象的位置参数元组, 即传给函数的参数且必须以元组的形式写, 
                   args=(1,),如果没有参数可以不写
            name---表示子进程的名字，即当前进程实例别名，可以手动命名，也可以不填
                   当不填的时候系统默认为Process-N，N为从1开始递增的整数
            例子: p = Process(target=run, name='进程1', args=("test",)) 
            pid---表示当前进程实例的pid值，每执行一次任务系统都会赋予进程实例不同的pid值

    Process类的常用方法:
        p.start(): 启动进程，并调用该子进程中的p.run()
        p.run(): 进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法（此方法之后会详细介绍）
        p.terminate(): 强制终止进程p，不会进行任何清理操作 （了解即可）
        p.is_alive(): 如果p仍然运行，返回True。用来判断进程是否还在运行
        p.join([timeout]): 主进程等待p终止，timeout是可选的超时时间


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
    print(p1.pid)
    p1.join(5)  #作用是让主进程等待子进程结束