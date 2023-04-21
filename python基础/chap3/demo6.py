# 作者：立志成为大神的小白

# 开发时间：2023/3/8 22:15

#比较运算符，其结果为bool型返回值
a=10
b=20
print('a>b?',a>b)
print('a<b?',a<b)
print('a==b?',a==b)
print('a!=b?',a!=b)
print('a>=b?',a>=b)
print('a<=b?',a<=b)

'''一个=表示赋值运算符 两个==表示是否相等的比较运算符
一个变量由三个部分组成----》标识、类型、值
==比较的是值
is(或者is not)比较的是标识
'''

print('--------对比==与is的区别----------')
c=1
d=2
print('c==d?',c==d)
print('c是d吗?',c is d)


list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1==list2)
print(list1 is list2)
print(list1!=list2)
print(list is not list2)
print('list1的id:',id(list1),'\nlist2的id:',id(list2))