from collections import deque
import sys

input = sys.stdin.read

# 입력 처리
data = input().split()
idx = 0
n = int(data[idx])
m = int(data[idx + 1])
k = int(data[idx + 2])
x = int(data[idx + 3])
idx += 4

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a = int(data[idx])
    b = int(data[idx + 1])
    idx += 2
    graph[a].append(b)

# 거리배열 초기화
distance = [float("inf")] * (n + 1)
distance[x] = 0

# BFS 초기화
q = deque([x])

while q:
    current = q.popleft()

    for neighbor in graph[current]:
        if distance[neighbor] == float("inf"):
            distance[neighbor] = distance[current] + 1
            q.append(neighbor)

# 결과 출력
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
