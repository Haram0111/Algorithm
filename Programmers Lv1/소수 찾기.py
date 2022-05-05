import math

def solution(n):
    cnt = 0 #소수가 아닌 것을 세는중
    for i in range(2,n+1):
        for j in range(1,int(pow(i,1/2))+1):
            if i % j == 0 and j != 1: #어떤 수로 나누어 떨어졌다라는 증거
                cnt += 1
                break
    return n-cnt-1