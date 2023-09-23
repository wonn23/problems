from collections import deque


def solution(maps):
    n = len(maps)  # 행
    m = len(maps[0])  # 열

    # 상하좌우 이동 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for i in range(m)] for j in range(n)]  # 2D로 방문 행렬 초기화

    q = deque()
    x, y, distance = 0, 0, 1  # x,y 위치와 제자리인 것 세줘야해서 1이다
    q.append([x, y, distance])
    visited[x][y] = True

    while q:
        x, y, distance = q.popleft()
        if x == n - 1 and y == m - 1:  # x,y가 도착지점에 도달했는지 먼저 확인
            return distance

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and visited[nx][ny] == False
            ):
                visited[nx][ny] = True
                q.append([nx, ny, distance+1])

    return -1  # while을 모두 빠져나왔다는 것은 도착지점에 도달 못했다는 것을 의미한다