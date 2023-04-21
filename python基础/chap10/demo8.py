# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo8.py 
@Author  ：zero 
@Date    ：2023/3/27 21:37  
"""
#变量的作用域
name='张三'
def fun():
    print(name)
fun()
print(name)
'''全局变量：函数体外定义的变量，可作用于函数内外'''
def fun():
    global age
    age=18
    print(age)
fun()
print(age)
'''局部变量：函数体内定义并使用的变量，只在函数内部有效
当局部变量使用global声明之后，这个变量就会变成全局变量'''