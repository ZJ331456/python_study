# 作者：立志成为大神的小白

# 开发时间：2023/3/11 20:26

'''
A 100-90
B 89-80
C 79-70
D 69-60
E 59-0

'''
sore=int(input('请输入你的成绩：'))
if sore<=100 and sore>=90:  #也可以写成--->if 90<=sore<=100:这种
    print('你的成绩评分为A')
elif sore<=89 and sore>=80:
    print('你的成绩评分为B')
elif sore<=79 and sore>=70:
    print('你的成绩评分为C')
elif sore<=69 and sore>=60:
    print('你的成绩评分为D')
elif sore<=59 and sore>=0:
    print('你的成绩并不合格')
else:
    print('你所输入的成绩并不合法，请重新输入')


