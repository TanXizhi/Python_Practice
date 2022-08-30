"""
包的概念(package):
    可以理解为文件夹, 前提是包中要包含一个__init__.py模块
包的作用：
    1、将模块归类、方便整理
    2、防止模块名冲突

包中的模块，名字会发生变化
    新名字： 包名.模块名

    MyMath
    Package01.MyMath

包中的模块如何使用：
    1、import 模块

    2、from 模块 import 变量, 函数, 类

"""


# import MyMath
# result =  MyMath.add(10,20)
# import Package01.MyMath
# result = Package01.MyMath.add(10,20)
# print(result)


from Package01.MyMath import *
result = add(10,20)
print(result)
result = sub(10,20)
print(result)
