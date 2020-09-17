# 소수 찾기 ver.2
* Date: 20.09.17
* 난이도: 중
* 문제 링크: [프로그래머스 문제 보기](https://programmers.co.kr/learn/courses/30/lessons/42839)

## 문제
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.  
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

## 나의 풀이
* 단순 소수 찾기가 아니라, 
  1. 주어진 수에 대해 순열을 구하고, 
  2. 그 중 소수인 것을 판별해야했다.
* i.를 어떻게 구현해야하나 찾아보다가 itertools 내에 permutations에 대해 알게됐다.
  * 순열 뿐 아니라 조합도 제공한다.
  
```python
from itertools import permutations
def solution(numbers):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, round(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # numbers로 구할 수 있는 모든 숫자 순열 구하기
    list_nums = []
    for digit in range(1, len(numbers)+1):
        list_nums += list(map(lambda x: int(x), (map(''.join, permutations(numbers, digit)))))
    
    return sum([isPrime(i) for i in set(list_nums)])
```
