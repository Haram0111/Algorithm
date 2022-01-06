def solution(n):
    a = []
    answer = list(str(n))
    for i in range(len(answer)):
        a.append(int(answer[len(answer)-i-1]))
    return a