from collections import deque
import sys
input = sys.stdin.readline

start, end = map(int,input().split())
MAX = 100001

time = [-1] * MAX
queue = deque()

queue.append(start)
time[start] = 0

while queue:
    node = queue.popleft()

    if node == end:
        print(time[node])
        break

    if 0 <= node * 2 < MAX and time[node * 2] == -1:
        time[node * 2] = time[node]
        queue.appendleft(node * 2)
    
    for n_node in (node + 1, node - 1):
        if 0 <= n_node < MAX and time[n_node] == -1:
            time[n_node] = time[node] + 1
            queue.append(n_node)