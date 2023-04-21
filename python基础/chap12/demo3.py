# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo3.py 
@Author  ：zero 
@Date    ：2023/3/30 22:10  
"""
#对象的创建
# import demo2
class Student:

    native_space='吉林'
    def __init__(self,name,age):
        self.name=name
        self.age=age
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


stu1= Student('张三', 20)
print(id(stu1))
print(type(stu1))
print(stu1)#实际输出的是该类在地址内存中的十六进制数
print('---------------------')
print(id(Student))
print(type(Student))
print(Student)
print('---------------------')
stu1.eat()   #对象名.方法名
stu1.method()
print(stu1.name)
print(stu1.age)

print('----------------------')
Student.eat(stu1) #与stu1.eat()功能相同，都是调用Student中的eat方法
                    #类名.方法名(类的对象)------>实际上就是方法定义处的self

stu1.cm()
Student.cm()
Student.method()