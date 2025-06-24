n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

s = []
visited = [False] * n 

def dfs(start,depth):
    if depth == m:
        print(' '.join(map(str, s)))
        return
    
    prev = 0 # 이전 숫자 기억
    for i in range(start, n):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            s.append(nums[i])
            dfs(i + 1, depth + 1)
            s.pop()
            visited[i] = False
            prev = nums[i]

dfs(0,0)

