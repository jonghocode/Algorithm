import sys

n, d, k, c = map(int, input().split())  # 접시 수, 가짓 수,  연속, 쿠폰
answer, cnt = 0, 0
lst = [0] * 60010
chk = [0] * 60010

for i in range(1,n+1):
    lst[i] = int(sys.stdin.readline().strip())
    lst[i+n] = lst[i]
    

for i in range(1, n+k+1):
    if chk[lst[i]] == 0:
        chk[lst[i]] += 1
        cnt += 1
    else :
        chk[lst[i]] += 1
    if i > k:
        # 빼기
        chk[lst[i-k]] -= 1
        if chk[lst[i-k]] == 0:
            cnt -= 1
    if i >= k and chk[c] == 0: # 쿠폰 확인
        answer = max(answer, cnt+1)
    answer = max(answer, cnt)

print(answer)