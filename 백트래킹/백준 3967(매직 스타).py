# (1,1, 1,3, 1,5, 1,7)
# (0,4, 1,3, 2,2, 3,1)
# (0,4, 1,5, 2,6, 3,7)
# (3,1, 3,3, 3,5, 3,7)
# (1,1, 2,2, 3,3, 4,4)
# (1,7, 2,6, 3,5, 4,4)


def back(d, n, idx): # 합을 구해야하는 6개를 미리 다 구해놓고 여기서 더하기만 하기
    if temp[1][1] + temp[1][3] + temp[1][5] + temp[1][7] > 26:
        return
    if temp[0][4] + temp[1][3] + temp[2][2] + temp[3][1] > 26:
        return
    if temp[0][4] + temp[1][5] + temp[2][6] + temp[3][7] > 26:
        return
    if temp[3][1] + temp[3][3] + temp[3][5] + temp[3][7] > 26:
        return
    if temp[1][1] + temp[2][2] + temp[3][3] + temp[4][4] > 26:
        return
    if temp[1][7] + temp[2][6] + temp[3][5] + temp[4][4] > 26:
        return
    
    if d == n:
        for i in range(5):
            for j in range(9):
                if temp[i][j] != 0:
                    print(chr(temp[i][j]+64), end='')
                else:
                    print(board[i][j], end='')
            print()
        exit()

    for j in range(1, 13): # 사전순이므로 위에 있는 행 부터 채워야 한다. 행은 함수의 인수로 컨트롤하고 열 부분은 방문배열로 컨트롤 / 여기서 2중 for문을 쓰면 시간초과
        if chk[j] == 0:
            chk[j] = 1
            temp[select[idx][0]][select[idx][1]] = j
            back(d+1, n, idx+1)
            temp[select[idx][0]][select[idx][1]] = 0
            chk[j] = 0


board = [] # 문자열 입력받는 리스트
temp = [[0 for _ in range(9)] for _ in range(5)] # 숫자로 저장할 리스트
select = [] # x인 좌표
chk = [0]*13

for i in range(5):
    board.append(list(input()))
    for j in range(len(board[i])):
        if board[i][j] == 'x':
            select.append([i, j])
        if board[i][j] != 'x' and board[i][j] != '.':
            chk[ord(board[i][j]) - 64] = 1
            temp[i][j] = ord(board[i][j]) - 64

back(0, len(select), 0)