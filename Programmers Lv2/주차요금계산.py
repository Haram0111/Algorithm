import math

def Time(time1, time2):
    time1 = time1.split(":")
    time2 = time2.split(":")
    min1 = int(time1[0]) * 60 + int(time1[1])
    min2 = int(time2[0]) * 60 + int(time2[1])
    result = int(min2) - int(min1)
    return result

def solution(fees, records):
    answer =[] 
    dic = {} #자동차별 정보넣을 곳
    for i in range(len(records)):
        temp = records[i].split(" ")
        if temp[1] not in dic: #차번호가 dic에 없으면
            dic[temp[1]] = [temp[0], 0, True] #dic에 넣어주고 이제 들어왔으니까 0으로 해준다잉
        elif temp[1] in dic and dic[temp[1]][2] == True: #dic에 들어있고 주차되어 있는 상태라면
            dic[temp[1]][2] = False #차가 나갔다고 해준다
            dic[temp[1]][1] += Time(dic[temp[1]][0], temp[0])#시간
        elif temp[1] in dic and dic[temp[1]][2] == False: #dic에 들어있고 아까 나간상태라면
            dic[temp[1]][2] = True #다시 들어와줬다고 체크해주고
            dic[temp[1]][0] = temp[0] #시간을 바궈준다
    #출차 안한 차량 시간 구하기
    for i in dic:
        if dic[i][2] == True:
            dic[i][1] += Time(dic[i][0], "23:59") #시간
            dic[i][2] = False
    #차량번호 오름차순으로 정렬
    dic = sorted(dic.items())
    #요금 계산
    for i in range(len(dic)):
        if dic[i][1][1] <= fees[0]: #기본 시간보다 사용안했다면 기본요금
            answer.append(fees[1])
        else: #더 사용했다면 요금계산
            answer.append(fees[1] + math.ceil((dic[i][1][1]-fees[0])/fees[2])*fees[3])
    return answer