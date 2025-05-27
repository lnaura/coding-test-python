def solution(numbers):
    answer = ''
    str_numbers = [str(n) for n in numbers]
    print(str_numbers)
    str_numbers.sort(key = lambda x:x*3, reverse = 1)
    answer = ''.join(str_numbers)
    return answer

print(solution([3, 30, 34, 5, 9]))
