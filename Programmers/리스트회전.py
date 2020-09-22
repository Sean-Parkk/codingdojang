'''
date: 20/01/06

a = input('숫자와 문자열을 입력하시오: ')
result = a.split()
num = int(result.pop(0))
result = result[-num:] + result[:-num]

http://codingdojang.com/scode/400?answer=20480#answer_20480
'''

a = input('숫자와 문자열을 입력하시오: ')
result = a.split()
num = int(result.pop(0))
result = result[-num:] + result[:-num]
