"""
try:
    可能出现问题的代码
except (异常1, 异常2, 异常3, ...) as e:
    print(type(e)) #打印异常类型
    print(e) #打印错误信息
    如果出现问题, 会执行该代码块
......


注意:使用元组存储多个异常的时候, 异常之间没有顺序要求
    
"""


a = input('请输入被除数:')
b = input('请输入除数:')
try:
    a = int(a)
    b = int(b)
    c = a / b
    print('商为:{}'.format(c))
except (Exception, ValueError, ZeroDivisionError) as e:
    print(type(e))
    print(e.args)
    print('输入类型有误')
