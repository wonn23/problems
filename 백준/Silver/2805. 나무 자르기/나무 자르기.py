def binary(start, end, heights):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        sum_h = 0
        for h in heights:
            if h - mid > 0:
                sum_h += h - mid
        if sum_h >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


n, m = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()
print(binary(0, heights[-1], heights))
