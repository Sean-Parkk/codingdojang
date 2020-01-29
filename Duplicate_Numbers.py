'''
date: 19/12/18

0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
sample inputs: 0123456789 01234 01234567890 6789012345 012322456789
sample outputs: true false false true false

http://codingdojang.com/scode/488?answer=20224#answer_20224
'''

a = int(input('숫자를 입력하세요.'))
print(True if len(a) == len(set(a)) == 10 else False)
