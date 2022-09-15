"""
多进程可通过以下三种方式实现: Process、继承Process的子类、进程池
当子进程不多的时候可以用Process和Process子类实现，当子进程很多的时候可以用进程池实现

进程池的作用也是用来创建多个进程

multiprocessing.Pool常用函数解析:
    apply_async: 使用非阻塞方式调用func，即创建子进程并调用函数，不需要再调用start方法
    apply: 使用阻塞方式调用func 
           阻塞的意思是同一时间只能有一个进程在执行，当它执行完之后下一个进程排队执行，
           这种方式用的不多，和单进程区别不大，效率不高，了解即可
    close(): 关闭pool, 使其不再接受新的进程任务
    terminate(): 不管任务是否完成，立即终止
    join(): 主进程阻塞，等待子进程的退出，必须在close或terminate之后使用

"""

from multiprocessing import Pool
import time
def work(num):
    print(num)
    time.sleep(1)
if __name__ == "__main__":
    po = Pool() #括号中的参数是最大进程数，即可以同时运行的最大进程数，如果不填则默认为CPU的核数
    for i in range(20): #通过for循环执行20次
        po.apply_async(work,(i,)) #进程池创建了20个work进程，每次执行CPU核数的进程直到所有进程执行完
    po.close() #不再接受新的进程，是关闭pool并不是关闭进程的意思
    po.join() #让主进程等待进程池里的进程全部执行完，主进程再结束，join一定要放在close后面这是固定写法




    
