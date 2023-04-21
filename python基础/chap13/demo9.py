# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo9.py 
@Author  ：zero 
@Date    ：2023/4/4 15:30  
"""

#特殊方法
#1、__add__方法
a=1
b=6
print(a+b)
print(a.__add__(b))
print('--------------------------------')
class Studet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Studet('张三',18)
stu2=Studet('李四',20)
#s=stu1+stu2
#print(s)#TypeError: unsupported operand type(s) for +: 'Studet' and 'Studet'
#print(stu1.__add__(stu2)) #AttributeError: 'Studet' object has no attribute '__add__'. Did you mean: '__hash__'?
print(stu1+stu2)
#__len__
lst=[1,2,3,4,5,6,7,8,9]
print(len(lst))#len()函数是内置函数
print(lst.__len__())
#print(stu1.__len__())#AttributeError: 'Studet' object has no attribute '__len__'. Did you mean: '__le__'?
print(stu1.__len__())
stu3=Studet('王五',30)
