def dfs(graph, start, visited, result):
    visited[start] = True
    #print(start, end=" ")
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited, result)

N = int(input()) #컴퓨터 개수
M = int(input()) #간선의 개수
graph = [ [] for i in range(N+1) ]
visited = [False] * (N+1)
result = []
for i in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
dfs(graph, 1, visited, result)

print(len(result)-1)