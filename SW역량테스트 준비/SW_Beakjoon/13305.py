N = int(input())
far = list(map(int,input().split(" ")))
price = list(map(int,input().split(" ")))

answer = 0
mini = price[0]
for i in range(len(far)):
    if price[i] < mini:
        answer += price[i] * far[i]
        mini = price[i]
    else:
        answer += mini * far[i]
print(answer)