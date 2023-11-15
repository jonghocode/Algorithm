import sys

A = [""] + list(sys.stdin.readline().strip())
B = [""] + list(sys.stdin.readline().strip())
dp = [[""]*len(B) for _ in range(len(A))]

# dp 부분에 길이를 저장하는게 아니라 문자열을 바로 저장해서
# 역추적을 따로 할 필요가 없음
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]: # 대각선에 있는 값을 가져옴
            dp[i][j] = dp[i-1][j-1] + A[i]
        else: # 바로 위 값 아니면 왼쪽 값 중 큰 값을 가져옴(역추적)
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

answer = dp[-1][-1]
print(len(answer))
print(answer)