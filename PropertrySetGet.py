# @property装饰器的用法
# @property可以将一个方法的调用方式变成‘属性调用’

class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误!薪水在1000-50000之间')


'''
    如下是@property的一种替代方法, 当需要get和set属性的时候应首选如上@property方法实现
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print('录入错误!薪水在1000-50000之间')
'''


emp1 = Employee('谭茜芷', 30000)
# print(emp1.get_salary())
# emp1.set_salary(40000)
# print(emp1.get_salary())

print(emp1.salary)  # 像调用属性一样调用方法
emp1.salary = 40000
print(emp1.salary)
