## 🎮 프로그래머스 - 게임 맵 최단거리

- **문제 유형**: BFS, 최단 거리
- **문제 링크**: [프로그래머스 - 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)
- **언어**: Python

---

### 🔍 문제 요약

- `n x m` 크기의 게임 맵이 2차원 배열로 주어진다.
- `1`은 이동 가능한 칸, `0`은 벽으로 이동 불가.
- 캐릭터는 좌측 상단 `(0,0)`에서 시작해 우측 하단 `(n-1,m-1)`까지 도달해야 한다.
- 상하좌우로만 한 칸씩 이동 가능하며, 맵 밖으로는 이동할 수 없다.
- 상대 진영까지 이동할 수 있다면 **최소 몇 칸을 지나가는지**를 반환한다.
- 도달할 수 없다면 `-1`을 반환한다.

---

### 💡 풀이 전략

- **최단 거리**를 구하는 문제이므로 **BFS(너비 우선 탐색)**을 사용.
- 큐에 현재 위치를 넣고, 상하좌우 방향으로 한 칸씩 이동하며 탐색.
- 이동할 수 있는 칸(`1`)에 대해, 이전 거리 + 1을 누적 저장.
- 최종적으로 도착점의 값이 누적 거리로 갱신되었는지를 확인해 결과 반환.

---

### ✅ 코드

```python
from collections import deque

def solution(maps):
    answer = 0
    
    n,m = len(maps), len(maps[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny <0 or nx >= n or ny >= m:
                    continue
                
                if maps[nx][ny] == 0:
                    continue
                    
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    
        if maps[n-1][m-1] == 1:
            return -1
        else:
            return maps[n-1][m-1]
    
    answer = bfs(0,0)
    return answer
