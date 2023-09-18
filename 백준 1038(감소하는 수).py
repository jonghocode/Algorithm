from collections import deque

n = int(input())

if n == 0:
    print(0)
else :
    q = deque([])
    d = 0
    for i in range(1, 10):
        q.append(i)
    
    while q:
        x = q.popleft()
        d+=1
        if d == n:
            print(x)
            exit()

        t = x%10
        for i in range(10):
            if t > i:
                q.append(x*10+i)
            else :
                break
    print(-1)
