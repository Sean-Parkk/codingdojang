'''
date: 19/12/20

홀수와 짝수의 개수를 구하는 프로그램을 만들어라.

http://codingdojang.com/scode/613?answer=20267#answer_20267
'''

def oe(*n):
  odd = len([x for x in n if x % 2 == 0])
  print('홀수 {}개, 짝수 {}개'.format(odd, len(n)-odd))
