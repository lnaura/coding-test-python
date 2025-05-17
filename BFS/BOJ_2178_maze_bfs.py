from collections import deque

# 입력
n, m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

# 상하좌우 확인
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지
    while queue:
        x,y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):    
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny <m:
                # 해당노드가 1이고 처음방문하는 경우만 최단거리기록록
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 
                    queue.append((nx,ny))
    
    return graph[n-1][m-1]

# 출력
print(bfs(0,0))


