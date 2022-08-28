# 测试组合
# ‘is-a'关系可以使用‘继承’，从而实现子类拥有父类的方法和属性；‘has-a'关系可以使用‘组合’，从而实现一个类拥有另一个类的方法和属性。

# 使用继承实现代码的复用
class A1:

    def say_a1(self):
        print('a1, a1, a1')


class B1(A1):
    pass


b1 = B1()
b1.say_a1()


# 同样的效果使用组合实现代码的复用
class A2:

    def say_a2(self):
        print('a2, a2, a2')


class B2:
    def __init__(self, a):  # 如果不用继承的方式，使B2能够使用A2，那么就需要把A2的对象作为B2的属性
        self.a = a


a2 = A2()
b2 = B2(a2)
b2.a.say_a2()


# 测试has-a关系，使用组合
class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print('计算CPU')
        print('cpu对象:', self)


class Screen:
    def show(self):
        print('显示一个好看的画面')
        print('screen对象:', self)


m = MobilePhone(CPU(), Screen())
m.cpu.calculate()
m.screen.show()
