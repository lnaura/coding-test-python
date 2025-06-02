import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

v, e = map(int,input().split())
start = int(input())

#그래프 만들기
graph = [[] for i in range(v+1)]

#최단경로 테이블
distance = [INF] * (v+1)

# 그래프 초기화
for _ in range(e):
    x, y, z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for d in distance[1::] :
    if d == INF:
        print("INF")
    else:
        print(d)