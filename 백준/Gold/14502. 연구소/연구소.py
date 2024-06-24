import sys
from itertools import combinations
from collections import deque
import copy

"""
  벽막기 -> 바이러스 퍼트리기 -> 0개수 세기
"""

input = sys.stdin.readline
n, m = map(int, input().split())

lab = []
virus = []
empty = []

for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            empty.append((i, j))


def spread_virus(lab):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque(virus)

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                q.append((nx, ny))


def count_safe_area(lab):
    count = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                count += 1
    return count


max_safe_area = 0

for walls in combinations(empty, 3):
    new_lab = copy.deepcopy(lab)

    for wx, wy in walls:
        new_lab[wx][wy] = 1

    spread_virus(new_lab)

    safe_area = count_safe_area(new_lab)
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
