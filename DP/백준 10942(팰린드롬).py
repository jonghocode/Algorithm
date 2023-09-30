# 2칸 까지는 예외 처리로 처리해주고
# 나머지는 양 끝이 같고 dp[i+1][j-1] == 1인지 체크
import sys
n = int(input())
lst = list(map(int, input().split()))
# 0,0 / 1,1 / 2,2/ 3,3/ 4,4/ 5,5
# 0,1 / 1,2 / 2,3
# 범위 안 넘어가게 체크
dp = [[0]*2010 for _ in range(2010)]
for cnt in range(n):
    stx, sty = 0, cnt
    if stx == 0 and sty == 0: # 한 자리
        while True:
            if stx > n-1 or sty > n-1:
                break
            dp[stx][sty] = 1
            stx+=1
            sty+=1
    elif stx == 0 and sty == 1: # 두 자리
        while True:
            if stx > n-1 or sty > n-1:
                break
            if lst[stx] == lst[sty]:
                dp[stx][sty] = 1
            stx+=1
            sty+=1
    else:
        while True:
            if stx > n-1 or sty > n-1:
                break
            if lst[stx] == lst[sty] and dp[stx+1][sty-1] == 1:
                dp[stx][sty] = 1
            stx+=1
            sty+=1

m = int(input())
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(dp[a-1][b-1])