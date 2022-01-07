def solution(a, b):
    sum = 0
    day = ["SUN","MON","TUE","WEN","THU","FRI","SAT"]
    monthday = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        sum += monthday[i]
    sum = (sum+b-1) % 7
    return day[sum-2]
#왜 틀렸는지 모르겠음