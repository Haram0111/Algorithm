N, K = map(int,input().split(" "))

answer = 0
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)

for i in range(len(lst)):
    answer += K // lst[-i-1]
    K = K % lst[-i-1]
    if K == 0:
        break
print(answer)