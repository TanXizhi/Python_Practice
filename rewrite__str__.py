# 测试重写object的__str__()

class Person:        #默认继承object根类

    def __init__(self, name):
        self.name = name
       

    def __str__(self):
        return '我的名字是:{0}'.format(self.name)


s = Person('谭茜芷')
print(s)