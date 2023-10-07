def binary(start, end, budget, total_budget):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum_budget = 0
        for b in budget:
            if mid >= b:
                sum_budget += b
            else:
                sum_budget += mid
        if sum_budget <= total_budget:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


n = int(input())
budget = list(map(int, input().split()))
m = int(input())
budget.sort()
print(binary(0, budget[-1], budget, m))
