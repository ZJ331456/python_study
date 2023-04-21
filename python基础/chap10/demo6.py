# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo6.py 
@Author  ：zero 
@Date    ：2023/3/27 20:58  
"""
#函数的参数总结
def fun(a,b,c):  #a、b、c在函数的定义处，所以是形式参数
    print('a=',a,type(a))
    print('b=',b,type(b))
    print('c=',c,type(c))

#函数的调用参数
fun(1,2,3) #函数调用时的参数传递，称为位置传参
lst=[11,22,33]
# fun(lst)#TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst)

print('----------------------------')
fun(a=1,b=2,c=3)#关键字传参
dic={'a':11,'b':22,'c':33}
fun(**dic)