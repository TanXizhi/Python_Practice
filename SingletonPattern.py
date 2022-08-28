# 测试单例模式

class Mysingleton:

    __obj = None  # 类属性
    __init_flag = True

    def __new__(cls, *args, **kwarges):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if Mysingleton.__init_flag:
            print('init......')
            self.name = name
            Mysingleton.__init_flag = False


a = Mysingleton('aa')
b = Mysingleton('bb')
print(a)
print(b)
c = Mysingleton('cc')
print(c)