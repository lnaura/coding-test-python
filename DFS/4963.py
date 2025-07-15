import sys
input = sys.stdin.readline

def DFS(x, y, graph, w, h, visited):
    stack = [(x, y)]
    visited[x][y] = True  # 방문 표시
    
    directions = [(0,-1), (0,1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]

    while stack:
        cx, cy = stack.pop()   # 현재 위치

        for dx, dy in directions:  # 다음위치
            nx, ny = cx + dx, cy + dy

            # 범위 체크 -> 방문 체크 -> 땅인지 체크
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny)) 

def land(w,h,graph):
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:  # 1인데 노방문
                DFS(i,j,graph,w,h,visited)
                cnt += 1         # 섬 찾으면 + 1
    return cnt

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break

    graph=[list(map(int,input().split())) for _ in range(h)]
    print(land(w,h,graph))


