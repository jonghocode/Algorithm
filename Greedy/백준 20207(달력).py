# 시작일이 같을 경우 기간이 긴 것이 먼저 채워진다 -> x 오름차순, y 내림차순
# 처음에 일단 정렬을 시켰었는데 이렇게 빈도 체크 하는 방식은 정렬이 필요가 없다
# 시간 복잡도 : O(n^2)
n = int(input())
calendar = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[0], -x[1]))
board = [0 for _ in range(366)]

for i in range(n):
    for j in range(calendar[i][0], calendar[i][1]+1):
        board[j] += 1

answer, cnt, m = 0, 0, 0
for i in range(1, 366):
    if board[i] == 0:
        answer += cnt*m
        cnt, m = 0, 0
    else:
        cnt += 1
        m = max(m, board[i])

answer += cnt*m # 계산이 덜 끝난 경우가 있을 수 있으므로
print(answer)