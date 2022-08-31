"""
try:
    可能出现问题的代码
except 异常1:
    如果出现问题, 会执行该代码块
except 异常2:
    如果出现问题, 会执行该代码块
except 异常3:
    如果出现问题, 会执行该代码块
......

如果代码错误不包括在以上异常中, 则python系统会报错。
因此在不知道错误类型的时候可以添加父类异常Exception(几乎包含了所有异常),如下：
except Exception:         
    print('其他异常‘)

注意:多个异常之间有顺序要求, 不能把except Exception放在最前面
    应该是子类异常在前, 父类异常在后。
    
"""


a = input('请输入被除数:')
b = input('请输入除数:')
try:
    a = int(a)
    b = int(b)
    c = a / b
    print('商为:{}'.format(c))
except ValueError:
    print('输入类型有误')
except ZeroDivisionError:
    print('除数不能为0')
