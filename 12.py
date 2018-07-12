print('在古希腊神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，但是不同的朵数的玫瑰花代表的含义是不用的')

number = int(input('请输入您想送几多玫瑰花，我会告诉你玫瑰花的含义：'))
if number == 1:
    print('你是我的唯一！')
elif number == 3:
    print('I Love You!')
elif number == 10: 
    print('十全十美')
elif number == 99:
    print('天长地久')
elif number == 108:
    print('求婚')
elif number == 999:
    print('土豪')
else:
    print('我也不知道了，您可以考虑送１朵，３朵，１０朵...')
