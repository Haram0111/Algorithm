def solution(elements):
    lst = []
    for i in range(len(elements)): #7 9 1 1 4
        pre = elements[i]
        for j in range(i+1,i+len(elements)):
            if j >= len(elements):
                j -= len(elements)
            pre += elements[j]
    lst.append(sum(elements))
    return len(set(lst))