print('为了您和他人的安全，严禁酒后驾车！')

number = int(input('每100毫升血液的酒精含量：'))
if number>20:
    if number>=20 and number <=80:
        print('您已经达到酒后驾驶的标准，请千万不要开车。')
    else:
        print('您已经达到醉酒的标准，请不要开车。' )
else:
    print('您还构不成饮酒行为，可以开车，但要注意安全。')
