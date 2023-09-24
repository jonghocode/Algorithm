# 비어 있는 칸 중에서 좋아하는 학생 가장 많은 칸을 골라서 리스트에 [인접 개수, 비어있는 칸, x, y] 이대로 정렬 후 넣기
# 마지막에 점수 구하기

n = int(input())
favorite = []
board = [[0]*(n+1) for _ in range(n+1)]
zx, zy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n*n):
    favorite.append(list(map(int, input().split())))

    student = favorite[i][0]
    find = []
    for a in range(1, n+1):
        for b in range(1, n+1):
            fcnt, empty = 0, 0 # 인접 개수, 비어있는 칸
            if board[a][b] != 0:
                continue
            for dir in range(4):
                x, y = zx[dir] + a, zy[dir] + b
                if x < 1 or x > n or y < 1 or y > n:
                    continue
                for k in range(1, 5): # 이 반복문은 위에서 리스트를 새로 만들어서 in 을 쓰면 없앨 수 있음
                    if board[x][y] == favorite[i][k]:
                        fcnt += 1
                if board[x][y] == 0:
                    empty += 1
            find.append([fcnt, empty, a, b])
    find.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    board[find[0][2]][find[0][3]] = student

favorite.sort()
answer = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt = 0
        for dir in range(4):
            x, y = zx[dir] + i, zy[dir] + j
            if x < 1 or x > n or y < 1 or y > n:
                continue
            for k in range(1, 5):
               if favorite[board[i][j]-1][k] == board[x][y]:
                    cnt += 1
        if cnt >= 1:
            answer += 10**(cnt-1)

print(answer)
