# 지금 위치에서 E 위치까지 바로 갈 수 있나? 체크
# 안된다면 이동할 수 있는 우산 위치 넣기
# 도착지점으로 갈 수 있으면 답 갱신

n, h, d = map(int, input().split())
board = [list(input()) for i in range((n))]
umbrella = []

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'E':
            ex, ey = i, j
        elif board[i][j] == 'U':
            umbrella.append([i, j])

answer = 987654321
chk = [0]*11 # 우산 좌표 체크

def back(x, y, h, um, deep):
    # x좌표, y좌표, 체력, 내구도, 깊이
    global ex, ey, d, answer
    # print(f"x : {x}, y : {y}, h : {h}, um : {um}, deep : {deep}")
    if abs(x-ex) + abs(y-ey) <= h + um: # 현재 위치에서 안전지대까지 바로 갈 수 있으면
        answer = min(answer, deep + abs(x-ex) + abs(y-ey))
        return
    
    for i in range(len(umbrella)):
        distance = abs(umbrella[i][0] - x) + abs(umbrella[i][1] - y)
        if chk[i] == 0 and distance <= h + um: # 방문하지 않았고 갈 수 있다면
            chk[i] = 1
            if distance > um: # 남은 거리가 내구도 보다 더 크면
                back(umbrella[i][0], umbrella[i][1], h - (distance - um), d, deep +distance)
            else: # 우산 내구도만으로 갈 수 있다면
                back(umbrella[i][0], umbrella[i][1], h, d, deep + distance)
            chk[i] = 0



back(sx, sy, h, 0, 0)
if answer == 987654321:
    answer = -1
print(answer)