# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo6.py 
@Author  ：zero 
@Date    ：2023/4/3 22:32  
"""


# object类---->一般重写object类用于返回该对象的一个描述（object类有多种方法）
class Student:  #不带（）默认是继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我叫{0}，我今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 20)

print(dir(stu))


print(stu) #当你重写str方法之后，使用print(stu)默认会调用__str__()这样的方法
print(type(stu))


