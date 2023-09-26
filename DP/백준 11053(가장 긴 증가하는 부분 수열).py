n = int(input())
dp = [1] * 1010
lst = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]: # 자신보다 작은 것 중에서
            dp[i] = max(dp[i], dp[j]+1) # (제일 큰 정수+1)를 넣기

print(max(dp))