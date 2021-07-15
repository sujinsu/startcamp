# 주석처리 해석x, 실행x 
# 주로 코드에 대한 설명, 메모 
# ctral + / : 선택문장 주석처리
# ctrl + home(+방향키) : 제일 앞으로이동 /  shift + 방향키 : 하나씩 드래그
#리스트 화용
import random

menu = ['한식','일식','중식','양식']
lunch = random.choice(menu)
print(lunch)

number = {'한식':'123-456','일식':'222-333','양식':'444-555','중식':'666-777'}
print(number[lunch])

print('오늘의 점심은',lunch,'입니다. 전화번호는 ',number[lunch], '입니다')
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]}입니다.')