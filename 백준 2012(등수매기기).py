import sys

n = int(input())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

answer = 0
lst.sort()
for i in range(n):
    answer += abs(lst[i]-(i+1))

print(answer)
