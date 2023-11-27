# 문제를 잘못 읽었다.
# 첫 번째 집을 선택하고 난 후 다 구해준다. 그리고 마지막부분은 첫번째 집과 마지막 집 색깔이 달라야하기 때문에
# dp[n-1][i] = 0x7fffffff 이렇게 최댓값을 넣어주고 답을 구했다.

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0x7fffffff

for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = 1001, 1001, 1001
    dp[0][i] = lst[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + lst[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + lst[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + lst[j][2]
        
    dp[n-1][i] = 0x7fffffff
    answer = min(answer, min(dp[n-1]))

print(answer)