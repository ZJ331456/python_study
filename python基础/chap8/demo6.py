# 作者：立志成为大神的小白

# 开发时间：2023/3/18 15:20
#集合的相关操作
#1、集合元素的判断操作
s={1,2,3,4,5,6,7,8,9}
print(1 in s)
print(10 not in s)

#2、集合元素的新增操作
#1、调用add()方法-------------->一次只能添加一个元素
s.add(11)
print(s)
#2、调用update()函数---------------->一次至少添加一个元素
s.update({22,33,44,1})
print(s)


#3、集合元素的删除操作
#调用remove()方法---------------->一次删除一个指定元素，如果元素不存在抛出KeyError
s.remove(1)
print(s)
# s.remove(111)
#调用discard()方法---------------->一次删除一个指定元素，如果指定元素不存在不抛出异常
s.discard(2)
print(s)
s.discard(111)
#调用pop()方法------------------------>一次删除一个任意函数,注意pop()方法不能有参数，否则会抛出异常TypeError: set.pop() takes no arguments (1 given)
s.pop()
print(s)
# s.pop(1)

#调用clear()方法---------------->清空整个集合
s.clear()
print(s)