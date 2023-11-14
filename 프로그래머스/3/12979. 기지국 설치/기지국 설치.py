import math

def solution(n, stations, w):
    answer = 0
    width = w*2+1

    # 처음 기지국 설치 전까지의 덩어리 계산
    answer += math.ceil((stations[0] - w - 1) / width)

    # 마지막 기지국 설치 후의 덩어리 계산
    answer += math.ceil((n - stations[-1] - w) / width)

    # 중간 기지국들 사이의 덩어리 계산
    for i in range(1, len(stations)):
        start = stations[i-1] + w + 1
        end = stations[i] - w - 1
        answer += math.ceil((end - start + 1) / width)

    return answer
