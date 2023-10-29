def solution(N, stages):
    result = []
    users = len(stages)
    fail_counts = [0] * (N + 2)

    for stage in stages:
        fail_counts[stage] += 1

    fail_user = 0
    for stage in range(1, N + 1):
        fail_user += fail_counts[stage - 1]
        if users - fail_user == 0:
            result.append((0, stage))
        else:
            fail_rate = fail_counts[stage] / (users - fail_user)
            result.append((fail_rate, stage))

    result.sort(key=lambda x: x[0], reverse=True)
    return [i[1] for i in result]
