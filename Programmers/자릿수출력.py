'''
date: 19/12/20

양의 정수만 입력으로 받고 그 수의 자릿수를 출력해보자. ex1) 3 > 1자리수, ex2) 649 > 3자리수 ....

http://codingdojang.com/scode/588?answer=20257#answer_20257
'''

n = input('숫자를 입력하시오: ')
print('{}자리수'.format(len(str(n))))
