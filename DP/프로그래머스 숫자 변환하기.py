def solution(x, y, n):
    answer = 0
    
    dp = [-1]*(y+1)
    dp[x] = 0

    for j in range(x, y+1):
        if dp[j] != -1 and j+n <= y: # n을 더하는 경우
            if dp[j+n] == -1:
                dp[j+n] = dp[j]+1
            elif dp[j+n] != -1:
                dp[j+n] = min(dp[j+n], dp[j]+1)
        if dp[j] != -1 and j*2 <= y: # 2를 곱하는 경우
            if dp[j*2] == -1:
                dp[j*2] = dp[j]+1
            elif dp[j*2] != -1:
                dp[j*2] = min(dp[j*2], dp[j]+1)
        if dp[j] != -1 and j*3 <= y: # 3을 곱하는 경우
            if dp[j*3] == -1:
                dp[j*3] = dp[j]+1
            elif dp[j*3] != -1:
                dp[j*3] = min(dp[j*3], dp[j]+1)

    
    return dp[y]