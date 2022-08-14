N = int(input())
N_lst = list(map(int,input().split(" ")))
N_lst.sort()
M = int(input())
M_lst = list(map(int,input().split(" ")))
M_lst.sort()
result = [0] * len(N_lst)
print(N_lst)
print(M_lst)
for i in range(len(N_lst)):
    start = 0
    end = len(M_lst)-1
    while start >= end:
        mid = (start + end) // 2
        if M_lst[mid] > N_lst[i]:
            end = end - 1
        elif M_lst[mid] < N_lst[i]:
            start = start + 1
        elif M_lst[mid] == N_lst[i]:
            start += 1
            result[i] = 1
print(result)