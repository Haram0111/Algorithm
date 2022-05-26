def solution(dart):
    sum = [0,0,0]
    lst = []
    option_lst = ['','','']
    num = ["0","1","2","3","4","5","6","7","8","9","10"]
    bonus = ["S","D","T"]
    option = ["*","#"]
    start = 0
    for i in range(len(dart)-1):
        if (dart[i] in bonus or dart[i] in option) and dart[i+1] in num:
            lst.append(dart[start:i+1])
            start = i+1
    lst.append(dart[start:])
    for i in range(len(lst)):
        if "S" in lst[i]:
            lst[i] = lst[i].split("S")
            sum[i] += int(lst[i][0])
            if lst[i][1] == "#":
                option_lst[i] += "#"
            elif lst[i][1] == "*":
                option_lst[i] += "*"
                if i > 0:
                    option_lst[i-1] += "*"
        elif "D" in lst[i]:
            lst[i] = lst[i].split("D")
            sum[i] += pow(int(lst[i][0]),2)
            if lst[i][1] == "#":
                option_lst[i] += "#"
            elif lst[i][1] == "*":
                option_lst[i] += "*"
                if i > 0:
                    option_lst[i-1] += "*"
        elif "T" in lst[i]:
            lst[i] = lst[i].split("T")
            sum[i] += pow(int(lst[i][0]),3)
            if lst[i][1] == "#":
                option_lst[i] += "#"
            elif lst[i][1] == "*":
                option_lst[i] += "*"
                if i > 0:
                    option_lst[i-1] += "*"
    for i in range(3):
        if option_lst[i] == "*":
            sum[i] = sum[i] * 2
        elif option_lst[i] == "#":
            sum[i] = sum[i] * -1
        elif option_lst[i] == "**":
            sum[i] = sum[i] * 4
        elif option_lst[i] == "*#" or option_lst[i] == "#*":
            sum[i] = sum[i] * (-2)
    return sum[0] + sum[1] + sum[2]
        
        #3번만 기회를 준다는게 3개의 데이터를 만들라는 의미이외에 다른 의미가 있는지 모르겠음
        #그냥 하나씩 다 끊기로 했음.
        #if 문으로 숫자를 골라야 되는데 이것도 그냥 list만들어서 바꾸자.
        #만약 이 안에 있다면 int()로 바꾸고 또 if 걸어서 1면 뒤에것도 확인하는거임
        #이렇게 하면 10도 확인가능
        #문제는 점수를 계산하는 방법이 조금 까다롭다는 건데 1 2 3으로 나눠서