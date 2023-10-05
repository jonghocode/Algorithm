def check(board): # 감시 시작
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i, j in teacher:
        for k in range(4):
            tx, ty = i, j
            while True:
                if tx < 0 or ty < 0 or tx >= n or ty >= n:
                    break
                if board[tx][ty] == 'S':
                    return False
                if board[tx][ty] == 'O':
                    break
                tx, ty = tx + dirx[k], ty + diry[k]

    return True
            

def back(d, idx, board):
    if d == 3:
        if check(board): # bfs가 True라면 모든 학생들로 부터 감시를 피한 것
            print("YES")
            exit()
        return
    for i in range(idx, len(candidate)):
        # 미리 좌표를 넣어주고 idx로 컨트롤 해주면 따로 chk 배열도 필요없이 컨트롤을 할 수 있어서
        # 빠르고 쉽다
        board[candidate[i][0]][candidate[i][1]] = 'O'
        back(d+1, i+1, board)
        board[candidate[i][0]][candidate[i][1]] = 'X'
    

n = int(input())
board = []
teacher = [] # 선생님 좌표
candidate = [] # 장애물이 될 후보
for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 'T': # 선생님 좌표 넣기 -> 큐 초기값
            teacher.append([i, j])
        elif board[i][j] == 'X':
            candidate.append([i, j]) # 비어있는 공간 좌표 넣기

back(0, 0, board)
print("NO") # 위에서 YES가 나오지 않는다면 프로그램이 끝나지 않기 때문에 출력