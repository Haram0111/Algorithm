from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph2, v, visited2):
    visited2[v] = True
    print(v, end = ' ')
    for i in graph2[v]:
        if not visited2[i]:
            dfs(graph2, i, visited2)
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

N, M, V = map(int,input().split(" "))
graph = [ [] for i in range(N+1) ]
graph2 = [ [] for i in range(N+1) ]

for i in range(M):
    start, end = map(int,input().split(" "))
    graph[start].append(end)
    graph[start].sort()
    graph[end].append(start)
    graph[end].sort()   
    graph2[start].append(end)
    graph2[start].sort()
    graph2[end].append(start)
    graph2[end].sort()
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (N+1)
visited2 = [False] * (N+1)
# 정의된 BFS 함수 호출
dfs(graph2, V, visited2)
print()
bfs(graph, V, visited)