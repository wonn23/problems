def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for i, j in sizes:
        if i > j:
            w = max(w, i)
        else:
            w = max(w, j)
        if i < j:
            h = max(h, i)
        else:
            h = max(h, j)
    answer = w * h

    return answer
