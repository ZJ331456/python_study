# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo4.py 
@Author  ：zero 
@Date    ：2023/3/30 22:28  
"""
#类属性、类方法、静态方法的使用方式

class Student:
    native_space='吉林'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
            print('学生在吃饭')
    #静态方法
    @staticmethod
    def sm():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

#类属性的使用
print(Student.native_space)
stu1=Student('张三',18)
stu2=Student('李四',20)
print(stu1.native_space)
print(stu2.native_space)
Student.native_space='天津'
print(stu1.native_space)
print(stu2.native_space)

print('-------------------类方法的使用方式---------------------')
Student.cm()
print('-------------------静态方法的使用方式---------------------')
Student.sm()
