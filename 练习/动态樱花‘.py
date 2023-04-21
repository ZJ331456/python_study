# -*- coding: UTF-8 -*- 
""" 
@Project ：py学习  
@File    ：动态樱花‘.py 
@Author  ：zero 
@Date    ：2023/4/7 12:00  
"""

from turtle import *

'''import * 就是import某一个模块的所有的类。这样使用其中的函数时，就不用再用句点指出来自于哪个模块了。
就比如使用math模块，如果使用import math的话，使用math模块里面的add方法------>math.add()
如果使用from math import *,再使用math模块里面的add方法的话--------->add()即可，不需要添加前缀math'''
from random import *
from math import *


def tree(n, l):
    pd()  # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l)  # 画树枝
    if n > 0:
        b = random() * 15 + 10  # 右分支偏转角度
        c = random() * 15 + 10  # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7)  # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)
        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        # ran = random()
        #这里相比于原来随机添加了填充的圆圈，让樱花叶子看起来更多一点
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)
        # if (ran > 0.7):
        #     begin_fill()
        #     circle(3)
        #     fillcolor('pink')
        #     # 把原来随机生成的叶子换成了统一的粉色
        #     pencolor("pink")
        #     circle(3)
        #     if ran > 0.7:
        #         end_fill()
        #         left(90)
        # 添加0.3倍飘落的叶子
        if (random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random() * 40
            setheading(an)
            dis = int(800 * random() * 0.5 + 400 * random() * 0.3 + 200 * random() * 0.2)
            forward(dis)
            setheading(t)
            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n * 0.5 + 0.5, n * 0.4 + 0.4, n * 0.4 + 0.4)
            circle(2)
            left(90)
            pu()
            # 返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
        pu()
        backward(l)  # 返回


bgcolor(0.5, 0.5, 0.5)  # 背景色
ht()  # 隐藏turtle
speed(0)  # 速度 1-10 渐进，0最快
tracer(0, 0)
pu()  # 抬笔
backward(100)
left(90)  # 左转90度
pu()  # 抬
backward(300)  # 后退300
tree(1, 100)  # 递归7层
done()
