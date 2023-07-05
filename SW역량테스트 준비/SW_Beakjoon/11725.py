import sys
sys.setrecursionlimit(10**6)

def DFS(graph, start, visited, root):
    visited[start] = root
    root = start
    for i in graph[start]:
        if visited[i] == 0:
            DFS(graph, i, visited, start)

N = int(input())
graph = [ [] for i in range(N+1) ]
visited = [0] * (N+1)
for i in range(N-1):
    start, end = map(int,input().split(" "))
    graph[start].append(end)
    graph[end].append(start)
DFS(graph, 1, visited, 0)
for i in visited[2:]:
    print(i)
