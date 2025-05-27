import sys

input = sys.stdin.readline

t = int(input().rstrip())
n = [int(input().rstrip()) for _ in range(t)]

for x in n:
    level = 0
    # n마리 잡았을 때 경험치
    exp = (x * (x + 1)) // 2

    left = 0
    right = x
 
    while left <= right :
        mid = (left + right) // 2

        nn = mid*(mid + 1)

        if nn <= exp:
            level = mid
            left = mid + 1

        else: 
            right = mid - 1

    print(level + 1)    

    