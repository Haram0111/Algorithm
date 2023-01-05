def solution(s):
    pre = s[0]
    answer = 0
    same = 1
    diff = 0
    for i in range(1,len(s)-1):
        if s[i] == pre:
            same += 1
        else:
            diff += 1
            if diff == same:
                answer += 1
                pre = s[i+1]
    return answer + 1