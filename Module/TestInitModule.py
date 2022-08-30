"""
package中的__init__.py是初始化模块
class中的__init__是初始化方法
以上两者都是用来初始化的
首次使用包中的模块时，__init__.py模块会被执行一次

__init__.py中可以存放什么？
    可以存放同普通模块一样的代码，比如变量，类，函数...都是可以的，但是一般情况下不会写这些
    一般会写一些辅助代码，让你更方便的使用模块


--------------------------------
#__init__.py方便模块使用1
在测试文件中： import 包
在包的__init__.py模块中: import 模块
这种方式等价于: 测试文件中使用  import 包.模块

--------------------------------
#__init__.py方便模块使用2
在测试文件中： from 包 import *
在包的__init__.py模块中: from .模块 import *
这种方式等价于: 测试文件中使用  from 包.模块 import *

"""

#import Package01.MyMath
#import Package01.MyMath

#__init__.py方便模块使用1
#import Package01           #等价于import Package01.MyMath
#result = Package01.MyMath.add(10,20)
#print(result)

#__init__.py方便模块使用2
from Package01 import *    #等价于 from Package0.Mymath import *
result = add(10,20)
print(result)
