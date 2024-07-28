import sys

input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
num_list = list(map(int, input().strip().split()))
add, sub, mul, div = map(int, input().strip().split())

# 최대값, 최소값 초기화
max_value = -int(1e9)
min_value = int(1e9)

# 백트래킹 함수 정의
def backtrack(index, current_value, add, sub, mul, div):
    global max_value, min_value

    # 모든 숫자를 사용한 경우
    if index == n:
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return

    # 가능한 연산자들을 각각 적용해보기
    if add > 0:
        backtrack(index + 1, current_value + num_list[index], add - 1, sub, mul, div)
    if sub > 0:
        backtrack(index + 1, current_value - num_list[index], add, sub - 1, mul, div)
    if mul > 0:
        backtrack(index + 1, current_value * num_list[index], add, sub, mul - 1, div)
    if div > 0:
        # 나눗셈의 경우 음수 처리를 위해 별도 처리
        if current_value < 0:
            backtrack(index + 1, -(-current_value // num_list[index]), add, sub, mul, div - 1)
        else:
            backtrack(index + 1, current_value // num_list[index], add, sub, mul, div - 1)

# 백트래킹 시작
backtrack(1, num_list[0], add, sub, mul, div)

# 결과 출력
print(max_value)
print(min_value)