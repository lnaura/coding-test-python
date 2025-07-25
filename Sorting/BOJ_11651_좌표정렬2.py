import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort(key=lambda x: (x[1], x[0]))

for x, y in points:
    print(x, y)
    