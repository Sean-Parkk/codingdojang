'''
date: 19/12/22

문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

입력 예시: aaabbcccccca

출력 예시: a3b2c6a1

http://codingdojang.com/scode/465?answer=20305#answer_20305
'''

a = str(input('문자열를 입력하시오: '))
result = a[0]
count = 0

for i in a:
  if i == result[-1]:
    count +=1
  else:
    result += str(count) + i
    count = 1
result += str(count)

result
