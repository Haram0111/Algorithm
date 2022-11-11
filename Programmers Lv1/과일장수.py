def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(1,len(score)+1):
        if i % m == 0:
            answer += score[i-1] * m
    return answer