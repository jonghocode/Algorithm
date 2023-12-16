def back(d, idx, end):
    global answer

    if d == end:
        start = []
        link = []
        for i in range(n):
            if chk[i] == 1:
                start.append(i)
            else:
                link.append(i)

        startsum, linksum = 0, 0
        for i in range(len(start)):
            for j in range(i+1, len(start)):
                startsum += board[start[i]][start[j]]
                startsum += board[start[j]][start[i]]

        for i in range(len(link)):
            for j in range(i+1, len(link)):
                linksum += board[link[i]][link[j]]
                linksum += board[link[j]][link[i]]
        
        if answer > abs(startsum-linksum):
            answer = abs(startsum-linksum)
        
        return
    
    for i in range(idx, n):
        if chk[i] == 0:
            chk[i] = 1
            back(d+1, i+1, end)
            chk[i] = 0
    

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
chk = [0]*n
answer = 0x7fffffff

for i in range(1, n):
    back(0, 0, i)

print(answer)