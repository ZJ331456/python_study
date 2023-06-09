# 作者：立志成为大神的小白

# 开发时间：2023/3/14 13:56
#列表元素的删除操作
#1、remove()方法  ---------->一次删除一个元素
lst=[1,2,3,4,5,6,7,8,9,10,2]
print('源列表：',lst)
lst.remove(2)
print('删除之后：',lst)
'''注意：若有重复元素，只删除第一个'''
# lst.remove(33)  若删除元素不存在表中，则会报错

#2、pop()函数---------------->删除一个指定索引位置的上的元素
lst=[1,2,3,4,5,6,7,8,9,10,2]
print('源列表：',lst)
lst.pop(10)
print('删除之后：',lst)
lst.pop()  #若是不指定索引值则默认删除最后一个元素
print('删除之后：',lst)
# lst.pop(11)  #若指定索引不存在，会报错


#3、切片----------------->一次至少删除一个元素，并且会产生一个新的列表对象
lst=[1,2,3,4,5,6,7,8,9,10,2]
print('源列表：',lst)
new_lst=lst[1:5]
print('切片后列表：',new_lst)
print('原列表id:',id(lst),'切片后列表id:',id(new_lst))
'''可见切片之后的id不一样'''
'''若要不产生新列表，而是删除源列表的元素'''
lst[1:5]=[]
print(lst,id(lst))



#4clear()函数清空列表中的元素，但是此列表所占用空间任然存在
lst.clear()
print(lst)


#5del函数----------------->直接删除该列表所用空间
del lst
print(lst)