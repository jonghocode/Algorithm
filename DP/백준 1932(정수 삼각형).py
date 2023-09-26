n = int(input())
dp = []
for i in range(1, n+1):
    dp.append(list(map(int, input().split())))

for i in range(n-2, -1, -1): # 마지막 전 줄부터 위로 올라가면서
    for j in range(i, -1, -1): 
        # 아래수를 더했을 때와 오른쪽 아래 수를 더했을 때 중 더 큰 값 넣기
        dp[i][j] = max(dp[i][j] + dp[i+1][j], dp[i][j] + dp[i+1][j+1])

print(dp[0][0])