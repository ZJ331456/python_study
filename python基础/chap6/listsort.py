# 作者：立志成为大神的小白

# 开发时间：2023/3/14 15:33
#列表元素的排序操作
#1、调用sort()方法-------------------->列表中所有元素按从小到大排列，可以指定reverse=True,进行降序排序
lst=[22,12,34,67,10,99]
print(lst,id(lst))
lst.sort()
print(lst,id(lst))
'''由此可以看出sort()方法是将原来列表值直接进行修改，不占用新的区域'''
#逆序
lst.sort(reverse=True)
print('逆序输出:',lst)
lst.sort(reverse=False)
print('升序输出：',lst)

print('------------------------------------------------------------')
#2、调用内置函数sorted()
lst=[22,12,34,67,10,99]
print(lst,id(lst))
new_lst=sorted(lst)
print('排序后：',new_lst,id(new_lst))
desc_lst=sorted(lst,reverse=True)
print('逆序后',desc_lst,id(desc_lst))