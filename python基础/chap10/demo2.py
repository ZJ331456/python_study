# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo2.py 
@Author  ：zero 
@Date    ：2023/3/27 19:48  
"""

#函数参数的传递
def fun(arg1,arg2):
    print('arg1:',arg1)
    print('arg2:',arg2)
    arg1=100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2:', arg2)

n1=11
n2=[22,33,44]
fun(n1,n2)
'''将位置传参，arg1、arg2，是函数定义处的形参，n1,n2是函数调用处的实参------>总结：实参名称可以与形参名称不一致'''
print(n1,n2)
'''在函数的调用过程中：进行参数的传递，
如果是不可变对象在函数体内的修改不会影响实参的值-------->arg1的值修改为100，n1的值不变
如果是可变对象，在函数体内的修改会影响实参的值-------->arg2的值增加了一个10，n2的值随之改变
'''
