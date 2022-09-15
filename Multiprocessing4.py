"""
继承Process: 即创建Process子类对象，在子类中重写run方法，把要执行的代码放在run方法中
Process中的run方法: 进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法

"""

import multiprocessing 
import time

#def test():
#    n = 5
#    while n > 0:
#        print(n)
#        time.sleep(1)
#        n -= 1
#if __name__ == "__main__":
#    p = multiprocessing.Process(target=test)
#    p.start()
#    p.join()

class MyProcess(multiprocessing.Process):
    #重写父类的run方法
    def run(self):
        n = 5
        while n > 0:
           print(n)
           time.sleep(1)
           n -= 1

if __name__ == "__main__":
    p = MyProcess()
    p.start()
    p.join()

    
