# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo5.py 
@Author  ：zero 
@Date    ：2023/3/30 23:04  
"""
#动态绑定属性和方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'吃饭了')

stu1=Student('张三',20)
stu2=Student('李四',30)

print(stu2.eat())

'''动态绑定属性'''
stu1.gender='男'
print(stu1.name,stu1.age,stu1.gender)

'''动态绑定方法'''
def ds():
    print('动态绑定方法')
stu1.ds=ds
stu1.ds()
# stu2.ds()---->AttributeError: 'Student' object has no attribute 'ds'，因为并没有给stu2绑定ds函数