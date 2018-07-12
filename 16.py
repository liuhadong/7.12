print('请输入您的名字:')
name = input()
print('编号　星座  日期　　　   性格')
print('1　 　水瓶　1月20~2月18  xxx')
print('2     双鱼　2月19~3月20  xxx')
print('3     白羊  3月21~4月19  xxx')
print('4     金牛　4月20~5月20  xxx')
print('5     双子　5月21~6月21  xxx')
print('6     巨蟹　6月21~7月22  xxx')
print('7     狮子  7月23~8月22  xxx')
print('8     处女　8月23~9月22  xxx') 
print('请根据如上提示选择对应编号：')

number = int(input())
if number == 1:
    print('%s,您好！水瓶座的您分析结果：日期是1月20~2月18,性格是xxx。'%name)
elif number == 2:
    print('%s,您好！双鱼座的您分析结果：日期是2月19~3月20,性格是xxx。'%name)
elif number == 3:
    print('%s,您好！白羊座的您分析结果：日期是3月21~4月19,性格是xxx。'%name)
elif number == 4:
    print('%s,您好！金牛座的您分析结果：日期是4月20~5月20,性格是xxx。'%name)
elif number == 5:
    print('%s,您好！双子座的您分析结果：日期是5月21~6月21,性格是xxx。'%name)
elif number == 6:
    print('%s,您好！巨蟹座的您分析结果：日期是6月21~7月22,性格是xxx。'%name)
elif number == 7:
    print('%s,您好！狮子座的您分析结果：日期是7月23~8月22,性格是xxx。'%name)
elif number == 8:
    print('%s,您好！处女座的您分析结果：日期是8月23~9月22,性格是xxx。'%name)





