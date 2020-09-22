# N개의 최소공배수
* date: 20.05.16
* 난이도: 보통 
  * 재귀를 어떻게 구현할까 고민하다가, 그냥 반복문으로 해결함
* 링크: [프로그래머스 문제 보기](https://programmers.co.kr/learn/courses/30/lessons/12953)

### 문제
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.  
예를 들어 2와 7의 최소공배수는 14가 됩니다.  
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.  
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.


### 나의 풀이
```python
# 최소공배수 함수 정의
def lcm(m, n):
    def gcd(a, b): return b if a % b == 0 else gcd(b, a % b)
    return m * n / gcd(m, n)

# [a, b, c, d]가 있을 때, lcm(lcm(lcm(a, b),c)d)가 정답인 것을 찾아냄
def solution(arr):
    answer = 1
    for n in arr: answer = lcm(answer, n)    # 이 부분을 재귀로 해결하려다가 그냥 반복문으로 진행
    return answer
```
