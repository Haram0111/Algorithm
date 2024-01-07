N, M = map(int,input().split(" "))

# 그리디
cnt = 1
while True:
    if M == N:
        break
    elif M < N:
        cnt = -1
        break
    if M % 2 == 0:
        M = M // 2
        cnt += 1
    elif str(M)[-1] == '1':
        M = int(str(M)[:-1])
        cnt += 1
    else:
        cnt = -1
        break
print(cnt)