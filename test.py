from collections import deque

board = [list(map(int, input().split())) for _ in range(3)]
s, X = 0, 123777
hash = [[] for _ in range(X)]
dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]

for i in range(3):
    for j in range(3):
        s = s*10 + board[i][j]

q = deque([(s, 0)])
hash[s%X].append(s)

while q:
    now, d = q.popleft()
    now = str(now)
    k = now.find('0')
    
    if now == '123456780':
        print(d)
        exit()

    for i in range(len(dir[k])):
        temp = ''
        for j in range(9):
            if j == k:
                temp += now[dir[k][i]]
            elif j == dir[k][i]:
                temp += now[k]
            else:
                temp += now[j]

        sw = 0
        for j in range(len(hash[int(temp)%X])):
            if hash[int(temp)%X][j] == temp:
                sw = 1
                break
        if sw == 0:
            hash[int(temp)%X].append(temp)
            q.append((temp, d+1))

print(-1)