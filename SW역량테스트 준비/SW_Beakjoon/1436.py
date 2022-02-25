N = int(input())
start = 666
cnt = 0
while True:
    start = str(start)
    if "666" in start:
        cnt += 1
    if cnt == N:
        print(start)
        break
    start = int(start)
    start += 1