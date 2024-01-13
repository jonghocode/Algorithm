from collections import deque

def key(n):
    num = n%X
    hash[num].append(n)

def p(board):
    s = 0
    for i in range(3):
        for j in range(3):
            s = s*10 + board[i][j]
    return s


X = 123777
hash = [[] for i in range(X)]
board = [list(map(int, input().split())) for i in range(3)]
dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
temp = p(board)

q = deque([(temp, 0)])
while q:
    now, d = q.popleft()
    now = str(now)
    k = now.find('0')
    if now == '123456780':
        print(d)
        exit()
    for i in range(len(dir[k])):
        t = k
        s = ''
        for j in range(9):
            if j == k:
                s += str(now[dir[k][i]])
            elif j == dir[k][i]:
                s += str(now[k])
            else:
                s += str(now[j])
        
        z = int(s) % X
        sw = 0
        for i in range(len(hash[z])):
            if hash[z][i] == s:
                sw = 1
                break
        if sw == 0:
            q.append((s, d+1))
            hash[z].append(s)
    
print(-1)