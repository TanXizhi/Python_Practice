# 测试LEGB规则：在python中查找‘名称’时，是按照LEGB规则查找的，即Local-->Enclosed-->Global-->Built in
#Local: 指的是函数或者类的方法内部
# Enclosed: 指的是嵌套函数（一个函数包裹着另一个函数，闭包）
#Global: 指的是模块中的全局变量
# Built in: 指的是python为自己保留的特殊名称
# 如果一个名称在所有命名空间中都没有找到，就会产生NameError

str = 'global'  # Global


def outer():
    str = 'outer'  # Enclosed

    def inner():
        str = 'inner'  # Local
        print(str)

    inner()


outer()
