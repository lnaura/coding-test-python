import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 설정
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)] # 인접리스트로 구성

# 트리 입력
for _ in range(n-1):
    u, v, w = map(int,input().split())
    tree[u].append((v,w))
    tree[v].append((u,w))

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

