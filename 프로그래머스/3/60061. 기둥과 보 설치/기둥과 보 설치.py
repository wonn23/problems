# 구조물을 모두 설치하고 조건을 따지며 제거한다.
# 구조물 설치하면서 조건을 따진다. -> 이것이 정답. 더 효율적이다. 구현의 복잡성은 극복해야하는 것이다.
# 일단 제거하는 것은 무시하고 설치하는 것만 생각해보자
def check_valid(structures):
    for x, y, a in structures:
        if a == 0:  # 기둥
            if y == 0 or (x, y-1, 0) in structures or (x-1, y, 1) in structures or (x, y, 1) in structures:
                continue
            else:
                return False
        elif a == 1:  # 보
            if (x, y-1, 0) in structures or (x+1, y-1, 0) in structures or ((x-1, y, 1) in structures and (x+1, y, 1) in structures):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    structures = set()
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            structures.add((x, y, a))
            if not check_valid(structures):
                structures.remove((x, y, a))
        else:  # 삭제
            structures.remove((x, y, a))
            if not check_valid(structures):
                structures.add((x, y, a))
                
    answer = map(list, structures)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))