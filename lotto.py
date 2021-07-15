import random

numbers = range(1,46)

#random.sample(seq,k) : 시퀀스에서 랜덤한 중복되지 않는 길이의 k개의 리스트 반환
lotto =  random.sample(numbers,7)

print('로또 번호는 ', lotto)