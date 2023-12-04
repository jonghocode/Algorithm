from collections import deque

def bfs(st, ed):
    q = deque()
    q.append([st, 0])
    visit = {st : 1}

    while q:
        now, d = q.popleft()
        if now == ed:
            return d
        
        lst = list(str(now))

        for i in range(4):
            temp = list(lst)
            for j in range(10):
                temp[i] = str(j)
                k = int(''.join(map(str, temp)))
                if k < 1000 or k > 9999 or chk[k] == 0 or k in visit:
                    continue
                visit[k] = 1
                q.append([k, d+1])


    
    return "Impossible"

chk = [1]*10000
for i in range(2, int(10000**0.5)):
    for j in range(i+i, 10000, i):
        chk[j] = 0

t = int(input())
for i in range(t):
    st, ed = map(int, input().split())
    print(bfs(st, ed))