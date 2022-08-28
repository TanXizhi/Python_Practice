#测试nonlocal, global关键字的用法

a = 100


def outer():
    b = 10

    def inner():
        nonlocal b  # 声明外部函数的局部变量
        print('inner b:', b)
        b = 30

        global a  # 声明全局变量
        print('inner a:', a)
        a = 400

    inner()
    print('outer b:', b)


outer()
print('outer a:', a)
