import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())
# 각 비용 입력받기
costs = [list(map(int, input().split())) for _ in range(n)]

# 최소값 저장할 변수
min_total_cost = INF

# 첫번째 집을 R,G,B로 고정해서 총 3번의 DP
for start_color in range(3):
    # 초기화
    dp = [[0]*3 for _ in range(n)]
    
    # 초기값 설정
    # 고정된 색 말고 다른 색들을 무한대로 설정
    for color in range(3):
        if color == start_color:
            dp[0][color] = costs[0][color]
        else:
            dp[0][color] = INF
    
    # DP 테이블 채우기
    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]) # 현재 집 Red
        dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]) # 현재 집 Green
        dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]) # 현재 집 Blue

    # 마지막 집의 색상 확인 , 결과 계산
    for end_color in range(3):
        if end_color != start_color:
            min_total_cost = min(min_total_cost, dp[n-1][end_color])


print(min_total_cost)
