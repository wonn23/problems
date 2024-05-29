from itertools import combinations
import sys

input = sys.stdin.read


def calculate_chicken_distanse(homes, chicken_stores):
    total_distance = 0
    for hx, hy in homes:
        min_distance = float("inf")
        for cx, cy in chicken_stores:
            distance = abs(hx - cx) + abs(hy - cy)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance


def main():
    data = input().strip().split()
    n = int(data[0])
    m = int(data[1])

    matrix = []
    index = 2
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(data[index]))
            index += 1
        matrix.append(row)

    homes = []
    chicken_stores = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                homes.append((i + 1, j + 1))
            elif matrix[i][j] == 2:
                chicken_stores.append((i + 1, j + 1))

    min_chicken_distance = float("inf")
    for chicken_comb in combinations(chicken_stores, m):
        chicken_distance = calculate_chicken_distanse(homes, chicken_comb)
        if chicken_distance < min_chicken_distance:
            min_chicken_distance = chicken_distance

    print(min_chicken_distance)


if __name__ == "__main__":
    main()
