height = int(input('输入你的身高(单位:cm):'))
vale = int(input('输入你的身价:'))
face = int(input('输入你的颜值分:'))

if height >=180 and vale >=1000000 and face >=99:
    print('高富帅')
elif vale >=1000000 and face >=99:
    print('富帅')
elif face >=99:
    print('帅')
elif height <=160 and vale <=100 and face <=60:
    print('矮穷矬')
