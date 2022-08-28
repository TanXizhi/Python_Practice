# 测试私有属性、私有方法

class Employee:

    __company = 'OTIS'  # 类属性私有

    def __init__(self, name, age):
        self.name = name  # 公有属性
        self.__age = age  # 私有属性

    def __work(self):  # 私有方法
        print('努力工作！')
        print('年龄：{0}'.format(self.__age))  # 私有属性类内部直接调用
        print(Employee.__company)  # 私有的类属性类内部直接调用


e = Employee('谭茜芷', 31)

print(e.name)  # 调用公有属性
# print(e.__age)           #类外部不能用此方法调用私有属性
print(e._Employee__age)  # age属性私有，类外部应通过类名_Employee__age进行调用
print(dir(e))  # 查看所有属性存储方式
e._Employee__work()  # work方法私有，类外部应通过类名_Employee__work()进行调用
# company类属性私有，类外部应通过类名_Employee__company进行调用
print(Employee._Employee__company)
