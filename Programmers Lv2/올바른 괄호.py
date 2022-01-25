def solution(s):
    r_cnt = 0
    l_cnt = 0
    answer = True
    for i in s:
        if s[0] == ')' or s[len(s)-1] == '(':
            answer = False
            break
        if i == '(':
            l_cnt += 1
        elif i == ')':
            r_cnt += 1
        if l_cnt < r_cnt:
            answer = False
    if r_cnt != l_cnt:
        answer = False
    return answer