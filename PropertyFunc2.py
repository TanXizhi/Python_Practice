"""
property的使用:
    私有属性，提供开放接口，供外界访问
"""

class Student():
    def __init__(self, name, age):
        self.name = name
        #私有属性
        self.__age = age
    def getAge(self):
        return self.__age
    def setAge(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise TypeError('类型错误')

    #使用property简化私有属性的访问方式
    age = property(getAge, setAge)
        
stu1 = Student('Xizhi', 18)
#print(stu1.__age) 因为age已经私有化了，不能直接访问，而应该通过接口（这种情况是getAge,setAge）访问

#可通过如下方式供外界访问
#stu1.setAge(20)
#print(stu1.getAge())

#使用property简化外界的访问方式
print(stu1.age)
stu1.age = 19
print(stu1.age)

