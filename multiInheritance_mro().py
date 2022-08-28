#python支持多重继承，如果父类中有相同名字的方法，在子类没有指定父类名时，解释器将从左向右按顺序搜索
#MRO(Method Resolution Order): 方法解析顺序。我们可以通过mro()方法获得‘类的层次结构‘

class A:
    def aa(self):
        print('aa')
    
    def say(self):
        print('say AAA!')

class B:
    def bb(self):
        print('bb')
    
    def say(self):
        print('say BBB!')

class C(B,A):
    def cc(self):
        print('cc')

c = C()
c.cc()
c.bb()
c.aa()
print(C.mro())     #打印类的层次结构
c.say()            #解释器寻找方法是从左至右的方式寻找， 此时会执行B类中的say()
    