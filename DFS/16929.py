import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
game = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
directions = [(0,-1),(-1,0),(1,0),(0,1)]

def DFS(x,y,px,py,color):
    visited[x][y] = True

    for dx,dy in directions:
        nx,ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if nx == px and ny == py:
                continue
            
            if game[nx][ny] == color:
                if visited[nx][ny]:
                    return True

                if DFS(nx,ny,x,y,color):
                    return True
    return False

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if DFS(i,j,-1,-1,game[i][j]):
                print("Yes")
                exit()

print("No")

