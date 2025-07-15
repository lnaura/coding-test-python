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

        if 0 <= nx < n and 0 <= ny < m:  # 범위 안 ?
            if nx == px and ny == py:   # 이전에 지나온 곳과 다음에 갈 곳이 같으면
                continue                # 안됨. -> 전으로 돌아가는 것이기 때문
            
            if game[nx][ny] == color:     # 다음 칸이 같은 컬러이면서
                if visited[nx][ny]:       # 방문했으면 한바퀴 돈 것임.
                    return True           # True 리턴 후 끝

                if DFS(nx,ny,x,y,color):  # 방문하지 않았으면 재귀하고 거기서 True 리턴하면
                    return True           # True 리턴 하고 끝
    return False

for i in range(n):     # 모든 곳을 탐색하기위해 (모든 구역을)
    for j in range(m):
        if not visited[i][j]: # 방문하지 않은!
            if DFS(i,j,-1,-1,game[i][j]): # 첫 시작점의 이전값은 -1,-1
                print("Yes")              # 리턴이 1이면 yes 출력 후 프로그램 끝내기
                exit()

print("No")

