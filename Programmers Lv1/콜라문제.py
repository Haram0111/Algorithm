def solution(a, b, n):
    cnt = 0
    rest = 0
    while n+rest >= a:
        n += rest
        rest = 0
        cnt += (n // a) * b
        rest += n % a
        n = (n // a) * b
    return cnt