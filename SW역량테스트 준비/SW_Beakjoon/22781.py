N = int(input())
A = list(map(int, input().split(" ")))
answer = [1000000] * N
#print(answer)
answer[0] = 0
for i in range(N):
    for j in range(i):
        #print((j-i) * (1 + abs(A[j]-A[i])))
        cal = max((i-j) * (1 + abs(A[j]-A[i])), answer[j])
        answer[i] = min(answer[i], cal)
    #print(answer)
print(answer[-1])