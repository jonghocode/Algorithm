def dfs(x,ch):
    global p, answer
    ch[x] = 1
    p+=1
    for i in range(7):
        if ch[i] == 0 and abs(dab[x][0] - dab[i][0]) + abs(dab[x][1] - dab[i][1]) == 1:
            dfs(i, ch)

def seven(n, y, d):
    global p, answer
    if y > 3:
        return
    if d == 7:
        p = 0
        for i in range(7):
            ch = [0]*7
        dfs(0, ch)
        if p == 7:
            answer += 1
            return
            

    if n >= 25:
        return
    
    chk[n//5][n%5] = 1; dab[d][0] = n//5; dab[d][1] = n%5 # 25개 중 하나 선택
    if student[n//5][n%5] == 'Y':
        seven(n+1, y+1, d+1)
    else:
        seven(n+1, y, d+1)
    chk[n//5][n%5] = 0

    seven(n+1, y, d) # 25개 중 선택하지 않은 경우
    


student = [input() for _ in range(5)]
chk = [[0]*7 for _ in range(7)] # 방문 체크
dab = [[0]*2 for _ in range(10)] # 7공주 x,y좌표 저장
answer = 0
seven(0, 0, 0) # x, y 좌표, 임도연파 학생 수, 총 깊이
print(answer)