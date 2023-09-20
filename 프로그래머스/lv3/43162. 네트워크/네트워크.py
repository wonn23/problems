def dfs(computers, visited, i):
    stack = [i]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for j in range(len(computers)):
                if computers[node][j] == 1 and not visited[j]:
                    stack.append(j)

def solution(n, computers):
    network_count = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            network_count += 1

    return network_count
