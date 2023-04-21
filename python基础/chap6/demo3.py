# 作者：立志成为大神的小白

# 开发时间：2023/3/13 22:42

#获取列表元素中的多个元素---------》语法格式列表名[start:stop:step]
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
print(id(lst))
lst2=lst[1:5:2]
print(lst2)
print(id(lst2))
'''所以这个切片操作是重新开辟了一处空间地址，step默认为1'''
print('------step为正---------')
print(lst[1:3])

print('-------step为负---------')
print(lst[::-1])
'''当step为负数的时候就相当于逆序输出'''
print(lst[6::-1])
print(lst[6:1:-1])