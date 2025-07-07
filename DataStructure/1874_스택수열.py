import sys
input = sys.stdin.readline

stack = []
for _ in range(n):
    n = int(input())
    stack.append(n)

cnt = 0
for i in range(n):
    target = stack[i]
    if target > cnt:
        for i in range(target):
            cnt += 1
            
    else

    


