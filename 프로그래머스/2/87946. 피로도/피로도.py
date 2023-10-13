from itertools import permutations
def solution(k, dungeons):
    answer = 0
    dungeons_list = list(permutations(dungeons,len(dungeons)))
    for dungeon in dungeons_list:
        max_dungeons = 0
        current_fatigue = k
        for min_fatigue, consume_fatigue in dungeon:
            if current_fatigue >= min_fatigue:
                current_fatigue -= consume_fatigue
                max_dungeons += 1
        answer = max(answer, max_dungeons)
    return answer