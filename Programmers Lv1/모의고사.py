def solution(answers):
    answer = []
    sol = [[1,2,3,4,5],      #5개
        [2,1,2,3,2,4,2,5],   #8개
        [3,3,1,1,2,2,4,4,5,5]]  #10개
    dic = {1:0,2:0,3:0}
    for i in range(1,4):  # i = 1,2,3
        cnt = 0
        for j in range(len(answers)): #j = 0~10까지
            if answers[j] == sol[i-1][j%len(sol[i-1])]: #i-1 = 0,1,2
                cnt += 1
        dic[i] = cnt
    for i in range(1,4):
        if dic[i] == dic.get(max(dic, key= dic.get)):
            answer.append(i)
    return answer