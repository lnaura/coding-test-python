def dfs(x,y,graph,visited,n):
    cnt = 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    visited[x][y] = True
    
    for dx,dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            cnt += 1
    return cnt


def count(graph,n):
    visited = [[False]*n for _ in range(n)]
    result = 0
    li = []
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] == 1:
                li.append(dfs(x,y,graph,visited,n))
                result += 1
    return result, li

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

print(count)

