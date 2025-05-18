from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 받기
n, m, v = map(int, input().split())

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 그래프

# 방문 리스트 초기화
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# DFS & BFS 수행
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
