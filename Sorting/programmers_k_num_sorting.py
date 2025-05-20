def solution(array, commands):
    answer = []
    
    for li in commands:
        i, j, k = li
        li1 = []
        for n in range(i-1,j):
            li1.append(array[n])
        li1.sort()
        answer.append(li1[k-1])
            
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))