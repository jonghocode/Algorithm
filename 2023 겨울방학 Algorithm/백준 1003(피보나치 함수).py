def fibo(n):
    if dp[n] != -1:
        return dp[n]
    if n == 0:
        dp[0] = 0
        lst[n][0] += 1
        return dp[0]
    elif n == 1:
        dp[1] = 1
        lst[n][1] += 1
        return dp[1]
    
    dp[n] = fibo(n-1) + fibo(n-2)
    lst[n][0] = lst[n-1][0] + lst[n-2][0]
    lst[n][1] = lst[n-1][1] + lst[n-2][1]
    return dp[n]

t = int(input())
dp = [-1]*41
lst = [[0 for _ in range(2)] for _ in range(41)]
for _ in range(t):
    n = int(input())
    fibo(n)
    print(lst[n][0], dp[n])