# 多态是指同一个方法调用由于对象不同可能会产生不同的行为。
# 注意如下2点：1、多态是方法的多态，属性没有多态。2、多态的存在有2个必要条件：继承、方法重写。

class Man:
    def eat(self):
        print('饿了， 吃饭啦！')


class Chinese(Man):
    def eat(self):
        print('中国人吃饭用筷子')


class English(Man):
    def eat(self):
        print('英国人吃饭用叉子')


class Indian(Man):
    def eat(self):
        print('印度人吃饭用右手')


def manEat(m):
    if isinstance(m, Man):
        m.eat()  # 多态，一个方法调用，根据对象不同调用不同的方法
    else:
        print('不能吃饭')


manEat(Chinese())
manEat(English())
