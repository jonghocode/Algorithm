n, k = map(int, input().split())
lst = []
dp = [0]*(k+1)
dp[0] = 1

for i in range(n):
    lst.append(int(input()))

for i in range(n):
    for j in range(lst[i], k+1):
       dp[j] += dp[j-lst[i]]
    print(dp)
        
print(dp[k])