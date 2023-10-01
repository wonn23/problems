from collections import deque

def adjacent_nodes(x, y, field):
    adjacent = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and field[nx][ny] == 1:
            adjacent.append((nx, ny))
    return adjacent

def dfs(x, y, field, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        current_x, current_y = q.popleft()
        for a, b in adjacent_nodes(current_x, current_y, field):
            if not visited[a][b]:
                visited[a][b] = True
                q.append((a, b))

def solution(n, m, field, visited):
    networks = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                dfs(i, j, field, visited)
                networks += 1
    return networks

def main():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        field = [[0] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            field[x][y] = 1

        result = solution(n, m, field, visited)
        print(result)

if __name__ == "__main__":
    main()
