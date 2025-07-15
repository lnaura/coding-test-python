from collections import deque
import sys
input = sys.stdin.readline


def BFS(sx,sy,fx,fy,graph,l):
    directions = [(-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(2,-1),(1,2),(2,1)]
    queue = deque()
    queue.append((sx,sy))

    while queue:
        x,y = queue.popleft()

        if x == fx and y == fy:
            return graph[fx][fy]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0<= nx < l and 0 <= ny <l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))    

n = int(input())

for _ in range(n):
    l = int(input())
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    graph = [[0]*l for _ in range(l)]

    if sx == fx and sy == fy:
        print(0)
        continue
    else: 
        print(BFS(sx,sy,fx,fy,graph,l))
