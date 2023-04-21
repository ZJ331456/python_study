# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo4.py 
@Author  ：zero 
@Date    ：2023/3/27 20:29  
"""
#函数参数的定义
def fun(a,b=120):
    print(a,b)

fun(100)
fun(100,100)
'''b默认值为120，但是可以给b赋值，如果给b一个新值那么默认值无效'''

print()
'''def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
如：print()里面end的默认值是换行'''
print('hello')
print('world')

print('hello',end='\t')
print('world')
