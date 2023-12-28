# 13398 연속합 2

n = int(input())
lst = list(map(int, input().split()))
dp, dp2 = [-0x7fffffff]*(n+1), [-0x7fffffff]*(n+1)

for i in range(n):
    dp[i+1] = max(dp[i] + lst[i], lst[i]) # 부수지 않은 배열은 (그 전까지 합 + 현재 값) 과 현재 값 중 선택 
    dp2[i+1] = max(dp[i], dp2[i] + lst[i], lst[i]) # 부순 배열은 (그 전까지 합/이걸 고르면 부순거/) 과 (부쉈던 배열과 현재 값) 과 현재 값 중 선택

print(max(max(dp), max(dp2)))