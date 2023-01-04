def solution(s):
    answer = []
    alpa = []
    number = []
    for i in range(len(s)):
        if s[i] not in alpa:
            answer.append(-1)
            alpa.append(s[i])
            for j in range(len(number)):
                number[j] = number[j] + 1
            number.append(1)
        else:
            answer.append(number[alpa.index(s[i])])
            for j in range(len(number)):
                number[j] = number[j] + 1
            number[alpa.index(s[i])] = 1
    return answer