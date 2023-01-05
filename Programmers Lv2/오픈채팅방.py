def solution(record):
    dic = {}
    outdata = []
    answer = []
    for i in record:
        inputdata = i.split()
        if inputdata[0] == 'Enter':
            dic[inputdata[1]] = inputdata[2]
            outdata.append([inputdata[1], "in"])
        elif inputdata[0] == 'Leave':
            outdata.append([inputdata[1], "out"])
        elif inputdata[0] == 'Change':
            dic[inputdata[1]] = inputdata[2]
    #출력을 맨 마지막에 받아야함
    for i in outdata:
        if i[1] == "in":
            answer.append(f"{dic[i[0]]}님이 들어왔습니다.")
        elif i[1] == "out":
            answer.append(f"{dic[i[0]]}님이 나갔습니다.")
    return answer