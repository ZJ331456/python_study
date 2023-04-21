# 作者：立志成为大神的小白

# 开发时间：2023/3/13 21:43
lst=[1,2,3,4,5,6,7,8,9,10,2]
print('源列表：',lst)
new_lst=lst[1:5]
print('切片后列表：',new_lst)
print('原列表id:',id(lst),'切片后列表id:',id(new_lst))
print(lst)