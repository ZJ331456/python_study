# 作者：立志成为大神的小白

# 开发时间：2023/3/11 21:55
#计算1到100之间的偶数和
num=1
sum=0
while num<=100:
    if num%2==0:
        sum+=num;
    num+=1
print('1到100之间的所有偶数和为：',sum)
