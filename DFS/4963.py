import sys
input = sys.stdin.readline

def DFS(x, y, graph, w, h, visited):
    stack = [(x, y)]
    visited[x][y] = True
    
    directions = [(0,-1), (0,1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]

    while stack:
        cx, cy = stack.pop()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            # 범위 체크 -> 방문 체크 -> 땅인지 체크
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny)) # 재귀 호출 대신 스택에 추가

def land(w,h,graph):
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                DFS(i,j,graph,w,h,visited)
                cnt += 1
    return cnt

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break

    graph=[list(map(int,input().split())) for _ in range(h)]
    print(land(w,h,graph))


