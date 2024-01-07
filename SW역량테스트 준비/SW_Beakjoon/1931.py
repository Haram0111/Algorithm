N = int(input())
timeTable = []

for i in range(N):
    time = list(map(int,input().split(" ")))
    timeTable.append(time)

timeTable.sort(key = lambda x : (x[1],x[0]))

#끝나는 시간에 초점 맞추기
cnt = 1
end_time = timeTable[0][1]
for i in range(1, N):
    if timeTable[i][0] >= end_time:
        cnt += 1
        end_time = timeTable[i][1]

print(cnt)