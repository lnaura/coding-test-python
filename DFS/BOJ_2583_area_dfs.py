def dfs(x, y, graph, visited, m, n):
    cnt = 1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    stack = [(x, y)]
    visited[y][x] = True

    while stack:
        cx, cy = stack.pop()

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((nx, ny))
                cnt += 1
        
    return cnt

def count(m, n, graph):
    visited = [[False] * n for _ in range(m)]
    area = []

    for j in range(m):
        for i in range(n):
            if not visited[j][i] and graph[j][i] == 0:
                area.append(dfs(i, j, graph, visited, m, n))

    area.sort()
    print(len(area))
    print(' '.join(map(str, area)))

# 입력
m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            graph[j][i] = 1

count(m, n, graph)

