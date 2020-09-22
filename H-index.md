# H-index
* Date: 20.09.22
* 난이도: 중간
  * 문제 자체 지문이 모호해서 이해하는데에 어려웠지, 코드 구현은 쉬웠음
* 문제 링크: [프로그래머스 문제 보기](https://programmers.co.kr/learn/courses/30/lessons/42747)


## 문제
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.  
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.  

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.  
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.  

## 나의 풀이
```python
def solution(citations):
    result = []
    for idx, i in enumerate(sorted(citations)):
        result.append(min(i, len(citations[idx:])))
    return max(result)
```
