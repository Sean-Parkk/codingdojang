'''
date: 19/12/20

3개의 숫자를 입력으로 받고 3개의 숫자 중에 중간값을 가지는 숫자를 출력하세요.
ex1) 2, 5, 3 => 3 ex2) 4, 6, 4 => 4

http://codingdojang.com/scode/585?answer=20255#answer_20255
'''

def mid(a,b,c):
  print(sorted([a, b, c])[1])
