import sys

def cnt(d, t):
    global n, m, answer
    if(d == m):
        sum = 0
        for i, j in z:
            MIN = 987654321
            for p in range(d):
                MIN = min(MIN, abs(i-o[p][0])+abs(j-o[p][1]))
            sum += MIN
        answer = min(answer,sum)
        return
    for i in range(len(c)):
        o[d][0] = c[i][0]
        o[d][1] = c[i][1]
        cnt(d+1, i+1)


n, m = map(int, input().split())
c, z = [], []
answer = 987654321
for i in range(n):
    k = sys.stdin.readline().strip().split()
    for j in range(n):
        if k[j] == '1':
            z.append([i,j])
        elif k[j] == '2':
            c.append([i,j])

chk = [0]*(n**2)
o = [[0]*n for _ in range(n)]
cnt(0, 0)
print(answer)