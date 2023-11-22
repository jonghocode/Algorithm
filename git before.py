# n <= 100,000 -> nlog(n) or 그리디 or 투포인터
# 이 문제는 그리디(힙 사용 x)

n = int(input())
lst = list(map(int, input().split()))
M = max(lst)
chk = [0 for _ in range(M+1)]

for i in lst:
    chk[i] = 1

answer = [0 for _ in range(M+1)]

for i in lst:
    cnt = 2
    while True:
        if i*cnt > M:
            break
        if chk[i*cnt] == 1:
            answer[i] += 1
            answer[i*cnt] -= 1
        cnt += 1
            
for i in lst:
    print(answer[i], end=' ')