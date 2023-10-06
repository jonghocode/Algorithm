from collections import deque

# q를 쓰는게 좋을 듯
wheel = []
for i in range(4):
    wheel.append(list(input()))
k = int(input())
for i in range(k):
    num, where = map(int, input().split())

print(wheel)