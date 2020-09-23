# 2xn 타일링
* Date: 20.09.23
* 난이도: 중
* 문제 링크: [프로그래머스 문제 보기](https://programmers.co.kr/learn/courses/30/lessons/12900)

## 나의 풀이
```python
def solution(n):
    a, b = 1, 1
    for _ in range(n): a, b = b, (a+b) % 1000000007
    return a
```

* 처음에는 규칙을 찾으려고 1부터 8까지 해봤다.
* 재귀함수 패턴을 보이길래 재귀함수를 썼더니 런타임 오류가 났다.
* 그래서 for문으로 촤라락
