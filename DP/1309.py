import sys

# 입력을 빠르게 받기 위함
input = sys.stdin.readline

N = int(input())
MOD = 9901

# dp[i]는 i번째 줄까지의 경우의 수를 의미
# dp[i][0]: i번째 줄에 사자를 놓지 않은 경우
# dp[i][1]: i번째 줄 왼쪽에만 사자를 놓은 경우
# dp[i][2]: i번째 줄 오른쪽에만 사자를 놓은 경우

# N=1일 때의 초기값
# prev_states는 i-1번째 줄의 상태를 저장
# [사자 없음, 왼쪽에만 있음, 오른쪽에만 있음]
prev_states = [1, 1, 1]

if N == 1:
    print(sum(prev_states) % MOD)
else:
    # 2번째 줄부터 N번째 줄까지 반복
    for i in range(2, N + 1):
        # curr_states는 i번째 줄의 상태를 계산
        curr_states = [0, 0, 0]

        # 1. i번째 줄에 사자를 놓지 않는 경우
        #    i-1번째 줄에는 사자가 없거나, 왼쪽 또는 오른쪽에 있어도 된다.
        curr_states[0] = (prev_states[0] + prev_states[1] + prev_states[2]) % MOD

        # 2. i번째 줄 왼쪽에만 사자를 놓는 경우
        #    i-1번째 줄에는 사자가 없거나, 오른쪽에만 있어야 한다.
        curr_states[1] = (prev_states[0] + prev_states[2]) % MOD

        # 3. i번째 줄 오른쪽에만 사자를 놓는 경우
        #    i-1번째 줄에는 사자가 없거나, 왼쪽에만 있어야 한다.
        curr_states[2] = (prev_states[0] + prev_states[1]) % MOD
        
        # 현재 상태를 다음 반복을 위해 이전 상태로 업데이트
        prev_states = curr_states
    
    # N번째 줄의 모든 경우의 수를 합산
    result = sum(prev_states) % MOD
    
    print(result)