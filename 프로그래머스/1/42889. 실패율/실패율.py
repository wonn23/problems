def solution(N, stages):
    result = []
    # 실패율의 값을 구하고 실패율을 내림차순으로 정렬 이때의 스테이지 번호를 나타내야함
    # stage와 일치하는 사람 / 전체사람
    # staage와 일치하는 사람 / 전체 사람 - 이전 stage와 일치하는 사람
    # 어떻게 시간을 줄이지?
    users = len(stages)
    fail_user = 0
    for stage in range(1,N+1):
        fail_user += stages.count(stage-1)
        if users - fail_user == 0:
            result.append((0,stage))
        else: 
            fail_rate = stages.count(stage) / (users - fail_user)
            result.append((fail_rate,stage))
    result.sort(key = lambda x : x[0], reverse = True)
    return [i[1] for i in result]