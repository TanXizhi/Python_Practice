# 测试类方法

class Student:
    company = 'Otis'  # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def printCompany(cls):  # 类方法
        print(cls.company)
      # print(self.name)  #类方法和静态方法不能调用实例变量、实例方法


Student.printCompany()
