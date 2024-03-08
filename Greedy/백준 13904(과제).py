import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
dp = [0 for _ in range(1001)]
MAX = int(1e12)

for d, w in lst:
    sw = MAX
    for i in range(1, d+1):
        if dp[i] < sw:
            sw = dp[i]
            idx = i
    
    dp[idx] = w

print(sum(dp))
for i in range(n+1):
    print(dp[i], end=' ')