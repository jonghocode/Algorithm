import sys

lst, dp1, dp2 = [], [0]*310, [0]*310
n = int(input())

for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

# 초기화
dp1[0], dp2[0] = lst[0], lst[0]
if n>1: # indexerror 방지
    dp1[1], dp2[1] = lst[0]+lst[1], lst[1]

# 규칙
# dp1은 한 칸 씩 올라오므로 두계단을 참조해야함
# dp2는 두 칸 씩 올라오므로 어느것을 참조하든 상관없음
for i in range(2, n):
    dp1[i] = dp2[i-1] + lst[i]
    dp2[i] = max(dp1[i-2], dp2[i-2]) + lst[i]

print(max(dp1[n-1], dp2[n-1]))