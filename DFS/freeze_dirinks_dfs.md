## 🧊 음료수 얼려 먹기 (DFS)

### 📌 문제 요약
N x M 크기의 얼음 틀이 주어집니다. 얼음 틀에는 구멍(0)과 칸막이(1)가 있으며, 구멍이 연결되어 있으면 하나의 음료수로 취급합니다. 얼릴 수 있는 음료수의 총 개수를 구하세요.

- 상하좌우로 연결된 '0'들은 하나의 그룹으로 간주됩니다.
- 연결된 모든 '0'들을 '1'로 바꿔가며 방문 처리하면 됩니다.

### 📥 입력
- 첫째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 ≤ N, M ≤ 1000)
- 둘째 줄부터 N개의 줄에는 0과 1로 구성된 문자열이 주어집니다.


### 📤 출력
- 얼릴 수 있는 음료수의 개수를 출력합니다.


## 🧠 풀이 전략

1. **전체 2차원 배열을 순회**하면서 `graph[i][j] == 0`인 지점을 발견하면 DFS 시작.
2. **DFS 탐색 중 만나는 모든 '0'을 '1'로 변경**하여 재방문 방지.
3. DFS가 True를 반환하면, 새로운 음료수 영역을 찾은 것이므로 `result += 1`.
4. 모든 좌표를 확인하며 DFS를 반복.

### ✅ 핵심 포인트
- 이 문제는 연결 요소(connected components)를 세는 전형적인 DFS 문제입니다.
- 방문 처리를 꼭 해주지 않으면 무한 재귀에 빠질 수 있습니다.

## 💻 핵심 코드 요약 (Python)

```python
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)

