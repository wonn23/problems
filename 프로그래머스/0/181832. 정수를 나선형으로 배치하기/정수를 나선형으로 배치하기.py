def solution(n):
    # 나선모양으로 수를 채울 것 (시계방향)
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    dx = [0,1,0,-1] # 오른쪽, 아래, 왼쪽, 위
    dy = [1,0,-1,0]
    
    x,y = 0, 0
    direction = 0
    num = 1
    
    while num <= n*n:
        answer[x][y] = num
        num += 1
        
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]
    
    return answer