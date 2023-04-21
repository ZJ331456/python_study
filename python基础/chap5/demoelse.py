# 作者：立志成为大神的小白

# 开发时间：2023/3/12 19:56
for _ in range(3):
    i=int(input('请输入密码：'))
    if i==666:
        print('密码输入正确')
        break
    else:
        print('密码输入错误')
else:
    print('不好意思，你三次密码均输入错误')



print('--------------------------------')
e=0
while e<3:
    i = int(input('请输入密码：'))
    if i == 666:
        print('密码输入正确')
        break
    else:
        print('密码输入错误')
    e+=1
else:
    print('不好意思，你三次密码均输入错误')