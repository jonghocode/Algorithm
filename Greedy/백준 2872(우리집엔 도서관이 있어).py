import sys
n = int(input())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

st = n
cnt = 0
# 최댓값을 먼저 찾은 후에 총 개수에서 최댓값을 기준으로 내림차순 되어 있는 것이 몇 개 인지 체크
for i in range(n-1, -1, -1):
    if lst[i] == st:
        cnt += 1
        st -= 1
print(n-cnt)
