"""
==:
    用来比较两个变量的值是否相等
is:
    用来比较两个变量是否为同一个(是否为同一个地址)

基本类型：
    小整数池[-5, 256]: 在原生IDE中, 这个范围内的数值共享同一个地址, 这个范围外的数值
                     出现一次就要重新创建一个地址。所以在原生IDE中,当数值为1000时,
                     a is b 答案是False.

引用类型：

"""

#a = 10
#b = 10
a = 1000
b = 1000
print(a == b)
print(a is b)
print(id(a))
print(id(b))

c = [1,2,3]
d = [1,2,3]
print(c == d)
print(c is d)
print(id(c))
print(id(d))
print(c[0] is d[0])