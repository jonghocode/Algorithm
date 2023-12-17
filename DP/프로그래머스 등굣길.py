# 기본적인 2차원 dp 문제입니다.
# 문제에서 "아래와 오른쪽으로만 이동할 수 있다" 이 부분을 보고 dp를 이용해야한다고 의심했고
# 경우의 수를 구한다는 부분에서 확신했습니다.

def solution(m, n, puddles):
    dp = [[-1]*m for _ in range(n)]
    chk = [[0]*m for _ in range(n)]
    for x, y in puddles: # x좌표와 y좌표가 반대로 되어있음
        chk[y-1][x-1] = 1
    
    for i in range(m): # 웅덩이 표시하기
        if chk[0][i] == 1:
            break
        else:
            dp[0][i] = 1
    
    for i in range(1, n):
        if chk[i-1][0] != 1 and chk[i][0] != 1: # 첫 열은 무조건 위에서만 오기때문에 처리해줌
            dp[i][0] = dp[i-1][0]
        for j in range(1, m):
            if chk[i][j] != 1:
                if dp[i][j-1] != -1 and dp[i-1][j] != -1: # 둘 다 웅덩이가 아니라면 경우의 수 더하기
                    dp[i][j] = (dp[i][j-1] + dp[i-1][j])%1000000007
                elif dp[i][j-1] == -1 and dp[i-1][j] != -1:
                    dp[i][j] = dp[i-1][j]
                elif dp[i][j-1] != -1 and dp[i-1][j] == -1:
                    dp[i][j] = dp[i][j-1]
    
    
    if dp[n-1][m-1] == -1: # 도착을 하지 못했다면 -1이므로 0으로 바꿔준다.
        dp[n-1][m-1] = 0
    return dp[n-1][m-1]