n = int(input())
dp = [0]*1000001
dp[2], dp[3] = 1, 1 # 초기화

for i in range(4, n+1):
    dp[i] = dp[i-1] + 1 # 1을 빼는 경우(bottom up이기 때문에 더함)
    if i%2 == 0: # 2를 나누는 경우
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0: # 3을 나누는 경우
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])