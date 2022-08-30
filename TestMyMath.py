"""
导入自定义模块
1. import模块
    问题：在导入模块时，模块中的代码会被执行一遍
    解决方案：在自定义模块中新增控制代码
             if __name__ == '__main__':
                测试代码执行

2. from 模块 import 函数...
"""


# import MyMath
a = 10
b = 20
# print('和:{}'. format(MyMath.add(a,b)))


from Module.MyMath import add, sub, mul, div
print('和:{}'. format(add(a,b)))