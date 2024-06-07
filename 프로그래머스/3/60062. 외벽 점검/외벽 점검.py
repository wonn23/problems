from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # weak 배열을 2배로 늘려서 원형을 일자로 펴줍니다.
    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1
    
    # 각 취약 지점을 시작점으로 설정합니다.
    for start in range(length):
        # 점검원의 순서를 변경하여 모든 경우를 확인합니다.
        for perm in permutations(dist):
            count = 1  # 사용한 점검원 수
            position = weak[start] + perm[count - 1]  # 첫 번째 점검원이 커버할 수 있는 마지막 지점
            
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + perm[count - 1]
            
            answer = min(answer, count)
    
    return answer if answer <= len(dist) else -1

# 테스트 예제
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))  # 출력: 2
