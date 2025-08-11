import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 설정

def find_parent(parent, x):
    # 자기 자신이 대표가 아니면, 재귀적으로 대표를 찾고
    # 자신의 부모를 최종 대표로 갱신한다.
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 각 노드의 대표자를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 점의 개수, 차례수
n, game_turn = map(int,input().split())

# 대표 초기화(자기자신을 부모로 설정
# parent = []
# for i in range(n):
#     parent.append(i)

parent = list(range(n))

cycle_turn = 0
for i in range(1, game_turn+1):
    a, b = map(int,input().split())
    
    if find_parent(parent,a) == find_parent(parent,b):
        cycle_turn = i
        break
    else:
        union_parent(parent,a,b)

print(cycle_turn)