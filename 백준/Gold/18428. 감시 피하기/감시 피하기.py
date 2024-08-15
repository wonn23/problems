import sys
from itertools import combinations

n = int(input())

school = []
for i in range(n):
    school.append(list(input().split()))

# 빈공간, 선생님 좌표 빼내기
empty_spaces = []
teachers = []
for i in range(n):
    for j in range(n):
        if school[i][j] == 'T':
            teachers.append((i,j))
        elif school[i][j] == 'X':
            empty_spaces.append((i,j))

            
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
                  
def can_see_student(x,y,direction):
    while True:
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        if school[x][y] == 'O':
            return False
        if school[x][y] == 'S':
            return True
        
def is_safe():
    for x, y in teachers:
        for d in range(4):
            if can_see_student(x,y,d):
                return False
    return True

# 장애물 설치
found = False
for walls in combinations(empty_spaces,3):
    for wx, wy in walls:
        school[wx][wy] = 'O'
    
    if is_safe():
        found = True
        break
    
    for wx, wy in walls:
        school[wx][wy] = 'X'
        
if found:
    print('YES')
else:
    print('NO')