def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            break
        elif num % 2 == 0:
            num = num / 2
            answer += 1
        else:
            num = num * 3 +1
            answer += 1
    if num != 1:
        return -1
    return answer