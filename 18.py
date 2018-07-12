name = 123
passwd = 123456
money = 666

name2 = int(input('输入账号：'))
passwd2 = int(input('输入密码：'))


if(name2 == name)and(passwd2 == passwd):
    print('开始取钱')
    money2 = float(input('请输入取钱金额：'))
    if money2 > money:
        print('没钱取毛线')
    elif money2 <= money: 
        money3 = 666-money2
        print('取了%s钱'%money2,'还剩%s'%money3)
else:
    print('非法账户')
   
