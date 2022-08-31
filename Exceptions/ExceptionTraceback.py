"""
异常处理的传递机制
"""


def test1():
    print('-'*10 + 'test1开始' + '-'*10)
    # 异常, python解释器遇到无法解释的代码时会报错，aa为不正确输入
    print(aa)
    print('-'*10 + 'test1结束' + '-'*10)
def test2():
    print('-'*10 + 'test2开始' + '-'*10)
    test1()
    print('-'*10 + 'test2结束' + '-'*10)
def test3():
    print('-'*10 + 'test3开始' + '-'*10)
    # test2()
    try:            #进行了异常处理，代码可执行完
        test2()    
    except:
        pass
    print('-'*10 + 'test3结束' + '-'*10)

test3()
