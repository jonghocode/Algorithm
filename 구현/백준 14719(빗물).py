h, w = map(int, input().split())
lst = list(map(int, input().split()))

t = max(lst)
board = [[0]*w for _ in range(h)]
for i in range(t):
    for j in range(w):
        if lst[j] >= t - i:
            board[i][j] = 1

answer = 0
for i in range(h):
    st = -1
    for j in range(w):
        if board[i][j] == 1 and st == -1:
            st = j
        elif board[i][j] == 1:
            answer += j-st-1
            st = j

print(answer)
