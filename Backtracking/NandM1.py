n,m = map(int,input().split())

s = []
visited = [False] * (n+1)

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(depth+1)
            s.pop()
            visited[i] = False

dfs(0)