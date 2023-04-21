# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo10.py 
@Author  ：zero 
@Date    ：2023/3/27 21:55  
"""

#斐波那契数列

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
'''输出第6为的数字'''
sum=fib(6)
print(sum)

for i in range(1,7):
    print(fib(i))