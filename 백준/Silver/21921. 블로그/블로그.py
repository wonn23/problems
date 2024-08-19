import sys

input = sys.stdin.readline

# 입력 받기
n, x = map(int, input().split())
num_list = list(map(int, input().split()))

# 초기 설정
start = 0
current_sum = sum(num_list[:x])  # 첫 번째 윈도우의 합
max_sum = current_sum
count = 1  # 첫 번째 윈도우에서의 최대값

# 슬라이딩 윈도우 적용
for end in range(x, n):
    current_sum += num_list[end] - num_list[start]
    start += 1

    if current_sum > max_sum:
        max_sum = current_sum
        count = 1  # 새로운 최대값이 나오면 카운트 초기화
    elif current_sum == max_sum:
        count += 1  # 최대값이 동일하면 카운트 증가

# 결과 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)