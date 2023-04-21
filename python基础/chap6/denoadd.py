# 作者：立志成为大神的小白

# 开发时间：2023/3/14 10:20



#向列表的末尾添加元素
#1、append()方法---------》在列表末尾添加一个元素
lst=['hello','world','python',1]
print('添加之前：',lst)
lst.append(2)
print('添加之后',lst)
'''注意：append一次只能添加一个元素,'''
lst2=[2,3,4,5,6]
lst.append(lst2)   #使用append()函数向原列表之后添加一个新列表，是将这个新列表当一个元素存储的
print(lst)
#2、extend()在末尾至少添加一个元素
print('--------------')
lst=['hello','world','python',1]
print('添加之前：',lst)
# lst.extend('2''3''4''5')
# lst.extend('uu')
lst.extend([2,3,4,5,6])
#lst.extend(lst2)  #使用extend()函数向原列表之后添加一个新列表，是将这个新列表直接接在源列表后面
print('添加之后：',lst)

print('---------------------------------------------')
#3、insert()函数是指在列表任意位置添加一个元素
lst=['hello','world','python',1]
print('添加之前：',lst)
lst.insert(1,99)
print('添加之后：',lst)
'''insert()有两个参数，第一个是添加位置，第二个是所要添加的元素'''

print('-----------------------------------------------')
#4、切片方法在任意位置添加多个元素
lst=['hello','world','python',1]
print('添加之前：',lst)
lst2=[1,2,3,4]
lst[1:2]=lst2
print('切片之后：',lst)
'''切片就是在你需要添加元素的位置进行添加，如果切片范围包含有原来元素就会覆盖，如果不包含就不会覆盖，
列表[:]有两个参数，第一个为起始位置，第二个为终止位置
'''
lst3=lst[1:3:2]
print(lst3)
lst4=lst[1:3:1]
print(lst4)
print('------------------------------')
lst=['hello','world','python',1]
print('添加之前：',lst)
lst22=[2,3,4,5,6,7,8]
lst[4:]=lst22
print(lst)