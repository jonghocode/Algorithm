from collections import deque
n, k = map(int, input().split())
q = deque()
for i in range(1, n+1):
    q.append(i)
cnt = 1
answer = 0
print("<", end='')
while q:
    temp = q.popleft()
    if cnt == k:
        if answer == 0:
            print(temp, end='')
        else:
            print(f", {temp}", end='')
        cnt = 0
        answer += 1
    else:
        q.append(temp)
    cnt += 1
print(">")