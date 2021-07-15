N=int(input()) # input의 결과는 문자열 // 정수형 문자열을 정수로 바꾸는 함수 int('문자열')


i=1
result = 0 #누적합을 저장할 변수 하나 선언 
while i <= N:
    result +=i
    i +=1
print(result)