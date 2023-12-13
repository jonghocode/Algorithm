def solution(land):
    answer = 0

    dp = [[0]*4 for _ in range(len(land)+1)]
    # 현재값 + dp[i][k] 중 제일 큰 것
    for i in range(len(land)):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i+1][j] = max(land[i][j] + dp[i][k], dp[i+1][j])
    
    
    return max(dp[-1])