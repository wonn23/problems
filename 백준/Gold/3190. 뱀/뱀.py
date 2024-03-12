N = int(input())
K = int(input())
apples = []
for i in range(K):
    a, b = map(int, input().split())
    apples.append((a, b))
L = int(input())
directions = [input().split() for _ in range(L)]
directions = [(int(x), c) for x, c in directions]

# 뱀의 초기 위치 및 방향 설정 (오른쪽을 바라보고 있음)
snake = [(1, 1)]
dx, dy = 0, 1  # 초기 이동 방향
time = 0  # 게임이 진행된 시간
direction_idx = 0  # 다음에 적용할 방향 변환의 인덱스


# 방향 전환 함수
def turn(direction, C):
    if C == "L":
        return -direction[1], direction[0]
    else:
        return direction[1], -direction[0]


# 게임 시작
while True:
    time += 1
    # 뱀의 머리 위치 갱신
    head = (snake[0][0] + dx, snake[0][1] + dy)
    # 벽 또는 자기 자신과 부딪히면 게임 종료
    if head in snake or not (1 <= head[0] <= N) or not (1 <= head[1] <= N):
        break
    snake.insert(0, head)
    # 사과가 있으면 꼬리를 움직이지 않음
    if head not in apples:
        snake.pop()
    else:  # 사과를 먹으면 사과 목록에서 제거
        apples.remove(head)
    # 방향 전환 시간이 되면 방향 전환
    if direction_idx < L and time == directions[direction_idx][0]:
        dx, dy = turn((dx, dy), directions[direction_idx][1])
        direction_idx += 1

print(time)
