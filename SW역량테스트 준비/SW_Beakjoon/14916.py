N = int(input())

cnt = 0

while True:
    if N % 5 == 0: #5로 나눠질 경우
        cnt += N // 5
        break
    else:
        N = N - 2
        cnt += 1
    if N < 0:
        break

if N < 0:
    print(-1)
else:
    print(cnt)