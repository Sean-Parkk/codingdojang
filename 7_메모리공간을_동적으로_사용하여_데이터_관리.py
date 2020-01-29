'''
date: 19/12/18

프로그램 실행 순서:
- 입력할 정수의 개수를 사용자로부터 입력 받는다.
- 입력받은 정수의 개수만큼 정수를 입력받는다.
- 입력받은 정수의 합과 평균 값을 출력한다.
- 할당된 메모리공간을 비운다.

요구사항:
- 메모리공간은 사용자의 입력 수의 따라 변동된다.
- 사용한 공간은 마지막에 비워야 한다.
- 배열을 사용하면 안된다.

http://codingdojang.com/scode/478?answer=20215#answer_20215
'''

n = int(input('몇 개의 정수를 입력하시겠습니까?\n'))
m = []

for i in range(n):
  m.append(int(input('정수를 입력하세요.\n')))
sum_m, avg_m = sum(m), int(sum(m) / len(m))

print('합계: {}, 평균: {}'.format(sum_m, avg_m))
del sum_m, avg_m, n, m
