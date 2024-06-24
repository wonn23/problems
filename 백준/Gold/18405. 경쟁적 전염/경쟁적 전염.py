import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

lab = []
viruses = []
for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(n):
        if row[j] != 0:
            viruses.append((lab[i][j], i, j))

s, x, y = map(int, input().split())

viruses.sort()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque(viruses)

time = 0
while q:
    if time == s:
        break
    for _ in range(len(q)):
        virus, i, j = q.popleft()
        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] == 0:
                lab[nx][ny] = virus
                q.append((virus, nx, ny))
    time += 1
print(lab[x - 1][y - 1])