# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo7.py 
@Author  ：zero 
@Date    ：2023/4/4 14:59  
"""
class Animal:
    def eat(self):
        print('动物会吃')

class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person:
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Person())