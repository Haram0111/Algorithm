def solution(a, b):
    sum = 0
    day = ["SUN","MON","TUE","WEN","THU","FRI","SAT"]
    monthday = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        sum += monthday[i]
    sum = (sum+b) % 7
    index = 5 + sum
    if index > 6:
        index -= 7
    return day[index-1]
#왜 틀렸는지 모르겠음