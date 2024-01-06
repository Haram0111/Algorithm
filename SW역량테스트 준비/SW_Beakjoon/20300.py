N = int(input())
loss = list(map(int,input().split(" ")))
loss.sort()
answer = []

for i in range(len(loss) // 2): #5개면 2개, 4개면 2개
    if len(loss) % 2 == 0: #짝수 개라면
        answer.append(loss[i] + loss[len(loss) -1 -i])
    else:
        answer.append(loss[-1])
        loss = loss[:-1]
        answer.append(loss[i] + loss[len(loss) -1 -i])
        
print(max(answer))