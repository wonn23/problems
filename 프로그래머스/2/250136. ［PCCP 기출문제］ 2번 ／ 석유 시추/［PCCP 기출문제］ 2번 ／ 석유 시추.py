from collections import deque

def bfs(land, x, y, visited, cluster_id):
    n, m = len(land), len(land[0])
    queue = deque([(x, y)])
    visited[x][y] = cluster_id
    size = 0  # 현재 덩어리의 크기
    columns = set()  # 현재 덩어리가 포함된 열의 집합

    while queue:
        cx, cy = queue.popleft()
        size += 1
        columns.add(cy)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = cluster_id
                queue.append((nx, ny))

    return size, columns

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[-1]*m for _ in range(n)]  # 방문한 노드와 덩어리 ID 저장
    cluster_info = {}  # 덩어리 ID를 key로, (크기, 포함된 열의 집합)을 value로 가지는 딕셔너리

    cluster_id = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == -1:
                size, columns = bfs(land, i, j, visited, cluster_id)
                cluster_info[cluster_id] = (size, columns)
                cluster_id += 1

    # 각 열별로 석유량 계산
    column_oil = [0]*m
    for cluster_id, (size, columns) in cluster_info.items():
        for column in columns:
            column_oil[column] += size

    return max(column_oil)