import sys
from collections import deque


def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1, node + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, node + 1):
            if not visited[i] and graph[v][i] == 1:
                q.append(i)
                visited[i] = True


node, edge, start = map(int, input().split())

graph = [[0] * (node + 1) for _ in range(node + 1)]

for i in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False] * (node + 1)
dfs(graph, start, visited)
print()

visited = [False] * (node + 1)
bfs(graph, start, visited)
