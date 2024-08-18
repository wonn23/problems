from collections import deque

n,l,r = map(int,input().split())

country = []
for i in range(n):
    country.append(list(map(int,input().split())))
    
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([(x,y)])
    union = [(x,y)]
    visited[x][y] = True
    total_population = country[x][y]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[x][y]-country[nx][ny]) <= r:
                    q.append((nx,ny))
                    union.append((nx,ny))
                    visited[nx][ny] = True
                    total_population += country[nx][ny]
    
    moved_population = total_population // len(union)
    for i, j in union:
        country[i][j] = moved_population
    return len(union) > 1

moves = 0
while True:
    is_moved = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    is_moved = True
    if is_moved:
        moves += 1
    else:
        print(moves)
        break
    