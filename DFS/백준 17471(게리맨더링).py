from collections import deque

def bfs(chk):
    q = deque()
    visit = chk[:]

    # chk가 0인 부분과 1인 부분 각각 사이클 되는지 구하기
    zero, one, zerosum, onesum = 0, 0, 0, 0
    temp, temp2 = [0]*(n+1), [0]*(n+1)
    
    for i in range(1, n+1):
        if chk[i] == 0:
            q.append(i)
            zero += 1; temp[i] = 1; zerosum += person[i-1]
            break
    
    for i in range(1, n+1):
        if chk[i] == 1:
            q.append(i)
            one += 1; temp2[i] = 1; onesum += person[i-1]
            break
    
    while q:
        now = q.popleft()
        for go in graph[now]:
            if chk[now] == 0:
                if visit[go] == 0 and temp[go] == 0: # 방문하지 않았고 0인 구역이라면
                    q.append(go)
                    temp[go] = 1; zero += 1; zerosum += person[go-1]
            elif chk[now] == 1: # 방문했고 1인 구역이라면
                if visit[go] == 1 and temp2[go] == 0:
                    q.append(go)
                    temp2[go] = 1; one += 1; onesum += person[go-1]

    if zero + one == n: # 사이클이 완성되었으면
        return abs(onesum - zerosum)
    else:
        return 0x7fffffff

def back(idx, d):
    global answer
    
    answer = min(answer, bfs(chk))

    for i in range(idx, n): # 백트래킹으로 조합 구하기
        if chk[i] == 0:
            chk[i] = 1
            back(i+1, d+1)
            chk[i] = 0


n = int(input())
person = list(map(int, input().split()))
answer = 0x7fffffff
graph = {i : [] for i in range(1, n+1)}
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        graph[i+1].append(temp[j])
        graph[temp[j]].append(i+1)


chk = [0]*(n+1)
back(0, 0)

print(answer if answer != 0x7fffffff else -1)