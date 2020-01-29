'''
date: 19/12/20

철이는 아스키코드에 대해 공부하고있었습니다.
하지만 기억력이 좋지않아 순서를 잊어먹게되는탓에 프로그램을 하나 만들어두려합니다.
문자를 입력받으면 그 문자에 해당하는 아스키코드를 출력하는 코드를 작성해주세요.

http://codingdojang.com/scode/595?answer=20262#answer_20262
'''

text = list(input('문자를 입력하세요: '))
for i in text:
  print('{}는 아스키코드로 {}입니다.'.format(i, ord(i), end=' '))
