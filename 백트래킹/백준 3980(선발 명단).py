import sys

def back(d, sum, cnt):
    global answer
    # d로 놔두지 않는 이유 : d 만큼 갔지만 11개가 다 안채워 졌을수도 있음
    if cnt == 11:
        answer = max(answer, sum)
        return

    # 처음에 이런식으로 풀었었는데 열 체크 부분도 d 처럼 인수로 넘겨주는 바람에
    # 답이 틀리게 나왔었다. 열체크 부분은 chk배열을 사용해야함. 이유는
    # 무조건 자신의 뒤에 있는 거를 고르는게 답이 아니기 때문이다
    for j in range(11):
        if board[d][j] != 0 and chk[j] == 0:
            chk[j] = 1
            back(d+1, sum + board[d][j], cnt+1)
            chk[j] = 0

test = int(input())
for _ in range(test):
    answer = -1
    chk = [0]*11
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    back(0, 0, 0)
    print(answer)