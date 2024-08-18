def solution(sequence, k):
    # 시작하는 인덱스와 끝나는 인덱스 출력하기
    # k 합을 낼 수 있는 빈 리스트를 만든다.
    # sequence를 처음부터 더하며 k 값과 일치하는지 확인한다.

    total_list = []
    start_index = 0
    min_length = float('inf')
    current_sum = 0

    for s in range(len(sequence)):
        current_sum += sequence[s]
        
        while current_sum > k and start_index <= s:
            current_sum -= sequence[start_index]
            start_index += 1
    
        if current_sum == k:
            if s - start_index < min_length:
                min_length = s - start_index
                total_list = [start_index,s]
    return total_list