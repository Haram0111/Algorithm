def solution(storey):
    answer = 0
    storey = str(storey)
    lst = []
    for i in range(len(storey)):
        lst.append(int(storey[i]))
    for i in range(len(lst)-1,0,-1):
        if lst[i] > 5:
            answer += 10 - lst[i]
            lst[i-1] += 1
        elif lst[i] == 5 and lst[i-1] >= 5:
            answer += 10 - lst[i]
            lst[i-1] += 1
        elif lst[i] == 5 and lst[i-1] < 5:
            answer += lst[i]
        elif lst[i] < 5:
            answer += lst[i]
    if lst[0] > 5:
        answer += 11 - lst[0]
    else:
        answer += lst[0]
    return answer
#95 > 6