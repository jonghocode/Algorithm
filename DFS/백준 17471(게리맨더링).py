from collections import deque

def bfs(deep):
    q = deque()
    visit = chk[:]
    temp = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            q.append(i)
            temp += 1
            visit[i] = 1
            break
    while q:
        k = q.popleft()
        for p in graph[k]:
            if visit[p] == 0:
                visit[p] = 1
                temp += 1
                q.append(p)
    
    if temp == deep:
        return True
    else:
        return False

def back(now, sum, d):
    global answer
    if d == 6:
        return
    if bfs(n-d):
        answer = min(answer, abs((personsum-sum)-sum))
        # print(chk, abs((personsum-sum)-sum))

    for go in graph[now]:
        if chk[go] == 0:
            chk[go] = 1
            back(go, sum + person[go-1], d+1)
            chk[go] = 0


n = int(input())
person = list(map(int, input().split()))
personsum = sum(person)
answer = 0x7fffffff
graph = {i : [] for i in range(1, n+1)}
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        if temp[j] not in graph[i+1]:
            graph[i+1].append(temp[j])
            graph[temp[j]].append(i+1)


for i in range(1, n+1):
    chk = [0]*(n+1)
    chk[i] = 1
    back(i, person[i-1], 1)

print(answer if answer != 0x7fffffff else -1)