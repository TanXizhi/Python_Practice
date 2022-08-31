"""
异常: 就是不正常,当python检测到一个错误时,解释器就无法继续执行下去了,
     反而出现了一些错误提示,这就是所谓的异常

案例:
    需求:输入被除数与除数, 求商, 并打印结果
    a,b,c

问题：
    1、str -> int 如果str不是纯数字时, int()转换会出问题: ValueError: invalid literal for int() with base 10: 'a'
    2、被除数为0时会报错: ZeroDivisionError: division by zero

解决方案：
    1、使用if-else 增加相关的容错处理
        核心为求商并打印结果，而这种方法使得代码核心偏移
    2、异常处理方案(推荐,更简单,提升效率):
        try:
            可能出现问题的代码
        except:
            如果出现问题, 会执行该代码块
"""


a = input('请输入被除数:')
b = input('请输入除数:')

"""
#方案1
#str -> int
#如果字符串a和b全部都是由纯数字组成，再进行转换以及后续操作
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if b != 0:
        #求商
        c = a / b
        print('商为:{}'.format(c))
    else:
        print('除数不能为0')
else: 
    print('数字类型有误')
"""

#方案2(推荐)
try:
    a = int(a)
    b = int(b)
    c = a / b
    print('商为:{}'.format(c))
except: 
    print('输入类型有误/除数不能为0')