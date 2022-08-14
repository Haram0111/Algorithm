N = int(input())
num = list(map(int,input().split(" ")))
for i in range(N):
    lst = []
    for j in range(i,N):
        if num[j] > num[i]:
            lst.append(num[j])
    if len(lst) == 0:
        print("-1",end=" ")
    else:
        print(lst[0],end=" ")