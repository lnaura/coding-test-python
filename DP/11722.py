import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp = [1] * n


for i in range(n):
    dp[i] = 1

    for j in range(i+1):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))