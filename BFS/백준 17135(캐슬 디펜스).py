# 거리가 d 이하인 적 중에서 가장 가까운 적, 길이 같은게 여러개면 가장 왼쪽(정렬)
# 같은 적은 여럿의 궁수에게 공격 당할 수 있음(배열에 1로 체크)
# 궁수 배치(백트래킹으로 3명)하기
# 거리 되는 애들 먼저 뽑고(처음에 좌표로 입력 다 받기)
# 적이 이동하는 것을 컨트롤 -> n-1 에서 궁수 공격 후 n-2로 줄이기

def go(where, temp):
    global n, m, d
    t = [[0]*m for _ in range(n)]
    cnt = 0

    for now in range(n-1, -1, -1): # 현재 맵 크기
        new = []
        for x, y in temp: # 적 좌표 새로 맞추기
            if x <= now and t[x][y] == 0:
                new.append([x, y])
        for k in where:
            chk = []
            for p in range(len(new)):
                if abs(now+1 - new[p][0]) + abs(k - new[p][1]) <= d:
                    chk.append([new[p][0], new[p][1], abs(now+1 - new[p][0]) + abs(k - new[p][1])])
               
            chk.sort(key = lambda x : (x[2], x[1]))
            if chk: # 공격할 수 있는 적이 있다면
                t[chk[0][0]][chk[0][1]] = 1

    # 죽인 적을 카운트
    for i in range(n):
        for j in range(m):
            if t[i][j] == 1:
                cnt += 1

    return cnt
        
        
                    

def back(where, temp, idx, deep):
    global answer
    if deep == 3:
        answer = max(answer, go(where, temp)) # 적의 수 구하기
        return
            
    for i in range(idx, m):
        where.append(i)
        back(where, temp, i+1, deep+1)
        where.pop()

n, m, d = map(int, input().split())
board = []
temp = []
answer = -1
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 1:
            temp.append([i, j])

back([], temp, 0, 0)
print(answer)