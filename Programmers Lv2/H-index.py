def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        print(citations[i], l-i)
        if citations[i] >= l-i:
            return l-i
    return 0