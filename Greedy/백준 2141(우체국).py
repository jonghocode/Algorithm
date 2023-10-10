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
import sys

n = int(input())
lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

answer, answeridx = -1, -1
for i in range(n):
    if i == 0:
        sum = lst[i+1][1]
    elif i == n-1:
        sum = lst[i-1][1]
    else:
        sum = lst[i-1][1] + lst[i+1][1]
    if sum > answer:
        answer = sum
        answeridx = lst[i][0]

print(answeridx)