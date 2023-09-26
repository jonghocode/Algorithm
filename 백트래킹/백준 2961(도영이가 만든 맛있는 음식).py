def cook(ssum, bsum, idx, d):
    global answer, n
    if d >= 1 and answer > abs(ssum-bsum):
        answer = abs(ssum-bsum)
        
    for i in range(idx, n):
        cook(ssum*s[i], bsum+b[i], i+1, d+1)

n = int(input())
s, b = [], []
answer = 1000000001
for i in range(n):
    x, y = map(int, input().split())
    s.append(x)
    b.append(y)

cook(1, 0, 0, 0)
print(answer)
