from collections import deque

def BFS(graph, final, visited):
    queue = deque
    

def solution(n, roads, sources, destination):
     # 1. 인접 리스트로 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    # 2. 목적지로부터 각 지역까지의 최단 거리를 저장할 배열
    # -1은 아직 방문하지 않았거나 도달할 수 없음을 의미
    distances = [-1] * (n + 1)
    
    # 3. BFS를 위한 큐 준비
    queue = deque()
    
    # 4. BFS 시작점 설정 (목적지에서 출발)
    distances[destination] = 0
    queue.append(destination)
    
    # 5. BFS 실행
    while queue:
        current_node = queue.popleft()
        
         # 현재 노드와 연결된 이웃 노드들을 확인
        for neighbor in graph[current_node]:
            # 아직 방문하지 않은 노드라면
            if distances[neighbor] == -1:
                # 거리 갱신 (+1) 하고 큐에 추가
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    
    # 6. 각 부대원 위치(sources)에서 목적지까지의 최단 거리를 결과로 반환
    answer = [distances[s] for s in sources]
    
    return answer