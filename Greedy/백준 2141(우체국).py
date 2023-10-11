import sys

n = int(input())
lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

lst.sort()

temp = [0]*n
temp[0] = lst[0][1]

for i in range(1, n):
    temp[i] = temp[i-1] + lst[i][1]

for i in range(n):
    l = temp[i]
    r = temp[n-1] - l
    print(l, r)
    if l >= r:
        print(lst[i][0])
        break
print(temp)