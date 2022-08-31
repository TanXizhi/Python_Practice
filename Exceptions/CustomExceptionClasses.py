"""
1、自定义异常
2、以及抛出自定义异常
    raise 异常对象

class 自定义异常(BaseException或者Exception):
    def __init__(self):
        pass

定义一个学生类, 私有属性gender, 提供对应的设置值以及访问值的方法
"""
#自定义一个异常类
class GenderException(Exception):
    def __init__(self):
        super().__init__()   #继承父类的init
        self.errMsg = '性别只能设置为男或女'


#定义一个学生类
class Student():
    def __init__(self, name, gender):
        self.name = name
        # self.__gender = gender  #用这种方法设置初始化gender仍然是有问题的，要对gender进行处理，方式同setGender方法，索性直接调用setGender
        self.setGender(gender)

    #设置性别
    def setGender(self, gender):
        if gender == 'Male' or gender == 'Female':
            self.__gender = gender
        else:
            #抛出异常（性别异常）
            raise GenderException()

    #获取性别
    def getGender(self):
        return self.__gender


    def showInfo(self):
        print('My Name:{0}  Sex:{1}'.format(self.name, self.__gender))

try:
    stu = Student('Tan Xizhi', '???')
except Exception as e:
    print(type(e))
    print(e.errMsg)

#try:
#    stu.setGender('Unknown')
#except Exception as e:
#    print(type(e))
#    # print(e.args)
#    print(e.errMsg)
#stu.showInfo()

