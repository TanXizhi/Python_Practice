# 测试继承的基本使用


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性，子类继承了父类的私有属性但是不能直接被子类用

    def say_age(self):
        print('年龄，年龄，我也不知道')


class Student(Person):

    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 定义子类时，必须在其构造函数中调用父类的构造函数，不然解释器不会去调用
        self.score = score


# Student-->Person-->object类   object类是所有类的父类，因此所有的类都有object类的属性和方法
print(Student.mro())    # mro()可以用来查看类的继承关系

s = Student('谭茜芷', 31, 100)
s.say_age()  # 继承父类方法
print(s.name)  # 继承父类属性

# print(s.age)  #私有属性不能直接被子类调用
obj = object()
print(dir(obj))  # 查看object类的所有属性
print(dir(s))  # 查看s子类的所有属性，包含了object类的所有属性
print(s._Person__age)  # 用此方法调用私有属性
