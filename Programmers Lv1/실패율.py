def solution(N, stages):
    answer = []
    falis = dict.fromkeys(range(1,N+1))
    for i in range(1,N+1):
        cnt = 0
        pre = 0
        for j in stages:
            if j > i:
                cnt += 1
            elif j == i:
                cnt += 1
                pre += 1
        falis[i] = pre / cnt
    falis = sorted(falis.items(),key=(lambda x: x[1]),reverse=True)
    for key in falis:
        answer.append(key[0])
    return answer
#틀림