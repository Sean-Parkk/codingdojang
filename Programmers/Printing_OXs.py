'''
date: 19/12/18

input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.

http://codingdojang.com/scode/492?answer=20227#answer_20227
'''

n = int(input('숫자를 입력하세요.'))
for i in range(1,n+1):
  print('O'*(n-i) + 'X' * (i))
