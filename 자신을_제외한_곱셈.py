'''
date: 19/12/20

배열 [a, b, c, d]를 입력하면 배열[bcd, acd, abd, abc]를 출력하는 코드를 작성하시오.
(단, 나눗셈 사용 금지)
입출력되는 배열은 어떤 형식이든 상관없습니다.

http://codingdojang.com/scode/591?answer=20261#answer_20261
'''

def exclude(a, b, c, d):
  x0 = b*c*d
  x1 = a*c*d
  x2 = a*b*d
  x3 = a*b*c
  print(x0, x1, x2, x3)
