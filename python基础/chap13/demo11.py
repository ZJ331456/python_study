# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：demo11.py 
@Author  ：zero 
@Date    ：2023/4/4 22:33  
"""

#类的浅拷贝与深拷贝
#1、类的浅拷贝
#浅拷贝 . Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
class CPU:
    def __init__(self,xh1):
        self.xh1=xh1
    def prin(self):
        print('cpu型号为：{0}'.format(self.xh1))
class Disk:
    def __init__(self, xh2):
        self.xh = xh2
    def prin(self):
        print('硬盘型号为：{0}'.format(self.xh2))
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
    # def prin(self,xh1,xh2):
    #     super().prin()
    #     print('cpu型号为：{0}，硬盘型号为：{1}'.format(self.xh1,self.xh2))


#(1)变量的赋值
cpu1=CPU('i5')
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
'''
<__main__.CPU object at 0x000001A6616A1610> 1814110541328 
<__main__.CPU object at 0x000001A6616A1610> 1814110541328
'''
#(2) 类有浅拷贝
print('------------------------------')
disk=Disk('LTC') #创建一个银盘类的对象
computer=Computer(cpu1,disk)
print(disk)
#浅拷贝
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
'''
<__main__.Computer object at 0x000001C0F5A51710> <__main__.CPU object at 0x000001C0F5A516D0> <__main__.Disk object at 0x000001C0F5A51750> 
<__main__.Computer object at 0x000001C0F5A51810> <__main__.CPU object at 0x000001C0F5A516D0> <__main__.Disk object at 0x000001C0F5A51750>
'''
'''
浅拷贝只有类对象的地址不同，而类对象的子对象地址相同
'''

print('-----------------------------------------')
#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
'''
<__main__.Computer object at 0x0000028C6CEA1790> <__main__.CPU object at 0x0000028C6CEA1750> <__main__.Disk object at 0x0000028C6CEA17D0> 
<__main__.Computer object at 0x0000028C6CEA18D0> <__main__.CPU object at 0x0000028C6CC450D0> <__main__.Disk object at 0x0000028C6CEA1810>
'''

'''
深拷贝 ·使用copy模块的deepcopv函数．递归堵拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
'''

computer.cpu.prin()
computer2.cpu.prin()
computer3.cpu.prin()