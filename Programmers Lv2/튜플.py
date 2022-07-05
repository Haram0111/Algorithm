def solution(s):
    answer = []
    s = s[1:-1]
    s = s.split('}')
    s.sort(key=len)
    print(s)
    for i in range(1, len(s)):
        for j in range(1, len(s[i])):
            if s[i][j] != ',' and s[i][j] != '{':
                if s[i][j] not in answer:
                    answer.append(s[i][j])
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer
        