'''
date: 19/12/30

타노스는 프로그램의 균형을 위해서는 리스트의 원소 절반을 무작위로 삭제해야 한다고 믿고 있다.
타노스가 손가락을 튕겼을 때(프로그램을 실행했을 때) 입력된 리스트에서 절반의 원소를 무작위로 삭제하여 리턴하는 인피니티 건틀렛 프로그램을 작성하시오.
(무작위 삭제이므로 입력값이 같아도 출력값이 매번 달라야 합니다)

http://codingdojang.com/scode/592?answer=20406#answer_20406
'''

import random

def thanos(x):
  x = random.sample(x,int((len(x)+random.randint(0,1))/2))
  return x

thanos(['캡틴', '토니', '토르'])    # 절반 확률로 1개 또는 2개 원소 삭제
thanos(['블랙위도우', '캡틴마블', '스파이더맨', '블랙팬서'])    # 2개 원소 삭제
