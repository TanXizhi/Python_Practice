# import MyMath        # MyMath是自定义模块，切换项目后找不到对应的模块
# print(MyMath.add(10,20))

# import random    # random是系统模块, 切换项目后仍然可用




import sys

# 解决方案1: 手动将MyMath所在路径加入到sys.path中
sys.path.append('/Users/tanx/Documents/Python_Code/Python_Practice/Module/Package01')
list1 = sys.path
for path in list1:
    print(path)

import MyMath        #找到对应模块
print(MyMath.add(10,20))    #调用自定义模块中封装好的函数

