def travel(now, chk):

    if chk == ((1 << n) -1): # 모든 곳을 방문했다면
        return board[now][0]
    if dp[now][chk] != 0: # 방문했던적이 있으면
        return dp[now][chk]
    
    dp[now][chk] = MAX
    for i in range(n):
        if chk & (1 << i) or board[now][i] == MAX: # 이미 방문했거나 갈 수 없는 길이라면
            continue
        dp[now][chk] = min(dp[now][chk], travel(i, chk|(1<<i)) + board[now][i])
    return dp[now][chk]



MAX = 0x7fffffff
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(1<<n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = MAX

print(travel(0, 1))