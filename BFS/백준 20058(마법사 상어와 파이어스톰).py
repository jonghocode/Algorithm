n, q = map(int, input().split())
n = 2**n
board = [list(map(int, input().split())) for _ in range(n)]

for _ in range(q):
    L = 2**int(input())
    temp = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    
    while True:
        # x 는 0부터 l까지
        # y가 범위를 벗어난다면 x의 기준을 바꾸기
        tx = x-1
        ty = y+L-1
        for i in range(x, x+L):
            
            tx = x
            for j in range(y, y+L):
                temp[tx][ty] = board[i][j]
                print(tx, ty)
                tx+=1
            
                for o in range(n):
                    for p in range(n):
                        print(temp[o][p], end=' ')
                    print()
           
            ty -= 1
            
        # 0 2
        # 0 2
        # 0 2
        # 2 4
        # 4 6
        # 6 8
        y += L
        if y >= n-1:
            x += L
            y = 0
        if x >= n-1:
            break
        
    
    # lst를 다시 board로 넣기


# r, c에는 얼음의 양
# L은 2^l * 2^l 만큼 나누기
# 모든 격자 부분 회전
# 각 격자 안에서 모든 칸에 대해 4 방향을 확인 후 chk배열에 1이 줄어들것인지 표시

# 1,1 - 1,n
# 1,2 - 2,n
# 1,3 - 3,n
# 1,4 - 4,n

# 2,1 - 1,3
# 2,2 - 2,3
# 2,3 - 3,3
# 2,4 - 4,3

# 1,5 - 1,8
# 1,6 - 2,8
# 1,7 - 3,8
# 



# 원본배열의 y값이 복사배열의 x로 가고, 복사배열의 y는 n-1부터 0까지 줄어들게
# 2중 for문에서 돈다
num = 1
for i in range(1, 9):
    for j in range(1, 9):
        print(num, end=' ')
        num+=1
    print()