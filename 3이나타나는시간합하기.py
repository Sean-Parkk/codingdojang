'''
date: 19/12/18

디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?

http://codingdojang.com/scode/473?answer=20214#answer_20214
'''

result = 0
for hour in range(0,24):
  for minute in range(0,60):
    if '3' in str(hour) + str(minute):
      result +=60
print(result)
