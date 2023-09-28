def adjacent_node(x, y):
    adjacent = []
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            adjacent.append((nx, ny))
    return adjacent


def dfs(i, j, visited):
    count = 1
    visited[i][j] = True
    stack = []
    stack.append((i, j))
    while stack:
        x, y = stack.pop()
        adjacent = adjacent_node(x, y)
        for x, y in adjacent:
            if not visited[x][y] and maps[x][y] == 1:
                visited[x][y] = True
                count += 1
                stack.append((x, y))
    return count


N = int(input())

maps = []
for i in range(N):
    maps.append(list(map(int, input())))

visited = [[False for _ in range(N)] for _ in range(N)]

network = 0
house = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j] == 1:
            network += 1
            house.append(dfs(i, j, visited))


print(network)
house = sorted(house)
for i in house:
    print(i)
