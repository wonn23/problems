from collections import deque

def adjacent_node(x,y,N,M):
    adjacent = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]: # 상하좌우
        nx, ny = x + dx, y + dy
        if 0<= nx < N and 0<= ny < M:
            adjacent.append((nx,ny))
    return adjacent
    
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    visited = [[False for _ in range(M)] for _ in range(N)]

    x,y,answer = 0,0,1
    q = deque()
    q.append((x, y, answer))
    visited[0][0] = True
    
    while q:
        x, y, answer = q.popleft()
        
        if x == N-1 and y == M-1:
            return answer
        adjacent = adjacent_node(x,y,N,M)
        for i, j in adjacent:
            if not visited[i][j] and maps[i][j] == 1:
                visited[i][j] = True
                q.append((i,j,answer+1))
    
    return -1