def solution(clothes):
    result = {}
    answer = 1
    lst = []
    for i in range(len(clothes)):
        if clothes[i][1] not in result:
            a = []
            a.append(clothes[i][0])
            result[clothes[i][1]] = a
        elif clothes[i][1] in result:
            a = []
            a.append(clothes[i][0])
            result[clothes[i][1]] += a
    for i in result:
        lst.append(len(result[i])+1)
    for i in lst:
        answer *= i
    return answer - 1