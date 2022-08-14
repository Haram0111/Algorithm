M, N = map(int,input().split(" ")) #M은 세로, N은 가로
chess = []
cnt = 0
for i in range(N):
    chess.append(input())
if chess[0][0] == "W":
    for i in range(M):
        for j in range(N):
            if i % 2 == 0: #짝수일때
                if j % 2 == 0: #짝수번째
                    chess[i][j] != "W"
                    cnt += 1
                    print(i,j)
                else: #홀수 번쨰
                    chess[i][j] != "B"
                    cnt += 1
                    print(i,j)
            else:
                if j % 2 == 0:
                    chess[i][j] != "B"
                    cnt += 1
                    print(i,j)
                else:
                    chess[i][j] != "W"
                    cnt += 1
                    print(i,j)
