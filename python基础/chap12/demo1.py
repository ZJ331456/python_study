# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo1.py 
@Author  ：zero 
@Date    ：2023/3/28 19:49  
"""


class Student:  #student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('{0}今年已经{1}岁了'.format(self.name,self.age))
#Python中一切皆对象,Student是对象吗
print(id(Student))
print(type(Student))
print(Student)
stu=Student('张三',20)
print(stu.name)#实例属性
print(stu.age)#实例属性
stu.info()#实例方法