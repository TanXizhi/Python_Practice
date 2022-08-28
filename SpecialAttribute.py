# 测试特殊属性

class A:
    pass


class B:
    pass


class C(B, A):
    def __init__(self, name):
        self.name = name

    def cc(self):
        print('cc')


c = C('Tan')

print(dir(c))   # 打印c的所有属性
print(c.__dict__)  # obj.__dict__打印对象的属性字典
print(c.__class__)  # obj.__class__打印对象所属的类
print(C.__bases__)  # class.__bases__打印类的基类元组（多继承）
print(C.__mro__)  # class.__mro__打印类的层次构
print(A.__subclasses__())  # class.__subclasses__()打印类的子类列表
