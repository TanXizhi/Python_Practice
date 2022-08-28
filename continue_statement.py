#!/usr/bin/env python3
#continue statement

for letter in 'python':   #第一个实例
    if letter=='h':
        continue
    print('当前字母:',letter)
    
var=10
while var>10:        #第二个实例
    var-=1
    if var==5:
        continue
    
    print('当前变量值：',var)
print('Good bye!')



#In many cases,however,simply using an if statement is just as good.
#for letter in 'python':
    #if not (letter=='h'):
        #print('当前字母:',letter)
