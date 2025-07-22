import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

stack = []

mlist = [-1] * n

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        s = stack.pop()
        mlist[s] = A[i]
    
    stack.append(i)

for i in mlist:
    print(i, end = " ")