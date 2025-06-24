## 📘 백준 15649번 - N과 M (1)

### 🔗 문제 링크
[https://www.acmicpc.net/problem/15649](https://www.acmicpc.net/problem/15649)

---

### 📌 문제 요약

- 자연수 N과 M이 주어졌을 때,
- 1부터 N까지의 수 중에서 **중복 없이 M개를 고른 모든 순열**을 출력하라.
- 출력은 **사전 순**이어야 함.

---

### 🔧 제한 사항

- 1 ≤ M ≤ N ≤ 8

---

### 🎯 입력 예시
```
3 2
```

### ✅ 출력 예시
```
1 2
1 3
2 1
2 3
3 1
3 2
```

---

### 🧠 알고리즘 분류

- 백트래킹 (Backtracking)
- DFS (깊이 우선 탐색)
- 순열 생성

---

### 🧩 풀이 방법

1. **리스트 s**: 현재까지 선택한 수열 저장
2. **visited 배열**: 중복을 피하기 위한 체크
3. **재귀 함수 dfs(depth)**: 깊이가 M이 되면 수열 출력

---

### 💡 핵심 코드

```python
n, m = map(int, input().split())

s = []
visited = [False] * (n+1)

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(depth + 1)
            s.pop()
            visited[i] = False

dfs(0)
```

---

### 🧠 백트래킹 개념 요약

| 개념 | 설명 |
|------|------|
| 상태 공간 트리 | 가능한 모든 선택지를 트리처럼 탐색 |
| 가지치기 | 조건에 맞지 않는 경우는 탐색하지 않음 |
| 되돌리기 | 한 선택을 끝낸 후 상태를 이전으로 복구 |
