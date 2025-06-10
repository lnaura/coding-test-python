import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    li = list(input().strip())

    count = 0
    while li:
        a = li.pop()
        if a == ")":
            count += 1
        elif a == "(":
            count -= 1
            
            if count < 0:
                print("NO")
                break

    if not li:
        if count > 0:
            print("NO") 
        elif count == 0:
            print("YES")

