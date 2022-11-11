def solution(ingredient):
    check = []
    answer = 0
    for i in ingredient:
        check.append(i)
        if len(check) > 3:
            if check[-1] == 1 and check[-2] == 3 and check[-3] == 2 and check[-4] == 1:
                for i in range(4):
                    check.pop()
                answer += 1
    return answer