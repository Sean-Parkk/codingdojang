'''
date: 19/12/20

3개의 각으로 삼각형의 예각, 직각, 둔각을 구별하는 프로그램을 만들어라.

http://codingdojang.com/scode/614?answer=20269#answer_20269
'''

def triangle(*v):
  if len(v) !=3 or sum(v) != 180 or min(v) <= 0: print('삼각형이 아님')
  else: print('둔각삼각형' if max(v) > 90 else '직각삼각형' if max(v) == 90 else '예각삼각형')
