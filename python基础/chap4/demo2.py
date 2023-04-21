# 作者：立志成为大神的小白

# 开发时间：2023/3/11 15:54


money=20000    #余额
print('-------输入取款操作--------')
s=int(input('请输入取款数额'))
#判断余额是否足够
if money>s:
    money=money-s
    print('取款成功，余额还有：',money)
else:
    print('余额不足，请从新输入')

'''
判断奇偶
num=int(input('请输入一个数'))
if num%2==0:
    print(num,'为偶数')
else:
    print(num,'为奇数')

'''

