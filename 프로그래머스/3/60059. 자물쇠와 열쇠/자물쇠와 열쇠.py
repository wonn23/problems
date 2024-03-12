def rotate_key(key):
    m = len(key)
    rotated = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[j][m-1-i] = key[i][j]
    return rotated

def match(key, lock, start_x, start_y):
    n = len(lock)
    m = len(key)
    extended_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # 자물쇠를 확장된 자물쇠 가운데에 배치
    for i in range(n):
        for j in range(n):
            extended_lock[i + n][j + n] = lock[i][j]
            
    # 열쇠를 이동시키면서 매칭 검사
    for i in range(m):
        for j in range(m):
            extended_lock[start_x + i][start_y + j] += key[i][j]
            
    # 확장된 자물쇠의 가운데 부분이 모두 1인지 검사
    for i in range(n):
        for j in range(n):
            if extended_lock[i + n][j + n] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    for rotation in range(4):  # 4방향 회전
        rotated_key = key
        for _ in range(rotation):
            rotated_key = rotate_key(rotated_key)
        for x in range(n * 2):
            for y in range(n * 2):
                if match(rotated_key, lock, x, y):
                    return True
    return False