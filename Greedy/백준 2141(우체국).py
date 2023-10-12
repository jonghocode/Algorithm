# 3, 5, 5, 5, 3
# 5 + 10 + 15 + 12 = 42
# 3 + 5 + 10 + 9 = 27
# 6 + 5 + 5 + 6 = 22 -> 3번째에 세웠을 때
# 3 + 5 + 10 + 9 = 27
# 5 + 10 + 15 + 12 = 42


# 100 50 50 5
# answer : 2

# 1 5 100 3 6 66 66 66

# 1   2  3  4
# 100 98 99 100
# 1,100
# 2,98
# 3,99
# 4,100
# 1 : 98 + 99*2 + 100*3 198+300+98
# 2 : 100 + 99 + 100*2 399
# 3 : 100*2 + 98 + 100 398
# 4 : 100*3 + 98*2 + 99 x


# len > 1 일 때 리스트에 있는 값이 다 똑같다면 무조건 idx가 1인곳이 답
# 양쪽의 합이 제일 큰 idx

# -1    2   5     100
# -1000   
import sys

n = int(input())
lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

st = 0
d = 0
lst.sort()
l = [0]*2000000010
r = [0]*2000000010
for i in range(n):
    s, e = lst[i][0], lst[i][1]
    l[s] = l[s-1]
    d += lst[i][1]
    l[s] += d*abs(lst[i][0] - st)
    st = s

st = n-1
d = 0
for i in range(n-1, -1, -1):
    s, e = lst[i][0], lst[i][1]
    r[s] = r[s+1]
    d += lst[i][1]
    r[s] += d*abs(lst[i][0] - st)
    st = s

answer = 0x7fffffff
for i in range(n):
    if i == 0:
        if answer > r[i+1]:
            answer = r[i+1]
            idx = i
    elif i == n-1:
        if answer > l[i-1]:
            answer = l[i-1]
            idx = i
    else:
        if answer > l[i-1] + r[i+1]:
            answer = l[i-1] + r[i+1]
            idx = i

print(idx)