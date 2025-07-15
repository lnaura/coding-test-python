import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = []
def DFS(graph, n):
    visited = [[False] * n for _ in range(n+1)]
    cnt = 0
    
    for i in range(1, n+1) :