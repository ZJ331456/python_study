# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo3.py 
@Author  ：zero 
@Date    ：2023/4/3 22:02  
"""
#继承
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear=teachofyear

stu=Student('张三',20,'1001')
stu.info()
teacher=Teacher('李四',34,10)
teacher.info()

