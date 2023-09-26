n = int(input())
line = []
for i in range(n):
    line.append(list(map(int, input().split())))

line.sort()
dp = [[line[0][1], 1]]

for i in range(1, len(line)):
    st, ed = line[i][0], line[i][1]
    x, y = -1, -1
    for j in range(len(dp)):
        if dp[j][0] < ed:
            if x < dp[j][1]:
                y = j
                x = dp[j][1]
    if x == -1 and y == -1: dp.append([ed, 1])
    else : dp.append([ed, dp[y][1]+1])

k = -1
for i in range(len(dp)):
    k = max(k, dp[i][1])

print(n-k)
