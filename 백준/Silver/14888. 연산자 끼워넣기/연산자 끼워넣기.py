import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
calcul_list = list(map(int, input().split()))

INF = int(10e9)

# calcul_list를 0,1,2,3으로 나타내기
perm_list = []
for i in range(4):
    # if calcul_list[i] >= 1:
    #     for _ in range(calcul_list[i]):
    #         perm_list.append(i)
    perm_list.extend([i] * calcul_list[i])


def solution(perm):
    result = num_list[0]
    for i in range(1, n):
        if perm[i - 1] == 0:
            result += num_list[i]
        elif perm[i - 1] == 1:
            result -= num_list[i]
        elif perm[i - 1] == 2:
            result *= num_list[i]
        elif perm[i - 1] == 3:
            # 나누는 값이 음수인 경우를 생각해줘야함
            if result < 0 and num_list[i] > 0:
                result = -(-result // num_list[i])
            else:
                result //= num_list[i]
    return result


max_value = -INF
min_value = INF

for perm in set(permutations(perm_list)):
    result = solution(perm)
    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)
