s = input()
dp = [0]*(len(s)+1)
n, dp[0], dp[1] = len(s), 1, 1
# i가 1일때 dp는 2부터 시작

if s[0] == '0': # 첫번째 0이 오면 안됨
    print(0)
    exit()
else :
    for i in range(1, n):
        if s[i-1] == '0' and s[i] != '0': # 앞이 0
            dp[i+1] = dp[i]
        elif s[i-1] != '0' and s[i] == '0': # 두번째가 0
            if s[i-1] == '1' or s[i-1] == '2':
                dp[i+1] = dp[i-1]
            else:
                break
        elif s[i-1] != '0' and s[i] != '0': # 둘 다 0이 아닌 경우
            t = int(s[i-1]+s[i])
            if 1 <= t and t <= 26:
                dp[i+1] = (dp[i] + dp[i-1])%1000000
            else:
                dp[i+1] = dp[i]

print(dp[n])
