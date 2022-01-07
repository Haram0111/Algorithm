def solution(n):
    lst = list(range(n+1))
    answer = 0
    for l in lst:
        div_cnt = 0
        for m in range(1,l+1):
            if l % m == 0:
                div_cnt += 1
        if div_cnt == 2: 
            answer += 1
    return answer
#미해결