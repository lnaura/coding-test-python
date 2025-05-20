n = int(input())

li = [list(map(int,input().split())) for _ in range(n)]

li.sort()

for i in range(n):
    print(li[i][0], li[i][1])