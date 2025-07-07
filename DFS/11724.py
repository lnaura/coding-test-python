import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[]*n for _ in range(n+2)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)

