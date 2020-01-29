'''
date: 19/12/17

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수
http://codingdojang.com/scode/406?answer=20201#answer_20201
'''

def pages(m, n):
  if m % n == 0:
    result = m // n
  else:
    result = (m // n) + 1
  return result
  
