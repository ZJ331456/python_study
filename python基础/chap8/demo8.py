# 作者：立志成为大神的小白

# 开发时间：2023/3/18 16:00
#集合的数学操作
#1、交集
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1.intersection(s2))
print(s1 & s2)
print(s1)
print(s2)
print('----------------------')
#2、并集操作
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)
print('-------------------------')
#3、差集操作
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
print(s1)
print(s2)
print('------------------')
#4、对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)
# print(s1.symmetric_difference_update(s2))