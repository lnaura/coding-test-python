import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MOD = 1_000_000_000

# dp[i][j]: i개의 정수를 더해서 합 j를 만드는 경우의 수
dp = [[0] * (n + 1) for _ in range(k + 1)]

# 초기값 설정:
# dp[i][0] = 1 (숫자 i개를 써서 0을 만드는 방법은 0만 i번 더하는 1가지)
for i in range(k + 1):
    dp[i][0] = 1


for i in range(1, k + 1):
    for j in range(1, n + 1):
        # 점화식: (k-1개로 n만들기) + (k개로 n-1 만들기)
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[k][n])