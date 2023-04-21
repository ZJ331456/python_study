# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo5.py 
@Author  ：zero 
@Date    ：2023/3/27 20:43  
"""
#函数参数的定义
#1、个数可变的位置参数--------->结果为元组
def fun(*args):
    print(args)
fun(10)
fun(10,20,30)

#2、个数可变的关键字形参-------->结果为字典
def fun1(**args1):
    print(args1)
fun1(a=1,b=2,c=3,d=4)

'''def fun(*args,*args1)
    pass
以上代码程序会报错，个数可变的位置参数只能是一个
    def fun(**args,**args1)
    pass
以上代码程序会报错，个数可变的关键字参数只能是一个

'''
def fun(*args,**args1):
    pass

'''def fun(**args,*args1)
    pass
以上代码程序会报错
当一个函数同时定义了个数可变的位置参数和个数可变的关键字参数，要求个数可变的位置参数要在个数可变的关键字参数之前定义
    '''