from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx,sy,fx,fy,graph,l):
    directions = [(-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]
    queue = deque()
    queue.append((sx,sy))

    while queue:
        x,y =queue.popleft()
        if not (x == fx and y == fy):
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0<= nx < l and 0 <= ny <l:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx,ny))
    return(graph[fx][fy])



n = int(input())

for _ in range(n):
    l = int(input())
    sx,sy = tuple(map(int,input().split()))
    fx,fy = tuple(map(int,input().split()))

    graph = [[0]*l for _ in range(l)]
    print(BFS(sx,sy,fx,fy,graph,l))
