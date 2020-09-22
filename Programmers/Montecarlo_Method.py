'''
date: 19/12/30

http://codingdojang.com/scode/507?answer=20403#answer_20403
'''

import random 
a = int(input('몇번 반복하시겠습니까?'))
result = 0
for i in range(a):
  x, y = random.uniform(0, 1), random.uniform(0, 1)
  if x**2 + y**2 <= 1:
    result += 1
print('파이값은 {:0.4f} 입니다.'.format(4*result/a))
