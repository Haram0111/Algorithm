K, N = map(int,input().split(" "))
lst = []
for i in range(K):
    lst.append(int(input()))
start = 1
end = max(lst)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in lst:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)