# 로봇 조종하기
# 제일 높은 수를 박고 시작
n, left, right = map(int, input().split())
lst = [1]*n
max_value = max(left, right)

if left + right > n + 1: # 예외처리
    print(-1)
    exit(0)

lst[n-right] = max_value # 높은 것 먼저 놓기
cnt = 2
for i in range(n-2, n-right, -1): # 최댓값까지 오른쪽 값 최소로 놓기
    lst[i] = cnt
    cnt += 1

# if b != 1:
#     lst[n-1] = 1
# if lst[n-right] > 1:
#     a -= 1
# if a == 0 and k1 == 1:
#     p = lst[n-b]
#     lst[n-b] = 1
#     lst[0] = p
if left == 1:
    lst[n-right] = 1
    lst[0] = max_value
else:
    temp = left-1
    for i in range(n-1-right, n-right-left, -1):
        lst[i] = temp
        temp -= 1

for i in range(n):
    print(lst[i], end=' ')