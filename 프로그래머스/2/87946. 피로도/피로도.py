from itertools import permutations
def solution(k, dungeons):
    perm_dungeons = list(permutations(dungeons,len(dungeons)))
    
    answer = 0
    for dungeon in perm_dungeons:
        count = 0
        current_f = k
        for min_f, consume_f in dungeon:
            if current_f >= min_f:
                current_f -= consume_f
                count += 1
        answer = max(answer, count)
        
    return answer