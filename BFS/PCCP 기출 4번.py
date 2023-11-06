from collections import deque

def solution(maze):
    answer = 0
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1]
    chk = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)]for _ in range(4)]
    
    n = len(maze)
    m = len(maze[0])
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rsx, rsy = i, j
            elif maze[i][j] == 2:
                bsx, bsy = i, j
            elif maze[i][j] == 3:
                rex, rey = i, j
            elif maze[i][j] == 4:
                bex, bey = i, j
    
    q = deque([])
    q.append([rsx, rsy, bsx, bsy, 0, 0, 0])
    chk[rsx][rsy][bsx][bsy] = 1
    
    while q:
        rx, ry, bx, by, d, rstate, bstate = q.popleft()
        print(rx, ry, bx, by, d, rstate, bstate)
        
        if rstate == 1 and bstate == 1:
            answer = d
            break
        
        for i in range(4):
            nx, ny = rx+dirx[i], ry+diry[i]
            for j in range(4):
                sw = 0
                sw2 = 0
                nx2, ny2 = bx+dirx[j], by+diry[j]
                if rstate == 1: # 빨간색이 도착했다면 파란색만 움직이기
                    sw = 1
                    if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m:
                        continue
                    if rx == nx2 and ry == ny2:
                        continue
                    if maze[nx2][ny2] == 5:
                        continue
                    if chk[rx][ry][nx2][ny2] == 1:
                        continue
                    if nx2 == bex and ny2 == bey:
                        sw2 = 1
                    chk[rx][ry][nx2][ny2] = 1
                    q.append([rx, ry, nx2, ny2, d+1, sw, sw2])
                    
                elif bstate == 1: # 파란색이 도착했다면 빨간색만 움직이기
                    sw2 = 1
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if bx == nx and by == ny:
                        continue
                    if maze[nx][ny] == 5:
                        continue
                    if chk[nx][ny][bx][by] == 1: # 새로추가
                        continue
                        
                    if nx == rex and ny == rey:
                        sw = 1

                    chk[nx][ny][bx][by] = 1
                    q.append([nx, ny, bx, by, d+1, sw, sw2])
                else:
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m:
                        continue
                    if maze[nx][ny] == 5 or maze[nx2][ny2] == 5:
                        continue
                    if nx == nx2 and ny == ny2:
                        continue
                    if nx == bx and ny == by:
                        continue
                    if nx2 == rx and ny2 == ry:
                        continue
                        
                    if chk[nx][ny][nx2][ny2] == 1:
                        continue
                        
                    if nx == rex and ny == rey:
                        sw = 1
                    
                    if nx2 == bex and ny2 == bey:
                        sw2 = 1

                    chk[nx][ny][nx2][ny2] = 1
            
                    q.append([nx, ny, nx2, ny2, d+1, sw, sw2])
                    
    
    return answer
