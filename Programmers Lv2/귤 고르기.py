def solution(k, tangerine):
    dic = {}
    answer = 0
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    sum = 0
    for i in dic:
        if k <= sum + i[1]:
            return answer + 1
        else:
            sum += i[1]
            answer += 1