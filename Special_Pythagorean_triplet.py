'''
date: 

세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ). 예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2 이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

http://codingdojang.com/scode/545?answer=20246#answer_20246
'''

for a in range(1, 500):
  for b in range(a, 500):
    for c in range(b, 500):
      if (a**2 + b**2) == (c**2) and a+b+c == 1000:
        print('a*b*c: {}\na: {}, b: {}, c: {}, '.format(a*b*c,a,b,c))
