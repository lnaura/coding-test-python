def dfs(x, y, graph, visited, h, w):
    # 8방향 탐색 (상, 하, 좌, 우, 대각선 4방향 포함)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # 스택을 이용하여 반복문으로 DFS 구현
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        
        # 8방향으로 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_islands(w, h, graph):
    visited = [[False] * w for _ in range(h)]  # 방문 여부를 기록하는 배열
    result = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:  # 섬 발견
                dfs(i, j, graph, visited, h, w)
                result += 1  # 섬 개수 증가
    
    return result

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    print(count_islands(w, h, graph))
