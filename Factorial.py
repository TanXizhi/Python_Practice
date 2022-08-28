def factorial(n):
    '''使用递归函数计算阶乘'''
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))

