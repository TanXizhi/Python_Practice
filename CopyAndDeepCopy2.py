"""
深浅复制：
    1、浅复制
        copy.copy()
    2、深复制
        copy.deepcopy()
    
    区别与联系：
        1、联系
            复制出一个新的备份出来
        2、区别
            对于普通的对象，深浅复制没有区别
            如果目标对象是一个复合对象（一个对象的成员变量还是对象）的话, 深浅复制有区别
                深复制:递归复制 (复制本身及其子对象)
                浅复制:只复制直接对象
            普通对象:
            list1 = [1,2,3]
            复合对象:
            list2 = [[1,2],[3,4]]
"""

import copy

print('-'*10,'普通对象','-'*10)
list1 = [1,2,3]
#浅复制
list2 = copy.copy(list1)
#深复制
list3 = copy.deepcopy(list1)
print(list2)
print(list2 is list1)
print(id(list2))
print('-'*30)
print(list3)
print(list3 is list1)
print(id(list3))

print('-'*10,'复合对象','-'*10)
list1 = [1,2]
list2 = [3,4]
#复合对象
list3 = [list1,list2]
#浅复制
list4 = copy.copy(list3)
#深复制
list5 = copy.deepcopy(list3)
print(list4)
print(list4 is list3)
print(id(list4))
print(list4[0] is list3[0])
print('-'*30)
print(list5)
print(list5 is list3)
print(id(list5))
print(list5[0] is list3[0])