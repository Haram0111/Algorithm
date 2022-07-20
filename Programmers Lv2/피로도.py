import itertools

def solution(k, dungeons):
    nPr = list(itertools.permutations(dungeons, len(dungeons)))
    fix = k
    cnt = 0
    for i in range(len(nPr)):
        k = fix
        result = 0
        # print(nPr[i])
        for j in range(len(nPr[i])):           
            # print(type(nPr[i][j][0]))
            # print(nPr[i][j])
            if k >= nPr[i][j][0]:
                k -= nPr[i][j][1]
                result += 1
                cnt = max(cnt, result)
            else: 
                cnt = max(cnt, result)                
    return cnt