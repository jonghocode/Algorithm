n, k = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
lst.sort()
dp = [[0]*2 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lst[i][0] + dp[j][0] <= k: # 무게를 더했을 때 가져올 수 있다면
            if dp[i][1] < dp[j][1] + lst[i][1]: # 원래 가치보다 더 높다면
                dp[i][1] = dp[j][1] + lst[i][1]
                dp[i][0] = dp[j][0] + lst[i][0]

    if dp[i][0] + dp[i][1] == 0:
        dp[i][0] = lst[i][0]
        dp[i][1] = lst[i][1]

answer = -1
for i in range(n):
    answer = max(answer, dp[i][1])
print(answer)