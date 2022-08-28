# 测试方法的动态性

class Person:

    def work(self):
        print('努力上班！')


def study(name):
    print('{0}在学习'.format(name))


def workhard(self):
    print('好好工作，努力上班！')


Person.study = study
p = Person()
p.work()  # Persob.work(p)
p.study()  # Person.study(p)

Person.work = workhard
p.work()
