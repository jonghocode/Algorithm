import sys

n, m, h = map(int, input().split()) # 열, 가로선 개수, 행
lst = [[0]*20 for _ in range(40)] # 사다리 좌표
for i in range(m):
    a, b = map(int, input().split())
    lst[a][b] = 1 # a높이에서 b열

def chk():
    for i in range(1, n+1): # 열
        t = i
        for j in range(1, h+1): # 행
            if lst[j][t]: t+=1
            elif lst[j][t-1]: t-=1
        if t!=i: return 0
    return 1


def dfs(x, y, d): # x좌표, y좌표, 추가 가로선 개수
    global k

    if d == k: # 가로선을 추가 다 했으면
        # 조건에 맞는지 검사
        # 맞다면 k 출력 후 종료
        if(chk()):
            print(k)
            sys.exit(0)
        return
    
    for i in range(x, h+1):
        for j in range(y, n):
            if not lst[i][j] + lst[i][j-1] + lst[i][j+1]:
                lst[i][j] = 1 # 가로선 추가
                dfs(i, j+1, d+1)
                lst[i][j] = 0
        y = 1


for i in range(4):
    k = i
    dfs(1, 1, 0)

print(-1)