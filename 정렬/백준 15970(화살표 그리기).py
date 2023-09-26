import sys

n = int(input())
lst = []
answer = 0

for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().strip().split())))

lst.sort(key = lambda x: (x[1],x[0]))

answer = lst[1][0] - lst[0][0] + lst[n-1][0] - lst[n-2][0]
for i in range(1, n-1):
    m = 987654321
    if lst[i][1] == lst[i-1][1]:
        m = min(m, lst[i][0] - lst[i-1][0])
    if lst[i][1] == lst[i+1][1]:
        m = min(m, lst[i+1][0] - lst[i][0])
    answer += m

print(answer)