import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    lists = list(map(int, input().split()))
    k = len(lists)
    current_node = lists[0]

    for i in range(1,k-1,2):
        neighbor = lists[i]
        distance = lists[i+1]
        tree[current_node].append((neighbor,distance))
        
def DFS(node,dist):
    visited[node] = True
    for neighbor, d in tree[node]:
        if not visited[neighbor]:
            distance[neighbor] = dist + d
            DFS(neighbor, dist + d)

visited = [False] * (n+1)
distance = [0] * (n+1)
DFS(1,0)
A = distance.index(max(distance))

visited = [False] * (n+1)
distance = [0] * (n+1)
DFS(A,0)
print(max(distance))