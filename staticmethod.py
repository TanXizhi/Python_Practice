# 测试静态方法：静态方法是与类对象无关的方法
# 静态方法和在模块中定义普通函数没有区别，只不过静态方法放到了类的名字空间里面，需要通过类调用。

class Student:
    company = 'Otis'  # 类属性

    @staticmethod
    def add(a, b):  # 静态方法
        print('{0}+{1}={2}'.format(a, b, a+b))


Student.add(10, 20)
