def time_to_min(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

Join = []
answer = 0

setTime = list(input().split())
startTime = time_to_min(setTime[0])
endStartTime = time_to_min(setTime[1])
endEndTime = time_to_min(setTime[2])

while True:
        try:
            revice = list(input().split())
            reviceTime = time_to_min(revice[0])
            reviceName = revice[1]
            if reviceTime <= startTime:
                Join.append(reviceName)
            if reviceTime >= endStartTime and reviceTime < endEndTime:
                if reviceName in Join:
                    answer += 1
        except:
            break
print(answer)