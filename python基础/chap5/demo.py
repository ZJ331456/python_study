# 作者：立志成为大神的小白

# 开发时间：2023/3/11 21:14
print(list(range(1,10,2)))
#range()函数的三种创建方式
#第一种---》只有一个参数在range函数的()里
r=range(3)
print(r)
print(list(r))
'''由此可以看出，当参数只有一个是，默认从0开始，到该参数就结束且不包含该参数'''
#第二种-----》有两个参数，第一个参数为生成数起始数字，第二个数字为截至数字但不包含该参数
r=range(3,10)
print(r)
print(list(r))
#第三种-----》有三个参数，第一个参数为生成数起始数字，第二个数字为截至数字但不包含该参数，第三个参数为每个数字之间间隔
print('----间隔1----')
r=range(3,10,1)
print(r)
print(list(r))
print('----间隔2----')
r=range(3,10,2)
print(r)
print(list(r))
#判断某个数字是否包含在所生成的数字序列中，使用in或者not in判断
print(2 in range(3,10))
print(2 not in range(3,10))