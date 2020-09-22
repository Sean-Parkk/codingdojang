'''
date: 19/12/20

DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자.

입력 - 화면에서 숫자로 된 문자열을 입력받는다.
>> "4546793"

출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
>> "454*67-9-3"

http://codingdojang.com/scode/529?answer=20244#answer_20244
'''

b = list(map(int,' '.join(str(int(input('숫자를 입력하세요.')))).split()))
answer = [str(b[0])]

for i in range(len(b)-1):
  if b[i] % 2 == 0 and b[i+1] % 2 == 0:
    answer.append('*')
  elif b[i] % 2 == 1 and b[i+1] % 2 == 1:
    answer.append('-')
  answer.append(str(b[i+1])) 

print(''.join(answer))
