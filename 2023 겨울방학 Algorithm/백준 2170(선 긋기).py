import sys

n = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lst.sort()

answer = 0
st, ed = lst[0][0], lst[0][1]

sw = 0
for i in range(1, n):
    if st <= lst[i][0] and lst[i][1] <= ed: # 선이 완전히 포함된다면 continue
        continue
    if lst[i][0] <= ed and lst[i][1] > ed: # 이번 시작점이 그 전 값보다 작고 끝 값이 더 크다면 끝값만 바꾸기
        ed = lst[i][1]
        sw = 0
    else:
        answer += ed - st
        sw = 1
        st, ed = lst[i][0], lst[i][1]

# 마지막에 답 한번 더 더해주기
answer += ed - st
print(answer)