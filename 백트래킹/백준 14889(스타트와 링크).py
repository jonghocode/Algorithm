def team(x, d):
    global n, answer

    if d == n//2:
        s1 = s2 = 0
        for i in range(n):
            for j in range(n):
                if teamchk[i] == 1 and teamchk[j] == 1:
                    s1 += game[i][j]
                elif teamchk[i] == 0 and teamchk[j] == 0:
                    s2 += game[i][j]
        answer = min(answer,abs(s1-s2))
        return

    for i in range(x, n):
        teamchk[i] = 1
        team(i+1, d+1)
        teamchk[i] = 0

n = int(input())

game, teamchk, answer = [], [0]*n, 0x7fffffff
for i in range(n):
    game.append(list(map(int, input().split())))


team(0, 0)
print(answer)