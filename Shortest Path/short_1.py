import sys
import heapq
INF = int(1e9)

# 노드 개수, 간선 개수, 시작 도시
n, m, start = map(int,sys.stdin.readline().split())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 초기화
graph = [[] for i in range(n+1)]

# 최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 간선정보 입력
for _ in range(m):
    a , b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리더ㅙㅆ으면 스킵
        if dist > distance(now):
            continue
    
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)       

print(count - 1 , max_distance)