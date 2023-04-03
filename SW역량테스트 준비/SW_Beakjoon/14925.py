M, N = map(int,input().split(" ")) #세로, 가로
lst = []
for i in range(M):
    lst.append(list(map(int,input().split(" "))))
print(lst)
answer = 0
for i in range(M):
    for j in range(N):
        lst[i][j]

#재귀함수를 만들어서 asnwer을 최대로 만들기