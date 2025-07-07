import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    r,g,b = map(int,input().split()) 
    
    if i == 0:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b
    else:
        dp[i][0] = r + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = g + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = b + min(dp[i-1][0],dp[i-1][1])

final_answer = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(final_answer)