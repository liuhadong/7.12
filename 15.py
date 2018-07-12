import random

number =random.randint(1,3)
number = int(input('请输入：'))
if number == 1:
    print('显示您当前的余额')
elif number == 2:
    print('显示您当前剩余的流量，单位为Ｇ')
elif number == 3:
    print('显示您当前的剩余通话，单位为分钟')


