'''
date: 19/12/17

주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

김씨와 이씨는 각각 몇 명 인가요?
"이재영"이란 이름이 몇 번 반복되나요?
중복을 제거한 이름을 출력하세요.
중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

http://codingdojang.com/scode/410?answer=20202#answer_20202
'''

# Q1.

member = '이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌'.split(',')

a = [i[0] for i in member]
print('김씨는 {}명 입니다. \n이씨는 {}명 입니다.'.format(a.count('김'), a.count('이')))

# Q2.
print(member.count('이재영'))

# Q3.
unq_member = list(set(member))
print(unq_member)

# Q4.
unq_member.sort()
print(unq_member)
