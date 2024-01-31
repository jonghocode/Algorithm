# 0이 있다면 -를 묶는다.
# 1과 1은 묶지 않는다.
# 음수는 처음부터, 양수는 끝에서부터 묶는다.

import sys
n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()
answer = 0
chk = [0 for _ in range(n)]
if n > 1:
    for i in range(0, n, 2):
        if lst[i] > 0 or lst[i+1] > 0:
            break
        answer += lst[i]*lst[i+1]
        chk[i], chk[i+1] = 1, 1

    for i in range(n-1, -1, -2):
        if lst[i] <= 1 or lst[i-1] <= 1:
            break
        if chk[i] == 0 and chk[i-1] == 0:
            answer += lst[i]*lst[i-1]
            chk[i], chk[i-1] = 1, 1

for i in range(n):
    if chk[i] == 0:
        answer += lst[i]
print(answer)