#순위검색
def solution(info, query):
    answer = []
    for i in range(len(info)): #정보 리스트로 만들기
        info[i] = info[i].split(" ")
    for i in range(len(query)): #query 리스트로 만들기 (조건)
        #print("********************")
        condition = []
        result = 0
        query[i] = query[i].split(" and ")
        a, b = query[i][3].split(" ")[0], query[i][3].split(" ")[1]
        query[i] = query[i][:3]
        query[i].append(a)
        query[i].append(b)
        #print(query[i])
        #print(query[i][4], info[i][4])
        for j in range(len(info)):
           # print("--------------")
            cnt = 0
            for person, detail in zip(info[j][:4], query[i][:4]):
                #print(person, detail)
                if detail == "-":
                    cnt += 1
                    #print("패스")
                elif person == detail:
                    cnt += 1
                    #print("일치")
            if int(info[j][4]) >= int(query[i][4]):
                cnt += 1
                #print("통과")
            if cnt == 5:
                result += 1
                #print(info[j],query[i])
        answer.append(result)
    return answer