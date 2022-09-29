def solution(n):
    cnt = 0
    while n != 1:
        if n % 2 == 1: #홀수 일 때
            n = n - 1
            cnt += 1
        else: #짝수일 때
            n = n // 2
    return cnt + 1