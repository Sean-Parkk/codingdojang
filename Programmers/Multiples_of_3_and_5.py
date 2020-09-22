'''
date: 19/12/17
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
http://codingdojang.com/scode/350?answer=20200#answer_20200
'''

result = 1
n = 1
while n < 1000:
  if n % 3 == 0 or n % 5 == 0:
    result += n
  n += 1

print(result)
