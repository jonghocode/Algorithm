import sys

n = int(input())
lst = []
for i in range(n):
    st, ed = map(int, sys.stdin.readline().split())
    lst.append((st, 1))
    lst.append((ed, -1))

lst.sort()
answer = []
cnt = 0
for i in range(n*2):
    answer.append(cnt)
    cnt += lst[i][1]
print(max(answer))