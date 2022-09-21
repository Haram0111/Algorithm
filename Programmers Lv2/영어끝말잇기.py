def solution(n, words):
    dic = {}
    start = words[0][0]
    for i in range(len(words)):
        if words[i][0] == start:
            start = words[i][-1]
            if words[i] not in dic:
                dic[words[i]] = True
            elif words[i] in dic:
                return [i%n + 1, i//n + 1]
        else:
            return [i%n + 1, i//n + 1]
    return [0,0]