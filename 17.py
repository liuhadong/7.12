BMI = float(80.5/1.75**2)
print('小明身高1.75,体重80.5kg，他的BMI指数为:'+str(BMI))

if BMI <18.5:
    print('过轻')
elif BMI >=18.5 <=25:
    print('正常')
elif BMI >25 <=28:
    print('过重')
elif BMI >28 <=32:
    print('肥胖')
elif BMI >32:
    print('严重肥胖')



