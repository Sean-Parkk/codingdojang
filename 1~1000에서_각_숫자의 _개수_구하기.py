'''
date:

예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자

10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

http://codingdojang.com/scode/504?answer=20235#answer_20235
'''

n = int(input('숫자를 입력하세요.'))

count = {x: 0 for x in range(0,10)}

for x in range(0,n):
  for y in str(x):
    count[int(y)] +=1

print(count)
