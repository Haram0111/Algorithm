import math

def solution(n,a,b):
    answer = 1
    while 1:
        if math.ceil(a/2) == math.ceil(b/2):
            break
        else:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
            answer += 1
    return answer