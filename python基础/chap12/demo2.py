# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo2.py 
@Author  ：zero 
@Date    ：2023/3/28 19:49  
"""
#定义python里面的类
class Student:  #student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_space='吉林'  #直接写在类里面的变量称为类属性

    def __init__(self,name,age):#name和age是实例属性
        self.name=name  #self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age=age
    #实例方法
    def eat(self):
            print('学生在吃饭')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

'''在类之外定义的称为函数，在类之内定义的称为方法'''
def drink():
    print('喝水')