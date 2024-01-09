def quad(l, r, u, d):
    if l == r == u == d:
        answer.append(board[l][r])
        return 
    one, two = 0, 0
    for i in range(u, d+1):
        for j in range(l, r+1):
            if one != 0 and two != 0:
                break
            if board[i][j] == '0':
                one += 1
            elif board[i][j] == '1':
                two += 1
    if one != 0 and two != 0:
        answer.append('(')
        quad(l, (l+r)//2, u, (u+d)//2)
        quad((l+r)//2 + 1, r, u, (u+d)//2)
        quad(l, (l+r)//2, (u+d) // 2 + 1, d)
        quad((l+r)//2 + 1, r, (u+d) // 2 + 1, d)
        answer.append(')')
    elif one == 0:
        answer.append(1)
        return
    else:
        answer.append(0)
        return
    

n = int(input())
board = [list(input()) for _ in range(n)]
answer = []
quad(0, n-1, 0, n-1)
print(''.join(map(str, answer)))