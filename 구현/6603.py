import sys

input = sys.stdin.readline
from collections import deque

size = int(input())
k = int(input())

# 사과 초기화
apple = [[0] * (size) for _ in range(size)]

# 사과 저장
for i in range(k):
    n, m = map(int, input().split())
    apple[n - 1][m - 1] = 1

# 방향 변환(오른쪽,아래,왼쪽,위)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

snake = deque()
head_x, head_y = 0, 0
snake.append((head_x, head_y))
time = 0

l = int(input())  # 방향 변환 횟수

cnt = 0

move = []
for i in range(l):
    move.append(list(input().split()))

count = 0
while True:
    if int(move[count][0]) == time:
        if move[count][1] == "D":
            cnt += 1
        elif move[count][1] == "L":
            cnt -= 1

        cnt %= 4

        if count < l - 1:
            count += 1

    time += 1
    head_x += direction[cnt][0]
    head_y += direction[cnt][1]

    if not (0 <= head_x < size and 0 <= head_y < size) or (head_x, head_y) in snake:
        print(time)
        exit()

    if apple[head_x][head_y] == 0:
        snake.append((head_x, head_y))
        snake.popleft()
    else:
        apple[head_x][head_y] = 0
        snake.append((head_x, head_y))

print(time)
