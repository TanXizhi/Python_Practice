# 测试嵌套函数（内部函数）的定义
# 一般什么情况下使用嵌套函？1、封装---数据隐藏：即外部无法访问嵌套函数；
# 2、贯彻DRY(don't repeat yourself)原则：嵌套函数可以让我们在函数内部避免重复代码；
# 3、闭包

from pickle import TRUE


def outer():
    print('outer running')

    def inner01():
        print('inner01 running')

    inner01()


outer()


print('#'*30)


def printName(isChinese, firstName, lastName):
    def inner(a, b):
        print('{0} {1}'.format(a, b))

    if isChinese:
        inner(lastName, firstName)
    else:
        inner(firstName, lastName)


printName(True, '茜芷', '谭')
printName(False, 'Kayla', 'Tan')
