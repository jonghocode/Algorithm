def p(idx, bag):
    if idx == n:
        return 0
    
    if dp[idx][bag] != -1:
        return dp[idx][bag]
    a, b = 0, 0
    a = p(idx + 1, bag)
    if bag + lst[idx][0] <= k:
        b = p(idx + 1, bag + lst[idx][0]) + lst[idx][1]
    dp[idx][bag] = max(a, b)
    return dp[idx][bag]

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(k+1)] for _ in range(n)]

print(p(0, 0))