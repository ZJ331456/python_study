# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo10.py 
@Author  ：zero 
@Date    ：2023/4/4 16:28  
"""

# 特殊方法
#3、__new__方法
#4、__init__方法
class Person:
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为:{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1)))