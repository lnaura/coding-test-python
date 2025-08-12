import sys
input = sys.stdin.readline

size, m = map(int,input().split())

graph = [[0] * (size + 1)]

for i in range(size):
    row = [0] + list(map(int,input().split()))
    graph.append(row)


D = [[0] * (size+1) for _ in range(size+1)]

for i in range(1, size+1):
    for j in range(1, size+1):
        D[i][j] = graph[i][j] + D[i-1][j] + D[i][j-1] - D[i-1][j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    sum = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(sum)