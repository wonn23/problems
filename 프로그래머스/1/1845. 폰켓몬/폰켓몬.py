def solution(nums):
    result = len(set(nums))
    if result > len(nums)/2:
        return len(nums)/2
    else:
        return result