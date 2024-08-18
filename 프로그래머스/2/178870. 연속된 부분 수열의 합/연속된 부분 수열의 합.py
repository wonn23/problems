def solution(sequence, k):
    # 결과를 저장할 리스트: [시작 인덱스, 끝 인덱스]
    result = []
    # 윈도우의 시작과 끝 인덱스
    start = 0
    # 현재 합계를 저장할 변수
    current_sum = 0
    # 최소 길이를 저장할 변수 (초기에는 매우 큰 값으로 설정)
    min_length = float('inf')

    # 슬라이딩 윈도우의 끝 인덱스를 반복
    for end in range(len(sequence)):
        # 현재 끝 인덱스의 값을 윈도우 합에 추가
        current_sum += sequence[end]

        # 윈도우의 합이 목표값을 넘지 않을 때까지 시작점을 이동
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        # 윈도우의 합이 목표값과 같다면 결과를 업데이트
        if current_sum == k:
            current_window_length = end - start + 1
            if current_window_length < min_length:
                min_length = current_window_length
                result = [start, end]

    return result