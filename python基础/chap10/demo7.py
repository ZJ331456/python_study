# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo7.py 
@Author  ：zero 
@Date    ：2023/3/27 21:21  
"""
def fun(a,b=10):
    print('a=',a)
    print('b=',b)

def fun2(*args): #个数可变的位置参数
    print(args)

def fun3(**args1): #个数可变的关键字参数
    print(args1)

fun2(1,2,3,4,5,6,7,8,9,10)

fun3(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)

print('------------------------------------------------')
def fun4(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

#调用fun4函数
fun4(1,2,3,4)#位置实参传递
fun4(a=1,b=2,c=3,d=4)#关键字实参传递
fun4(1,2,c=3,d=4) #前面两个位置实参传递，后两个关键字实参传递
'''若c,d只能通过关键字实参传递'''
def fun5(a,b,*,c,d):  # 符号*的作用是，在函数调用时，处于*后面的参数只能采用关键字传递
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

fun5(1,4,c=1,d=4)


'''函数定义时的形参顺序问题'''
def fun6(a,b,*,c,d,**e):
    pass

def fun7(*a,**b):
    pass
def fun8(a,b=10,*c,**d):
    pass
'''def fun9(*a,*b):
    pass
    报错
def fun10(*,a,b):
    pass
    正常'''
