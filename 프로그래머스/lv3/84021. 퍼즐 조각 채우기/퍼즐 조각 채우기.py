import copy


def solution(game_board, table):
    n = len(game_board)
    answer = 0
    blank = []
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blank.append(dfs(game_board, i, j, [0, 0], n, 0)) # 1. game_board의 빈칸 좌표를 구해서 (0,0)을 기준으로 옮기기

    for k in range(4): # 6. 2~5번 과정을 4번 반복한다.
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copy_table[i][j] == 1:
                    block = dfs(copy_table, i, j, [0, 0], n, 1) # 2. table의 블록 좌표를 구해서 (0,0)을 기준으로 옮기기
                    if block in blank:
                        blank.remove(block)                     # 3. 빈칸과 block 좌표가 일치하면 빈칸 리스트에서 제거 해준다.
                        answer += len(block)                    # 3. 지운 칸 수 만큼 answer에 더해준다.
                        table = copy.deepcopy(copy_table)       # 4. 해당 block 좌표는 더이상 사용하면 안되므로 table을 업데이트 시켜준다.
                    else:
                        copy_table = copy.deepcopy(table)       # 5. 만약 일치하지 않는다면 table을 원해 상태로 돌려 놓는다.
    return answer


def dfs(board, x, y, position, n, num): # board: game_board or table
    dx = [-1, 0, 1, 0]                  # x,y: 시작 좌표
    dy = [0, 1, 0, -1]                  # position: 인접한 노드를 탐색하는 현재 위치. (0,0)부터 시작
                                        # n: 정사각형 한 변의 길이
    result = [position]                 # num: game_board일 땐 0, table일 땐 1

    board[x][y] = 2                     # 방문처리를 2로 하는 이유는 0,1은 퍼즐의 위치를 찾을 때 사용하기 때문이다.

    for i in range(4):
        px = x + dx[i] # px, py는 단순히 보드판을 넘어가는지만 확인하는 용도로 사용
        py = y + dy[i]

        if 0 <= px and px < n and 0 <= py and py < n:
            if board[px][py] == num:
                result += dfs(
                    board, px, py, [position[0] + dx[i], position[1] + dy[i]], n, num
                )

    return result


# 90도 회전
def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = table[i][j]

    return rotated
