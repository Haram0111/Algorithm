def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        for j in range(len(i)):
            if (j+1) % 2 == 1:
                a = i[j].upper()
                answer += a
            else:
                a = i[j].lower()
                answer += a
        answer += ' '
    return answer[:-1]