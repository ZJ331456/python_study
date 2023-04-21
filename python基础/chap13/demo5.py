# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo5.py 
@Author  ：zero 
@Date    ：2023/4/3 22:19  
"""

#方法重写
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
    def info(self):
        super().info()  #方法重写
        print('学号：' + self.stu_no)
class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear=teachofyear
    def info(self):
        super().info()
        print('教龄：'+self.teachofyear)
stu=Student('张三',20,'1001')
stu.info()
print('--------------------------------------')
teacher=Teacher('李四',34,'10')
teacher.info()