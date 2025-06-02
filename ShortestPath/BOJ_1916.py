import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1) 

for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

start, finish = map(int,input().split())

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance[finish])

