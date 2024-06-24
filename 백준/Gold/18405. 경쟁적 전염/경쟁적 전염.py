import sys
from collections import deque

""" 
  접근 방법은 n * n 배열을 만들고 바이러스가 퍼져나가는 로직을 작성하려고함
  그런데 낮은 수부터 퍼져나가야하는 것을 어떻게 컨트롤 해야하는지 모르겠음.
  이때, 배열 index에 바이러스 번호를 추가함. 1번부터 k번까지의 바이러스 번호를 돌면서 배열을 채움.
  s 초 반복함 -> x,y 배열 데이터를 출력함.
"""

input = sys.stdin.readline

n, k = map(int, input().split())
lab = []
viruses = []
for i in range(n):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(n):
        if row[j] != 0:
            viruses.append((row[j], i, j))

s, x, y = map(int, input().split())


viruses.sort()

q = deque(viruses)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
while q:
    if time == s:
        break
    for _ in range(len(q)):
        virus_type, i, j = q.popleft()
        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and lab[nx][ny] == 0:
                lab[nx][ny] = virus_type
                q.append((virus_type, nx, ny))
    time += 1
print(lab[x - 1][y - 1])
