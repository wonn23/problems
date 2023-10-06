def solution(sizes):
    new_sizes = []
    for i in sizes:
        i = sorted(i)
        new_sizes.append(i)
        
    max_w, max_h = 0, 0
    for i,j in new_sizes:
        max_w = max(max_w, i)
        max_h = max(max_h, j)
        
    return max_w*max_h
    
        
    