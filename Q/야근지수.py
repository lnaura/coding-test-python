import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    
    que = []
    
    for work in works:
        que.append(-1 * work)

    heapq.heapify(que)

    for i in range(n):
        max = que.get()
        
        if max == 0:
            break
            
        que.put(max+1)
    
    while not que.empty():
        work = que.get()
        answer += (-work) ** 2
        
    return answer