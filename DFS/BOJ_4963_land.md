# 백준 4963번 - 섬의 개수

## 문제 설명

2차원 배열로 나타낸 지도에서 1은 땅, 0은 바다입니다. 주어진 지도에서 연결된 땅을 하나의 **섬**으로 보고, 섬의 개수를 구하는 문제입니다. 두 땅은 가로, 세로, 또는 대각선으로 연결된 경우에만 서로 연결된 것으로 취급합니다.

---
## 입력

- 첫째 줄에 너비 `w`와 높이 `h`가 주어집니다. (`1 ≤ w, h ≤ 50`)
- 그 후 `h`개의 줄에 각 줄마다 `w`개의 수가 주어집니다. 각 수는 `0` 또는 `1`로, `1`은 땅을, `0`은 바다를 나타냅니다.
- 입력의 끝은 `0 0`으로 주어지며, 이는 종료 조건입니다.

---
## 출력

- 각 테스트 케이스에 대해 섬의 개수를 출력합니다.

---
## 문제 풀이

이 문제를 해결하기 위해서는 **깊이 우선 탐색(DFS)**을 활용하여 연결된 섬을 찾는 방법을 사용할 수 있습니다. 한 섬을 발견하면, 그 섬과 연결된 모든 `1`들을 방문하여 하나의 섬으로 처리하고, 그 섬을 카운트한 뒤 다음 섬을 찾습니다.

---
## 풀이 방법

1. **DFS 탐색**: 각 칸에 대해 `1`인 땅을 발견하면 DFS를 통해 그 섬과 연결된 모든 `1`들을 방문 처리합니다. 이때, 방문한 곳은 다시 방문하지 않도록 처리해야 합니다.
2. **방문 처리 배열**: 각 칸이 방문되었는지를 확인하기 위해 `visited` 배열을 사용합니다.
3. **8방향 탐색**: 섬이 가로, 세로, 대각선으로 연결될 수 있기 때문에 8방향으로 탐색해야 합니다.

---
## 코드 구현

```python
def dfs(x, y, graph, visited, h, w):
    # 8방향 탐색 (상, 하, 좌, 우, 대각선 4방향 포함)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # 스택을 이용하여 반복문으로 DFS 구현
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        
        # 8방향으로 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))

def count_islands(w, h, graph):
    visited = [[False] * w for _ in range(h)]  # 방문 여부를 기록하는 배열
    result = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:  # 섬 발견
                dfs(i, j, graph, visited, h, w)
                result += 1  # 섬 개수 증가
    
    return result

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    print(count_islands(w, h, graph))
