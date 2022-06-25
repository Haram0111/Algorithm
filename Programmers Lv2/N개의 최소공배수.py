from math import gcd     
def solution(arr):                    
    answer = arr[0]                                 # answer을 arr[0]으로 초기화
    for num in arr:                                 # 반복문을 처음부터 끝까지 돈다.
        answer = answer*num // gcd(answer, num)     
    return answer