import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, k, start = map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append((y,1))

def dijkstra(start):
    q = []

    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count = 0
i = 0
for d in distance:
    if d == k:
        print(i)
        count += 1
    i += 1

if count == 0:
    print(-1)
    