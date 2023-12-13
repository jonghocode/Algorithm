# 테이블은 지나가게하고 파티션은 못지나가게 한 후 상하좌우로 2번 움직이는데 있으면 바로 0리턴이고
# 없으면 지나감

def solution(places):
    global state
    answer = []
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def dfs(x, y, d):
        global state

        if board[x][y] == 'P' and d!=0:
            state = False
            return
        if d == 2:
            return
        
        for i in range(4):
            nx, ny = x + dirx[i], y + diry[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if board[nx][ny] == 'X':
                continue
            if visit[nx][ny] == 1:
                continue
            dfs(nx, ny, d+1)
            
        
        
    for i in range(5):
        board = []
        for j in range(5):
            board.append(list(places[i][j]))
        
        person = []
        for x in range(5):
            for y in range(5):
                if board[x][y] == 'P':
                    person.append([x, y])
        

        sw = False
        for j in range(len(person)):
            visit = [[0]*5 for _ in range(5)]
            visit[person[j][0]][person[j][1]] = 1

            state = True
            dfs(person[j][0], person[j][1], 0)

            if not state:
                sw = True
                answer.append(0)
                break
        if sw == False:
            answer.append(1)
        
    return answer