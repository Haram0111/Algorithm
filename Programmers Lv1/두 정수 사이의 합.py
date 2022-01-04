def solution(a, b):
    answer = 0
    c = min(a,b)
    for i in range(abs(b-a)+1):
        answer += c
        c += 1
    return answer