def solution(food):
    answer = ''
    lst = []
    for i in range(1, len(food)):
        lst.append(food[i]//2)
    print(lst)
    for i in range(len(lst)):
        answer += str((i+1)) * lst[i]
    answer += '0'
    for j in range(len(lst),0,-1):
        answer += str((j)) * lst[j-1]
    print(answer)
    return answer