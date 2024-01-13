from collections import deque

def bfs(board, a, b):
    n = len(board)
    queue = deque()
    cnt = 1
    queue.append((a,b))
    board[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x <= n-1 and 0 <= next_y <= n-1:
                if board[next_x][next_y] == 1:
                    board[next_x][next_y] = 0
                    queue.append([next_x, next_y])
                    cnt += 1
    return cnt
        
N = int(input())
board = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

answer = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            answer.append(bfs(board, i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)