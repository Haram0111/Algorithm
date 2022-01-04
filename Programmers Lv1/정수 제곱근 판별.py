def solution(n):
    answer = 0
    num = int(n**(1/2))
    if n - num*num == 0:
        answer = (num+1)*(num+1)
    else:
        answer = -1
    return answer