def solution(park, routes):
    
    def move(sw, n, x, y):
        tx, ty = x, y
        while n != 0:
            nx, ny = x + dirx[sw], y + diry[sw]
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]) or park[nx][ny] == 'X':
                return tx, ty
            n -= 1
            x = nx
            y = ny
            
        return x, y
    
    dirx, diry = [-1, 1, 0, 0], [0, 0, -1, 1] # 북, 남, 서, 동
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    for i in routes:
        if i[0] == 'N':
            sw = 0
        elif i[0] == 'S':
            sw = 1
        elif i[0] == 'W':
            sw = 2
        else:
            sw = 3
        x, y = move(sw, int(i[2]), x, y)
    
    
    return [x, y]