def solution(strings, n):
    answer = []

    strings.sort()
    strings.sort(key=lambda x: x[n])

    for i in strings:
        answer.append(i)

    return answer