#조건문(if/else)
#미세먼지 농도(dust)

dust = 55
if dust > 50:
    print('50초과')
else:
    print('50이하')

# 0~20, 31~80, 81~150, 151~

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나2쁨')
elif dust >30:
    print('보통')
else:
    print("좋음")