'''
date: 20/02/04

정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''

def solution(n):
    answer = n
    for num in range(1,int(n/2)+1):  # 약수는 그 수의 절반을 넘지 못하므로, 2로 나눈 후 for문 실행
        if n % num == 0:
            answer += num

    return answer
    
