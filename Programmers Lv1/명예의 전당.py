def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)):
        lst.append(score[i])
        lst.sort(reverse = True)
        if len(lst) < k:
            answer.append(lst[-1])
        else:
            answer.append(lst[k-1])
    return answer
