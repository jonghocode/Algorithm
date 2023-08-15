from collections import deque
import sys

a, b = map(int, input().split())
q = deque([])
q.append([a, 1])

while q:
    x, d = q.popleft()
    if x > b:
        continue
    if x == b:
        print(d)
        sys.exit(0)

    q.append([x*2, d+1])
    q.append([x*10+1, d+1])
    
print(-1)