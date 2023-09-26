computers = int(input())
edges = int(input())
graph = [[0 for _ in range(computers + 1)] for _ in range(computers + 1)]
for i in range(edges):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False for _ in range(computers + 1)]
count = 0

def dfs(graph, v, visited):
    visited[v] = True
    global count
    for i in range(1, computers + 1):
        if not visited[i] and graph[v][i] == 1:
            count += 1
            dfs(graph, i, visited)

    return count


print(dfs(graph, 1, visited))
