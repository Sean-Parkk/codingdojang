'''
date: 19/12/28

파이썬과 같은 몇몇 프로그래밍 언어는 Pothole_case 를 더 선호하는 언어라고 합니다.

Example:

codingDojang --> coding_dojang

numGoat30 --> num_goat_3_0

위 보기와 같이 CameleCase를 Pothole_case 로 바꾸는 함수를 만들어요!

http://codingdojang.com/scode/484?answer=20383#answer_20383
'''

def Pothole_case(a):
  b = a[1:]
  result = ''
  for x in str(b):
    if x == x.upper(): result += '_' + x.lower()
    elif x.isdigit(): result += '_' + x
    else: result += x
  return a[0] + result

print(Pothole_case('codingDojang'))    # coding_dojang
print(Pothole_case('CodingDojang'))    # coding_dojang
print(Pothole_case('numGoat30'))    # num_goat_3_0
print(Pothole_case('123numGoat30'))    # 1_2_3num_goat_3_0
