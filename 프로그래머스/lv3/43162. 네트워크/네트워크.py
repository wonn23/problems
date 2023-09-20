def solution(n, computers):
    def dfs(x):  # Modified to only accept x as parameter
        stack = []
        stack.append(x)
        while stack:
            node = stack.pop()
            for y in range(n):
                if computers[node][y] == 1 and visited[y] == False:
                    visited[y] = True
                    stack.append(y)

    visited = [False for _ in range(n)]
    network = 0
    for i in range(n):
        if visited[i] == False:
            network += 1
            visited[i] = True
            dfs(i)
    return network