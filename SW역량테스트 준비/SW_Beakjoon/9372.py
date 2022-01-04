def dfs(start):
    global cnt
    visited[start] = 1 #현재 내가 있는 곳을 1로 바꾸겠다.
    for i in airport[start]: #내가 연결되어 있는 곳을 찾는거임
        go_lst = []
        if visited[i]==0: #어디로 가는지 정하는건데 0으로 가는거임 근데 이렇게 되면 횟수가 많아질 수 있음
            go_lst.append(i)
            direct = []
            for j in range(len(go_lst)):
                direct.append(len(airport[j]))           
            dfs(min(direct))
            cnt +=1

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    airport = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int,input().split())
        airport[a].append(b)
        airport[b].append(a)
    print(airport)

cnt = 0
visited = [0]*(N+1)

starting = len(airport[1])
for i in range(1,M):
    if i < starting:
        starting = i

dfs(starting)
print(cnt)

#미해결