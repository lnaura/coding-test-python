INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for i in range(n+1)]

for a in range(1,n+1):
    for b in range(1 , n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x][y] = min(graph[x][y],z)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
