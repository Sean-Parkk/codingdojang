'''
date: 19/12/20

리스트에 있는 숫자들의 중앙값을 구하는 프로그램을 만들어라.

http://codingdojang.com/scode/611?answer=20266#answer_20266
'''

def midvalue(*x):
  a = list(x)
  a.sort()
  print(a[int(len(a)/2)] if len(a) % 2 == 1 else (a[int(len(a)/2-1)]+a[int(len(a)/2)])/2)

midvalue(7, 9, 14) #9
midvalue(24, 31, 35, 49) #33.0
midvalue(17, 37, 37, 47, 57) #37
