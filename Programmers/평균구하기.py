'''
date: 19/12/20

리스트에 있는 숫자들의 평균을 구하는 프로그램을 만들어라.

http://codingdojang.com/scode/610?answer=20264#answer_20264
'''

def avg(*a):
  return sum(a) / len(a)
