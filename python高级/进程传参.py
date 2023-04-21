# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：进程传参.py 
@Author  ：zero 
@Date    ：2023/4/21 15:49  
"""


#导包
import multiprocessing
import time

def task1(count):
    for i in range(count):
        print('task1 -',i+1)
        time.sleep(1)
def task2(content,count):
    for i in range(count):
        print(content,'-', i + 1)
        time.sleep(1)


if __name__ == '__main__':
    #利用args传参
    # p1=multiprocessing.Process(target=task1,args=(5,))
    # p2=multiprocessing.Process(target=task2,args=('python',5))

    #利用kwargs
    p1=multiprocessing.Process(target=task1,kwargs={'count':5})
    p2=multiprocessing.Process(target=task2,kwargs={'count':5,'content':'python'})

    p1.start()
    p2.start()