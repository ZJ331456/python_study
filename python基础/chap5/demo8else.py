# 作者：立志成为大神的小白

# 开发时间：2023/3/13 14:07
for i in range(1,10):
    for j in range(1,i+1):
      print('*',end=' ')
    print('\t')

# print('-------研究print()作用-------')
# print('1')
# # print()
# print('2')

print('----------99乘法表---------')
for i in range(1,10):
    for j in range(1,i+1):
        num=i*j
        print(i,'*',j,'=',i*j,end='\t')
    print()


