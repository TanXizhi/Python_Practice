"""
@property 
@属性.setter
装饰器:简化私有属性的访问方式, 使用@property取代get和set方法

"""

class Account():
    def __init__(self):
        #私有属性
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            raise Exception('金钱类型错误')

m = Account()
m.money = 100
print(m.money)