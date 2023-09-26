from collections import deque

def adjacent_node(x,y):
    adjacent = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0<= nx < n and 0<= ny < m:
            adjacent.append((nx,ny))
    return adjacent

n, m = map(int, input().split())

maps = []
for i in range(n):
    line = list(map(int, input()))
    maps.append(line)

visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0,0,1))
visited[0][0] = True

while q:
    x, y, depth = q.popleft()
    
    if x == n-1 and y == m-1:
        print(depth)
        break
        
    adjacent = adjacent_node(x,y)
    
    for i, j in adjacent:
        if not visited[i][j] and maps[i][j] == 1:
            visited[i][j] = True
            q.append((i, j, depth + 1))