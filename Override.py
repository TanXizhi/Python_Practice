# 测试方法的重写


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def say_age(self):
        print('我的年龄:', self.__age)

    def say_introduce(self):
        print('我的名字是{0}'.format(self.name))


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 定义子类时，必须在其构造函数中调用父类的构造函数，不然解释器不会去调用
        self.score = score

    def say_introduce(self):
        '''重写父类的方法'''
        print('报告老师，我的名字是{0}!'.format(self.name))


s = Student('谭茜芷', 31, 100)
s.say_age()
s.say_introduce()
