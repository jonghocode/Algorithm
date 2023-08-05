n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [-1] * 10001
dp[0] = 0

for i in coin:
    for j in range(i, k+1):
        if dp[j-i] != -1:
            if dp[j] != -1:
                dp[j] = min(dp[j], dp[j-i]+1)
            else :
                dp[j] = dp[j-i]+1
print(dp[k])