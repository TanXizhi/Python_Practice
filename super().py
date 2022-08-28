# 测试super()，代表父类的定义，而不是父类的对象
# 子类中，如果想要获得父类的方法时，我们可以通过super()来做


class A:

    def say(self):
        print('A:', self)


class B(A):

    def say(self):
        # A.say(self)      #可通过左边的代码调用父类的方法
        super().say()  # 也可以通过super()调用父类的方法
        print('B:', self)


B().say()
