# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo3.py 
@Author  ：zero 
@Date    ：2023/3/27 20:10  
"""

#函数的返回值
def fun(num):
    ord=[]#存偶数
    even=[]#存奇数
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            ord.append(i)
    return ord,even

#函数调用
lst=[i for i in range(10)]
print(fun(lst))

'''函数的返回值
（1）如果函数没有返回值【函数值执行完之后不需要给调用处提供数据】则return可以省略不写
（2）函数的返回值，如果只是一个，直接返回类型
（3）函数的返回值，如果是多个，返回的结果为元组
'''
def fun1():
    print('hello')
    #return

def fun2():
    return 'hello'
str=fun2()
print(str)

def fun3():
    return 'hello','world'
print(fun3())


'''函数是否需要返回值，视情况而定'''