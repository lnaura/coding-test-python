def solution(N, stages):
    result = []
    total_users = len(stages)

    for i in range(1, N + 1):
        current = stages.count(i)

        if total_users == 0:
            fail = 0
        else:
            fail = current / total_users

        result.append((i, fail))
        total_users -= current

    result.sort(key=lambda x: x[1], reverse=True)
    return [stage for stage, _ in result]