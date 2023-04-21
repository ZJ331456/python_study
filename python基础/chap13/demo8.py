# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo8.py 
@Author  ：zero 
@Date    ：2023/4/4 15:11  
"""
#特殊属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class D(A):
    pass
#创建C的类对象
x=C('Andy',20)
print(x.__dict__) #输出实例对象的字典属性
print(C.__dict__)  #对类对象使用的话：你会看到他的一个属性和方法的一个字典
print(
'----------------------'
)
print(x.__class__)  #<class '__main__.C'>---->输出的是x对象所属的类
print(C.__class__)
print(C.__bases__)  #输出C类的所有父类类型的元素
print(C.__base__)   #输出C类的一个父类，采取就近原则，在创建c(a,b)时，a挨的近就输出a
print(C.__mro__)   #输出C类的类的层次结构
print(A.__subclasses__())  #输出A的所有子类列表