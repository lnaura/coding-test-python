import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e9)

m,n  = map(int, input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

direction = [(0,-1),(0,1),(1,0),(-1,0)]
cost = [[INF]* m for _ in range(n)] # 최소 비용
cost[0][0] = 0
new_cost = 0

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        cx , cy = queue.popleft()

        for dx, dy in direction:
            nx = cx + dx
            ny = cy + dy
            
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                
                if graph[nx][ny] == 0:
                    if cost[cx][cy] < cost[nx][ny]:
                        cost[nx][ny] = cost[cx][cy]
                        queue.appendleft((nx,ny))
                else:
                    if cost[cx][cy]+1 < cost[nx][ny]:
                        cost[nx][ny] = cost[cx][cy] + 1
                        queue.append((nx,ny))
BFS(0,0)
print(cost[n-1][m-1])