n = int(input())
dp = [0]*12
dp[1], dp[2], dp[3] = 1, 2, 4 # 초기화

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(n): # 케이스마다 출력
    k = int(input())
    print(dp[k])