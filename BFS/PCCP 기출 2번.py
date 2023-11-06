from collections import deque

def solution(land):
    
    def bfs(cnt, i, j):
        q = deque([])
        q.append([i, j])
        chk[i][j] = cnt
        cnt2 = 0
        while q:
            x, y = q.popleft()
            cnt2 += 1
            for i in range(4):
                nx, ny = x + dirx[i], y + diry[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if chk[nx][ny] != 0:
                    continue
                if land[nx][ny] == 0:
                    continue
                chk[nx][ny] = cnt
                q.append([nx, ny])
        return cnt2
    
    answer = -1
    
    n = len(land)
    m = len(land[0])
    
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    chk = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 1
    lst = []
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and chk[i][j] == 0:
                lst.append(bfs(cnt, i, j))
                cnt += 1
    # lst[chk[i][j]-1]에 값 있음
    
    for i in range(m):
        sum = 0
        dict = {}
        for j in range(n):
            if chk[j][i] not in dict and chk[j][i] != 0:
                dict[chk[j][i]] = 1
                sum += lst[chk[j][i]-1]
        answer = max(answer, sum)
    
    return answer
