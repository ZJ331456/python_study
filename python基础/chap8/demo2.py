# 作者：立志成为大神的小白

# 开发时间：2023/3/18 14:11
#元组的创建方式
#1、直接使用小括号
t=('python','pycharm',66)
print(t)
print(type(t))

'''省略括号'''
t1='python','pycharm',66
print(t1,type(t1))

print('-----------------------')
'''当元组只有一个元素时'''
t3='python',
print(t3,type(t3))
t3='python'
print(t3,type(t3))


t4=('python',)
print(t4,type(t4))
t4=('python')
print(t4,type(t4))

#使用内置函数tuple()
t=tuple(('python','hello'))
print(t,type(t))
'''注意调用内置函数tuple()时，因为该函数只能输入一个参数，所以得用括号将多个参数值括起来'''



#3、空元组
'''空列表和空字典'''
l1=[]
l2=list()
print(l1,l2)

d1={}
d2=dict()
print(d1,d2)

'''空元组'''
t11=()
t22=tuple()
print(t11,t22)