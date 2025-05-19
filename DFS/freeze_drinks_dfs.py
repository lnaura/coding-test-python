n,m = map(int,input().split())

graph =[list(map(int,input())) for _ in range(n)]

def dfs(x,y):
    # 주어진 범위를 벗어나면 종료
    if !(0 <= x < n and 0 <= y <= m):
        return False
    
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 상하좌우 위치 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)