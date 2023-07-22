n = int(input())

dp = [-1]*5010 # -1로 초기화
dp[0] = 0

for i in range(3, n+1): # 3으로 배달
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1

for i in range(5, n+1): # 5로 배달
    if dp[i-5] != -1: # 5로 배달할 수 있다면
        if dp[i] != -1: # 현재 값이 있으면 (전 값+1)과 현재값 비교
            dp[i] = min(dp[i], dp[i-5]+1)
        else : # 현재 값이 없으면 (전 값+1)
            dp[i] = dp[i-5] + 1

print(dp[n])