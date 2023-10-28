def solution(m, n, puddles):
    puddles = [[x,y] for y,x in puddles] # puddles의 x,y 좌표 위치 바꿔주기
    
    map = [[0]*(m+1) for _ in range(n+1)]
    map[1][1] = 1
    for x in range(1,n+1):
        for y in range(1,m+1):
            if x==1 and y==1:
                continue
            if [x,y] in puddles:
                map[x][y] = 0
            else:
                map[x][y] = (map[x][y-1] + map[x-1][y])% 1000000007
    return map[n][m]