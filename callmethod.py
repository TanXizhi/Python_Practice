# __call__方法的对象，被称为‘可调用的对象’，即该对象可以像函数一样被调用

class SalaryAccount:
    '''工费计算类'''

    def __call__(self, salary):
        print('工资计算如下：')
        yearSalary = salary*12
        daySalary = salary//20
        hourSalary = daySalary//8

        return dict(yearSalary=yearSalary, monthSalary=salary, daySalary=daySalary, hourSalary=hourSalary)


s = SalaryAccount()
print(s(30000))
