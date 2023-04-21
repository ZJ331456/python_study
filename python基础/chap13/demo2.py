# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo2.py 
@Author  ：zero 
@Date    ：2023/4/3 21:51  
"""

#封装
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 两个_表示该变量不希望在类的外部使用

    def show(self):
        print(self.name + '已经' + self.__age + '岁了')

stu = Student('张三', '21')
stu.show()
#在类外使用name和age
print(stu.name)
# print(stu.__age)
# print(stu.age)
print(dir(stu))
print(stu._Student__age)
#dir()函数的参数是你传入的对象，它会返回对象的属性和方法。比如字符串，当你不记得某个方法的拼写就可以用该函数查询字符串的所有方法。