def solution(n):
    answer = 0
    for i in range(n):
        start = i + 1
        number = start
        sum = 0
        while True:
            sum += number
            number += 1
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer