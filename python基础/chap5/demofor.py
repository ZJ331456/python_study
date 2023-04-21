# 作者：立志成为大神的小白

# 开发时间：2023/3/11 22:05
for i in range(1,20,2):
    print(i)
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)


'''for-i循环有两种情况'''
'''第一种是带参数'''
for item in 'python':
    print(item)
print('--------输出1到100之间所有偶数之和')
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)
'''第一种是不带参数，用来空循环只执行循环体里面的语句，用_代替设置变量'''
for _ in range(5):#输出五次
    print('你好')