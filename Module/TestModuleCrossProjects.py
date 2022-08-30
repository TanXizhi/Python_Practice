"""
1、模块的发布
    a. 为什么要发布
        自定义模块，切换项目后不好用
        系统模块，切换项目后仍然可用
    b. sys.path
        导入模块时，搜索路径列表，如果所有路径中都没有导入的模块，会导致无法导入目标模块
        解决方案：
            1、将模块所在路径手动加入到sys.path中
            2、将自定义模块发布到系统目录
                发布自定义模块的步骤：
                    1、确定发布的模块(目录结构)
                    |--setup.py
                    |--package
                        |
                        --自定义模块 MyMath
                    2、setup的编辑工作
                        setup()
                    3、构建模块
                        python setup.py build
                    4、发布模块
                        python setup.py sdist

2、模块的安装
    2.1 通过命令完成安装（推荐，更安全）
        a. 找到之前发布的压缩包，解压操作
        b. 找到对应的文件,执行命令python setup.py install
        注意:以上命令是默认安装在系统文件夹。如果在install的时候,指定目录安装,可以使用python setup.py install --prefix=安装路径

    2.2 暴力安装
        直接将要安装的包, 以及模块, 复制到对应的系统目录中
"""

# import MyMath
# print(MyMath.add(10,20))
# import random

import sys
list1 = sys.path
for path in list1:
    print(path)

