def solution(n):
    result = ""
    while n >= 3:
        result += str(n % 3)
        n = n // 3
    result += str(n)
    return int(result,3)