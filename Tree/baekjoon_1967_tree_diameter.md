
# 백준 1967번: 트리의 지름

## ✅ 문제 요약

- 루트가 1인 트리가 주어진다.
- 각 간선에는 가중치가 존재한다.
- 트리에서 가장 긴 경로(= 지름)의 길이를 구하는 문제.

---

## 🔍 트리의 지름이란?

트리에서 임의의 두 정점 간의 가장 긴 거리이다.

### 구하는 방법 (2번 DFS/BFS)

1. 아무 노드에서 가장 먼 노드 A를 찾는다.
2. A에서 가장 먼 노드 B를 찾는다.
3. A-B 간의 거리가 트리의 지름이다.

---

## 🧠 풀이 전략 (DFS 이용)

1. 트리를 인접 리스트로 구성
2. 1번 노드에서 DFS → 가장 먼 노드 A 기록
3. A에서 DFS → 가장 먼 거리 계산 = 트리의 지름

---

## 💡 정답 코드 (Python)

```python
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

# 트리 입력
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

# DFS 함수
def dfs(node, dist):
    visited[node] = True
    for neighbor, weight in tree[node]:
        if not visited[neighbor]:
            distance[neighbor] = dist + weight
            dfs(neighbor, dist + weight)

# 1차 DFS: 아무 노드(1번)에서 가장 먼 노드 A 찾기
visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(1, 0)
A = distance.index(max(distance))  # 가장 먼 노드 A

# 2차 DFS: A에서 가장 먼 거리 찾기 → 트리의 지름
visited = [False] * (n + 1)
distance = [0] * (n + 1)
dfs(A, 0)
print(max(distance))
```

---

## 📌 예제 입력

```
5
1 3 2
1 4 3
4 5 6
3 2 4
```

### 📌 트리 구조

```
    1
   / \
  3   4
 /     \
2       5
```

가장 긴 경로: `2 → 3 → 1 → 4 → 5` = `4 + 2 + 3 + 6 = 15`

출력: `15`

---

## ✅ 요약 정리

| 단계 | 설명 |
|------|------|
| 1차 DFS | 루트에서 가장 먼 노드 A 찾기 |
| 2차 DFS | A에서 가장 먼 거리 찾기 → 지름 |
| 주요 자료구조 | 인접 리스트, DFS, visited[], distance[] |
