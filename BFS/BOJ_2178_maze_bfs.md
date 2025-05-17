## 🧭 미로 탐색 (BOJ 2178)

- **문제 분류**: BFS, 그래프 탐색
- **문제 링크**: [백준 2178번 - 미로 탐색](https://www.acmicpc.net/problem/2178)
- **언어**: Python

---

### 🔍 문제 요약

- N x M 크기의 미로가 주어진다.
- (1, 1)에서 출발해 (N, M)으로 이동할 때 지나야 하는 최소 칸 수를 구하라.
- 이동은 상하좌우 인접한 칸으로만 가능하고, 1은 이동 가능한 칸, 0은 벽이다.

---

### 💡 풀이 아이디어

- BFS를 사용하면 최단 경로를 보장할 수 있으므로 BFS로 풀이.
- `graph[x][y]`에 해당 칸까지 이동하는 데 걸린 최소 칸 수를 기록.
- 인접한 칸이 1(길)이고 아직 방문하지 않은 경우에만 큐에 추가하고 거리 갱신.

---

### 📌 코드

```python
from collections import deque

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):    
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 처음 방문하는 길이면 거리 갱신
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1 
                    queue.append((nx, ny))
    
    return graph[n-1][m-1]

# 출력
print(bfs(0, 0))
