# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：进程注意事项1_进程之间不共享全局变量.py 
@Author  ：zero 
@Date    ：2023/4/21 16:20  
"""

import multiprocessing
import time

#定义一个全局变量
c_list=[]

def add_data():
    print('task1:',id(c_list))
    for i in range(5):
        c_list.append(i)
        print('ADD:',c_list)
        # time.sleep(0.5)

def get_data():
    print('task2:', id(c_list))
    print('GET:',c_list)

if __name__ == '__main__':
    p1=multiprocessing.Process(target=add_data)
    p2=multiprocessing.Process(target=get_data)

    p1.start()
    #将子进程加入到当前进程之前
    #当前进程会等待p1进程执行完成后，在继承向后执行
    p1.join()

    p2.start()
    print('task1:',id(c_list))
    print('Main:',c_list)


'''我的地址都不一样
视频里都一样'''