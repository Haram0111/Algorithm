def solution(n):
    num = str(bin(n))[2:].count('1')
    while True:
        n += 1
        if str(bin(n))[2:].count('1') == num:
            answer = n
            break
    return answer