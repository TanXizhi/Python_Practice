class Student:  # 类名一般首字母大写，多个单词采用驼峰原则

    def __init__(self, name, score):  # self必须位于第一个参数; 构造函数用于初始化对象，即给实例属性赋值
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print('{0}的分数是: {1}'.format(self.name, self.score))


s1 = Student('Xizhi', 100)    #通过类名Student调用构造函数__init__
s1.say_score()
