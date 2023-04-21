# 作者：立志成为大神的小白

# 开发时间：2023/3/8 16:08

n1=1.1
n2=2.1
n3=2.2
print(n1+n2)
print(n1+n3)


#Decimal类型会自动保留小数点后面不需要的0，以与输入的精度相匹配
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))