[![HitCount](http://hits.dwyl.com/Sean-Parkk/codingdojang.svg)](http://hits.dwyl.com/Sean-Parkk/codingdojang)

# codingdojang
1일 1코딩 파이썬 코딩 연습하기  
(프로그래머스, 백준)

## 새로 알게 된 것들
* bin
  * 2진수로 변환, 앞에 0b를 달고 str객체로 반환됨
* rjust (ljust도 있음)
  * 오른쪽으로 n자리만큼 정렬하고, 공백은 지정한 문자로 채움
  ```python 
  'abc'.rjust(5, '0')    # '00abc'
  ```
* gcd
  ```python
  def gcd(a, b):
      return b if a % b == 0 else gcd(b, a % b)
  ```
* lcm
  ```python 
  def lcm(a, b):
      return a * b / gcd(a, b)
  ```
* all
  * iterable 요소를 and연산 후 bool객체 반환
  ```python
  all([1,2,3,4,5])    # True
  all([0,1,2])    # False
  ```
* any
  * all을 or연산처리
  ```python
  any([1,1])    # True
  any([0,1])    # True
  any([0,0])    # False
  ```
* itertools 내 순열과 조합
  ```python
  from itertools import permutations    # 순열
  from itertools import combinations    # 조합
  list(map(''.join, permutations('123', 2)))    # ['12', '13', '21', '23', '31', '32']
  list(map(int, map(''.join, combinations('123', 2))))    # [12, 13, 23]
  ```
* N진법 구현
  ```python
  num = 153
  digit = 16
  T = '0123456789ABCDEF'
  result = ''
  
  while num:
      result = T[num%digit] + result
      num //= digit
  print(result)    # '99'
  ```
