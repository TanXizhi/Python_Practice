"""
属性私有化的问题：
1. xx
    一般情况下使用的变量，都能被使用
2. _xx
    在某个模块中，如果变量是_xx形式的，
    使用from import *的方式无法使用
3. __xx
    私有属性/私有方法 （只能在类内使用）
    名字被重整了（改名）,重载的原则：_类名__私有属性名, _类名__私有方法名。
                                这种访问方法不是官方提倡的，应该避免用这种方法访问。
4. __xx__
    主要用于方法
    __init__
    __del__
    __new__
    __str__
    以上方法叫做Magic Method, 且都有个共性，即不需要手动调用，系统会自动调用
    注意：自定义方法避免与魔法方法重名
5. xx_
    用于区分变量名/方法名


1&2以PI = 3.14为例创建文档TestModule
1. xx
import TestModule
print(TestModule.PI)
from TestModule import *
print(PI)
以上两种方式都可以输出结果为3.14

2. _xx
import TestModule
print(TestModule._PI)
from TestModule import *
print(_PI)
只有第一种方式可以输出结果为3.14，第二种方式报错

"""

# 3. __xx 只能在类中使用
class Person():
    def __init__(self, name, age):
        self.name = name
        #私有属性
        self.__age = age

    def showInfo(self):
        print("name:%s age:%d"%(self.name,self.__age))
    def __test(self):
        print("我是Person类中的私有方法")

# 以下输出结果为name:Xizhi age:18
P = Person('Xizhi',18)
P.showInfo()

#以下获取不到结果，因为age是私有属性不能被外部直接访问
# print(P.__age)

#查看私有属性__age名字重载后在系统中的存储名字
print(dir(P))

#调用私有属性在系统中存储的名字执行
print(P._Person__age)

#以下获取不到结果，因为test是私有方法不能被外部直接调用
#P.__test()

#调用私有方法在系统中存储的名字执行
P._Person__test()


