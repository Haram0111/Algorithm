def solution(progresses, speeds):
    finsh = [[False] for i in range(len(progresses))]
    start = 0
    suc = []
    while (True):
        cnt = 0
        for i in range(len(speeds)): #매일 speeds값 더해주기
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                progresses[i] = 100
                finsh[i] = True
        for j in range(start,len(finsh)): #start값 부터 차례대로 확인하기
            if finsh[j] == True:
                start += 1
                cnt += 1
            else:
                break
        if cnt != 0:
            suc.append(cnt)
        if sum(suc) == len(progresses):
            break
    return suc