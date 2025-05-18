## 📘 백준 1260번: DFS와 BFS

### 📌 문제 설명

N개의 정점과 M개의 간선으로 이루어진 무방향 그래프가 주어졌을 때, 
정점 번호가 작은 것을 우선으로 탐색하는 **DFS**와 **BFS** 결과를 출력하는 문제입니다.

---

### 📥 입력

- 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점 V가 주어진다.
- 다음 M개의 줄에 간선이 연결하는 두 정점의 번호가 주어진다.


---

### 📤 출력

- 첫째 줄에 DFS 결과
- 둘째 줄에 BFS 결과


---

### 🧠 풀이 전략

- **DFS**는 재귀로 구현하고, **BFS**는 `deque`를 이용해 큐로 구현합니다.
- 정점 번호가 작은 것을 먼저 방문해야 하므로, **인접 리스트 정렬**이 필요합니다.
- 방문한 정점을 저장할 `visited` 배열은 DFS와 BFS 각각 따로 사용해야 합니다.

---

### 💻 코드 (Python)

```python
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

# 입력
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 간선 입력
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 무방향 그래프

# 방문 배열
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# 결과 출력
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)


