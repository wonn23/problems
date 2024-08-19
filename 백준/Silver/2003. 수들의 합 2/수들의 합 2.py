# 슬라이딩 윈도우
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

start = 0
current_sum = 0
count = 0
for end in range(n):
    current_sum += num_list[end]

    while current_sum > m:
        current_sum -= num_list[start]
        start += 1
    if current_sum == m:
        count += 1
print(count)
