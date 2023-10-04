import sys

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))

lst.sort(key = lambda x : (-x[1], -x[0]))

st = lst[0][1] - lst[0][0]
for i in range(1, n):
    if st > lst[i][1]:
        st = lst[i][1] - lst[i][0]
    else:
        st -= lst[i][0]
print(st)